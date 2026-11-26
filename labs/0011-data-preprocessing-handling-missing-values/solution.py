import numpy as np

def impute(X: np.ndarray) -> np.ndarray:
    '''
    Fill in missing values (NaN) in the input array.
    
    Args:
        X: Array with possible NaN values, shape (n_samples, n_features)
    
    Returns:
        X_clean: Array with no NaN values, same shape as X
    '''
    X_clean = X.copy()
    
    # TODO: Fill in NaN values
    mean_of_columns=np.nanmean(X_clean,axis=0)
    mean_of_columns=np.nan_to_num(mean_of_columns)
    nan_row,nan_col=np.where(np.isnan(X_clean))
    X_clean[nan_row,nan_col]=mean_of_columns[nan_col]
    
    return X_clean
