import numpy as np
import sklearn.linear_model
from .accumulator import Accumulator
from .splits import Split
from .utils import dict_compile
from .descriptors import *
from .predictors import *

class ModelBase(object):
    def __init__(self, 
            DescriptorClass, 
            descriptor_args, 
            PredictorClass, 
            predictor_args,
            task,
            tag=None):
        self.DescriptorClass = DescriptorClass
        self.descriptor_args = descriptor_args
        self.PredictorClass = PredictorClass
        self.predictor_args = predictor_args
        self.predictor = None
        self.descriptor = None
        self.task = task
        self.tag = tag
        if self.tag is None:
            self.tag = "%s:%s" % (
                self.DescriptorClass.__name__, 
                self.PredictorClass.__name__)
    def __str__(self):
        return self.tag
    def describe(self, dataset, meta=None):
        self.descriptor = self.DescriptorClass(**self.descriptor_args)
        return self.descriptor.describe(dataset, meta)
    def fit(self, X, y, configs=None, meta=None):
        self.predictor = self.PredictorClass(X, y, **self.predictor_args)
        return self.predictor.fit(X, y)
    def predict(self, X, configs=None):
        return self.predictor.predict(X)
    def covers(self, dataset):
        check = (dataset["task"] == self.task)
        if hasattr(self.DescriptorClass, "covers"):
            check = check and self.DescriptorClass.covers(dataset)
        if hasattr(self.PredictorClass, "covers"):
            check = check and self.PredictorClass.covers(dataset)
        return check
    def hyperDim(self):
        return 1

class Model(ModelBase):
    def __init__(self,
            DescriptorClass, 
            PredictorClass, 
            task,
            tag=None,
            descriptor_args={}, 
            predictor_args={},
            # Hyperparameter-related args
            descriptor_hyper=[],
            predictor_hyper=[],
            combine_hyper='combinatorial',
            split_hyper_args={},
            metric_hyper=None,
            select_hyper=None):
        ModelBase.__init__(self, DescriptorClass, descriptor_args,
            PredictorClass, predictor_args, task=task, tag=tag)
        # Hyperparameter optimization settings
        self.do_desc_hyper = True if len(descriptor_hyper) else False
        self.do_est_hyper = True if len(predictor_hyper) else False
        self.recalc_desc = not self.do_desc_hyper
        self.desc_hyper = descriptor_hyper
        self.est_hyper = predictor_hyper
        self.combine_hyper = combine_hyper
        self.split_hyper_args = split_hyper_args
        self.metric_hyper = metric_hyper
        self.select_hyper = select_hyper
        if self.metric_hyper is not None:
            if self.select_hyper not in {"largest", "smallest"}:
                raise ValueError("Hyperselection not specified")
        self.prepareHyper()
    def prepareHyper(self):
        # Compile option lists
        self.desc_kwargs_list = dict_compile(
            self.descriptor_args, self.desc_hyper, self.combine_hyper)
        self.est_kwargs_list = dict_compile(
            self.predictor_args, self.est_hyper, self.combine_hyper)
    def hyperDim(self):
        return len(self.desc_kwargs_list)*len(self.est_kwargs_list)
    def describe(self, dataset, meta=None):
        if not self.recalc_desc: return super().describe(dataset, meta)
        else: return np.zeros((len(dataset),1))
    def fit(self, X, y, configs=None, meta=None, log=None):
        if not self.do_est_hyper: return super().fit(X, y, configs, meta)
        # Evaluate options
        kwargs_metric = []
        for dkwargs in self.desc_kwargs_list:
            self.descriptor_args = dkwargs
            if self.recalc_desc:
                self.descriptor = self.DescriptorClass(**self.descriptor_args)
                X = super().describe(configs, meta)
            for ekwargs in self.est_kwargs_list:
                accu = Accumulator()
                self.predictor_args = ekwargs
                for info, train, test in Split(X, **self.split_hyper_args):
                    super().fit(X[train], y[train])
                    yp = super().predict(X[test])
                    accu.append("test", yp, y[test])
                avg, std = accu.evaluate("test", self.metric_hyper)
                kwargs_metric.append({ 
                    "desc": dkwargs, 
                    "est": ekwargs, 
                    "metric": avg })
        # Select best
        kwargs_metrics = sorted(kwargs_metric, key=lambda m: m["metric"])
        select = None 
        if self.select_hyper == "largest": select = kwargs_metrics[-1]
        elif self.select_hyper == "smallest": select = kwargs_metrics[0]
        self.descriptor_args = select["desc"]
        self.predictor_args = select["est"]
        # Fit and return
        return super().fit(X[train], y[train])

def compile():
    return [
        Model(
            DescriptorClass=XRandom, 
            PredictorClass=Ridge, 
            task="regress"),
        Model(
            DescriptorClass=XRandom, 
            PredictorClass=Ridge, 
            task="regress",
            tag="randctrl_dim10",
            descriptor_args={"dim": 10}, 
            predictor_args={"alpha": 0.1}),
        Model(
            DescriptorClass=XRandom, 
            PredictorClass=Ridge, 
            task="regress",
            tag="randctrl_hyper",
            descriptor_args={"dim": 100}, 
            descriptor_hyper=[
                {"path": "dim", "vals": np.logspace(1, 2, 2, dtype='int') } ],
            predictor_args={"alpha": 1.0}, 
            predictor_hyper=[
                {"path": "alpha", "vals": np.logspace(-3, 3, 7)},
                {"path": "normalize", "vals": [ False, True ]} ],
            combine_hyper='combinatorial',
            split_hyper_args={"split": "mc", "n": 5, "f": 0.9},
            metric_hyper="r2",
            select_hyper="largest")
    ]

