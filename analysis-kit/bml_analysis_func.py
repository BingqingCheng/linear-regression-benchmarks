"""
for processing data
"""

import numpy as np

from asaplib.fit.getscore import get_score
from asaplib.fit import LC_SCOREBOARD

def model_elementwise_error(model_now):
    
    n_repeats = model_now['n_repeats']
    
    # some options to select certain data points
    y_train = model_now['train'][model_now['train'][:,-1]==1]
    y_test = model_now['test'][model_now['test'][:,-1]==0]
    y_all = np.concatenate([y_test,y_train])
    y_sorted = y_all[np.argsort(y_all[:, 0])]
    
    # the avg value of the y from all replicas
    y_avg = np.asmatrix([np.mean(v) for v in y_sorted[:] ] )
    # print(np.shape(y_avg))
    
    # this records the prediction error y_true-y_pred for each data point using each fit
    y_error = np.asmatrix([ v[2]-v[1] for v in y_sorted]).reshape((-1,n_repeats))
    # records the MSE, MAE, and the standard deviation of error
    y_e_analysis = np.asmatrix([ [np.mean(v), np.mean(np.abs(v)), np.std(v)] for v in y_error[:] ] )
    # y, y_MSE, y_MAE, y_SD
    return np.asarray(np.squeeze(y_avg)).T, np.asarray(y_e_analysis[:,0]), \
           np.asarray(y_e_analysis[:,1]), np.asarray(y_e_analysis[:,2])

def model_error_correlation(model_1, model_2, compare='MAE', metric='CORR'):

    
    y_avg, error_mse, error_mae, error_std = model_elementwise_error(model_1)
    y_avg_2, error_mse_2, error_mae_2, error_std_2 = model_elementwise_error(model_2)
        
    if compare == 'y':
        return get_score(y_avg, y_avg_2)[metric]
    elif compare == 'MAE':
        return get_score(error_mae, error_mae_2)[metric]
    elif compare == 'MSE':
        return get_score(error_mse, error_mse_2)[metric]
    elif compare == 'STD':
        return get_score(error_std, error_std_2)[metric]
    else:
        raise ValueError("don't know what to compare")


def model_correlation_matrix(by_model, key_now, compare='MSE', metric='CORR', verbose=True):

    correlation_matrix = np.ones((len(by_model.keys()),len(by_model.keys())))
    model_list = []

    for i, model_key_now in enumerate(by_model.keys()):
        model_list.append(model_key_now)

        for j, model_key_now_2 in enumerate(by_model.keys()):
            if i > j:
                model_now = by_model[model_key_now][key_now]
                model_now_2 = by_model[model_key_now_2][key_now]

                correlation_matrix[i, j] = correlation_matrix[j, i] = model_error_correlation(model_now, model_now_2, compare, metric)
                if verbose: print(model_key_now, model_key_now_2, correlation_matrix[i, j])

    return correlation_matrix, model_list

def all_model_correlation_matrix(by_model, key_now_list=[], compare='MSE', metric='CORR', verbose=True):

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
                             model_error_correlation(model_now, model_now_2, compare=compare, metric=metric)
                    if verbose: print(model_key_now, r_now, model_key_now_2, r_now_2, all_corr_matrix[i, j])

    return all_corr_matrix, all_model_list
