import numpy as np
import scipy.stats
import sklearn.metrics
import json

def metric_mse(yp, yt):
    return np.sum((yp-yt)**2)/yp.shape[0]

def metric_rmse(yp, yt):
    return metric_mse(yp,yt)**0.5

def metric_mae(yp, yt):
    return np.sum(np.abs(yp-yt))/yp.shape[0]

def metric_rhop(yp, yt):
    return scipy.stats.pearsonr(yp, yt)[0]

def metric_rhor(yp, yt):
    return scipy.stats.spearmanr(yp, yt).correlation

def metric_auc(yp, yt):
    return sklearn.metrics.roc_auc_score(yt,yp)

def metric_r2(yp, yt):
    return sklearn.metrics.r2_score(yt, yp)

class Accumulator(object):
    eval_map = { 
        "mae": metric_mae,
        "mse": metric_mse,
        "rmse": metric_rmse, 
        "rhop": metric_rhop,
        "auc":  metric_auc,
        "r2": metric_r2
    }
    def __init__(self, jsonfile=None):
        self.yp_map = {}
        self.yt_map = {}
        if jsonfile is not None: self.load(jsonfile)
        return
    def append(self, channel, yp, yt):
        if not channel in self.yp_map:
            self.yp_map[channel] = []
            self.yt_map[channel] = []
        self.yp_map[channel] = self.yp_map[channel] + list(yp)
        self.yt_map[channel] = self.yt_map[channel] + list(yt)
        return
    def evaluate(self, channel, metric, bootstrap=0):
        if len(self.yp_map[channel]) < 1: return np.nan
        if bootstrap == 0:
            return Accumulator.eval_map[metric](
                np.array(self.yp_map[channel]), 
                np.array(self.yt_map[channel])), 0.
        else:
            v = []
            n = len(self.yp_map[channel])
            yp = np.array(self.yp_map[channel])
            yt = np.array(self.yt_map[channel])
            for r in range(bootstrap):
                re = np.random.randint(0, n, size=(n,))
                v.append(Accumulator.eval_map[metric](yp[re], yt[re]))
            return np.mean(v), np.std(v)
    def evaluateNull(self, channel, metric, n_samples):
        if len(self.yp_map[channel]) < 1: return np.nan
        z = []
        for i in range(n_samples):
            yp_null = np.array(self.yp_map[channel])
            yt_null = np.array(self.yt_map[channel])
            np.random.shuffle(yp_null)
            z.append(Accumulator.eval_map[metric](
                yp_null, yt_null))
        z = np.sort(np.array(z))
        return z
    def evaluateAll(self, metrics, bootstrap=0, log=None):
        res = {}
        for channel in sorted(self.yp_map):
            res[channel] = {}
            vs = []
            dvs = []
            for metric in metrics:
                v, dv = self.evaluate(channel, metric, bootstrap=bootstrap)
                res[channel][metric] = v
                res[channel][metric+"_std"] = dv
                vs.append(v)
                dvs.append(dv)
            if log:
                log << "%-25s : " % (channel) << log.flush
                for v, metric in zip(vs, metrics):
                    log << "%s=%+1.4e +- %+1.4e" % (
                        metric, v, dv) << log.flush
                log << log.endl
        return res
    def save(self, jsonfile):
        json.dump({ "yp_map": self.yp_map, "yt_map": self.yt_map },
            open(jsonfile, "w"), indent=1, sort_keys=True)
        return
    def load(self, jsonfile):
        data = json.load(open(jsonfile))
        self.yp_map = data["yp_map"]
        self.yt_map = data["yt_map"]
        return

