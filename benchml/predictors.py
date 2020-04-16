import sklearn.linear_model

class Ridge(sklearn.linear_model.Ridge):
    def __init__(self, X, y, **kwargs):
        sklearn.linear_model.Ridge.__init__(self, **kwargs)
