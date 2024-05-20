# Sweet, J.N., (2003)

import numpy as np
vec1 = np.array([1, 3, 5, 7])
vec2 = np.array([2, 4, 6, 8])

def ssv (daed, dicorr):
    '''
    Spectral Similarity Value

    :param daed: dimensionally adjusted Euclidian distance
    :param dicorr: directional correlation
    :result: spectral similarity value
    '''
    return(daed*daed+dicorr*dicorr)

def daed(vec1, vec2):
    '''
    Dimensionally adjusted Euclidian distance

    :param vec1: first input vector
    :param vec2: second input vector
    :result: dimensionally adjusted Euclidian distance
    '''
    diff_mat = vec2[:, None] - vec1[None, :]
    diff_mat_sqrd = diff_mat*diff_mat
    return(np.sum(diff_mat_sqrd)/vec1.shape[0])

def dicorr(vec1, vec2):
    '''
    Directional correlation

    :param vec1: first input vector
    :param vec2: second input vector
    :result: directional correlation
    '''
    corr_coef = np.corrcoef(vec1, vec2)[0, 1]
    if (corr_coef > 0):
        return(1.0-corr_coef*corr_coef)
    if (corr_coef <= 0):
        return(0)


