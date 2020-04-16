from __future__ import print_function
from .readwrite import read
import numpy as np
import json
import os

class BenchmarkData(object):
    def __init__(self, root, filter_fct=lambda meta: True):
        paths = map(lambda sdf: sdf[0], filter(
            lambda subdir_dirs_files: "meta.json" in subdir_dirs_files[2],
                os.walk(root)))
        self.dataits = map(lambda path: DatasetIterator(
            path, filter_fct=filter_fct), paths)
    def __iter__(self):
        for datait in self.dataits:
            for dataset in datait:
                yield dataset
        return

class DatasetIterator(object):
    def __init__(self, path, filter_fct=lambda meta: True):
        self.path = path
        self.meta = json.load(open(os.path.join(path, "meta.json")))
        self.filter = filter_fct
        return
    def __iter__(self):
        for tidx, target in enumerate(self.meta["target"]):
            for didx, dataset in enumerate(self.meta["datasets"]):
                meta_this = {
                  "name": "{0}:{1}:{2}".format(
                    self.meta["name"], target, dataset),
                  "type": self.meta["type"],
                  "target": target,
                  "domain": self.meta["domain"][tidx],
                  "additive": self.meta["additive"][tidx],
                  "task": self.meta["task"][tidx],
                  "splits": self.meta["splits"],
                  "metric": self.meta["metric"][tidx],
                  "elements": self.meta["elements"],
                }
                if self.filter(meta_this):
                    yield Dataset(os.path.join(self.path, dataset), meta_this)
        return

class Dataset(object):
    def __init__(self, ext_xyz, meta):
        self.structs = read(ext_xyz)
        self.meta = meta
        self.y = np.array([ s.info[meta["target"]] for s in self.structs ])
        return
    def info(self):
        return "{name:50s} #structs={size:-5d}  task={task:8s}  metric={metric:s}".format(
            name=self.meta["name"], size=len(self.structs), 
            task=self.meta["task"], metric=",".join(self.meta["metric"]))
    def __getitem__(self, key):
        if np.issubdtype(type(key), np.integer): return self.structs[key]
        elif type(key) in {list, np.ndarray}: return [ self.structs[_] for _ in key ]
        elif type(key) is str: return self.meta[key]
        else: raise TypeError("Invalid type in __getitem__: %s" % type(key))
    def __len__(self):
        return len(self.structs)
    def __str__(self):
        return self.info()
    def __iter__(self):
        return self.structs.__iter__()

def compile(root="./data", filter_fct=lambda meta: True):
    return BenchmarkData(root, filter_fct=filter_fct)

if __name__ == "__main__":
    bench = compile()
    for data in bench:
        print(data)

