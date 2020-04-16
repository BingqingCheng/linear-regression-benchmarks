from . import models
from .accumulator import Accumulator
from .splits import Split

def make_accu_id(model, dataset, splitter, mode):
    return "mod={model};dset={data};split={split};perf={mode}".format(
        model=str(model), 
        data=str(dataset).split()[0], 
        split=splitter.tag, 
        mode=mode)

def evaluate_model(dataset, model, accu, log):
    X = model.describe(dataset, meta=dataset.meta)
    splitter = Split(dataset, **dataset["splits"][0])
    for info, train, test in splitter:
        log << log.back << "  %-20s  %-10s  #train=%-4d  #test=%-4d  [#hyper=%d]" % (
            str(model), info, len(train), len(test), model.hyperDim()
            ) << log.flush
        configs_train = dataset[train]
        configs_test = dataset[test]
        model.fit(X[train], dataset.y[train], 
            configs=configs_train, meta=dataset.meta)
        yt = model.predict(X[train], configs_train)
        yp = model.predict(X[test], configs_test)
        accu.append(make_accu_id(model, dataset, splitter, "train"), 
            yt, dataset.y[train])
        accu.append(make_accu_id(model, dataset, splitter, "test"), 
            yp, dataset.y[test])
    log << log.endl

def evaluate_ensemble(dataset, models, log):
    log << log.mg << "Dataset: %s" % dataset << log.endl
    accu = Accumulator()
    for model in models:
        if model.covers(dataset):
            evaluate_model(dataset, model, accu, log)
    performance = accu.evaluateAll(
        metrics=dataset.meta["metric"], 
        bootstrap=100, log=None)
    return performance

def evaluate(data, models, log):
    bench = {}
    for dataset in data:
        bench.update(evaluate_ensemble(dataset, models, log))
    return bench

