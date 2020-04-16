import numpy as np

class XRandom(object):
    def covers(dataset):
        return dataset["domain"] == "global"
    def __init__(self, dim=100):
        self.dim = dim
    def describeAtomic(self, dataset, meta=None):
        X = []
        for frame in dataset:
            X.append(np.random.uniform(0., 1., size=(len(frame), self.dim)))
        return np.concatenate(X, axis=0)
    def describeGlobal(self, dataset, meta=None):
        return np.random.uniform(0., 1., size=(len(dataset), self.dim))
    def describe(self, dataset, meta):
        if meta["domain"] == "global":
            return self.describeGlobal(dataset, meta)
        else:
            return self.describeAtomic(dataset, meta)

