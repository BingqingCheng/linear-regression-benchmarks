"""
for processing data
"""

import numpy as np

from asaplib.fit.getscore import get_score
from asaplib.fit import LC_SCOREBOARD

def model_elementwise_error(model_now, select='test', compare='MSE', replica=None):
    
    n_repeats = model_now['n_repeats']

    # some options to select certain data points

    if select=='all':
        y_train = model_now['train']
        y_test = model_now['test']
        y_raw = np.concatenate([y_test,y_train])
        y_all = y_raw[np.argsort(y_raw[:, 0])]
    elif select=='train':
        if replica == None:
            y_all = model_now['train']
        else:
            y_all = model_now['train'][model_now['train'][:,-2]==replica]
    elif select=='test':
        if replica == None:
            y_all = model_now['test']
        else:
            y_all = model_now['test'][model_now['test'][:,-2]==replica]
    else:
        raise ValueError("selection not exist")

    # y_MSE, y_MAE
    if compare == 'MSE':
        # train_idcs, y_pred, y_true, submodel_id, train_or_not
        return np.asarray([v[1]-v[2] for v in y_all])
    elif compare == 'MAE':
        return np.asarray([np.abs(v[1]-v[2]) for v in y_all])
    elif compare == 'RMSE':
        return np.asarray([(v[1]-v[2])**2. for v in y_all])
    elif compare == 'y':
        return np.asarray([v[1] for v in y_all])
    else:
        raise ValueError("selection not exist")

def model_error_correlation(model_1, model_2, select='test', compare='MSE', metric='CORR', replica=None):

    
    y_1 = model_elementwise_error(model_1, select, compare, replica)
    y_2 = model_elementwise_error(model_2, select, compare, replica)
        
    return get_score(y_1, y_2)[metric]


def model_correlation_matrix(by_model, key_now, select='test', compare='MSE', metric='CORR', replica=None, verbose=True):

    correlation_matrix = np.ones((len(by_model.keys()),len(by_model.keys())))
    model_list = []

    for i, model_key_now in enumerate(by_model.keys()):
        model_list.append(model_key_now)

        for j, model_key_now_2 in enumerate(by_model.keys()):
            if i > j:
                model_now = by_model[model_key_now][key_now]
                model_now_2 = by_model[model_key_now_2][key_now]

                correlation_matrix[i, j] = correlation_matrix[j, i] = model_error_correlation(model_now, model_now_2, select, compare, metric, replica)
                if verbose: print(model_key_now, model_key_now_2, correlation_matrix[i, j])

    return correlation_matrix, model_list

def all_model_correlation_matrix(by_model, key_now_list=[], select='all', compare='MSE', metric='PearsonR', replica=None, verbose=True):

    all_corr_matrix_size = len(by_model.keys())*len(key_now_list)

    all_corr_matrix = np.ones((all_corr_matrix_size,all_corr_matrix_size))
    all_model_list = []

    for i, model_key_now in enumerate(by_model.keys()):
        for ri, r_now in enumerate(key_now_list):
            # the index of the first model
            index_model_1 = i*len(key_now_list) + ri
            all_model_list.append(str(model_key_now)+str(r_now))
        
            for j, model_key_now_2 in enumerate(by_model.keys()):
                for rj, r_now_2 in enumerate(key_now_list):
                    # the index of the second model
                    index_model_2 = j*len(key_now_list) + rj
                
                    if i > j:
                        model_now = by_model[model_key_now][r_now]
                        model_now_2 = by_model[model_key_now_2][r_now_2]
                    
                        all_corr_matrix[index_model_1,index_model_2] = all_corr_matrix[index_model_2,index_model_1] = \
                             model_error_correlation(model_now, model_now_2, select, compare, metric, replica)
                    if verbose: print(model_key_now, r_now, model_key_now_2, r_now_2, all_corr_matrix[i, j])

    return all_corr_matrix, all_model_list
