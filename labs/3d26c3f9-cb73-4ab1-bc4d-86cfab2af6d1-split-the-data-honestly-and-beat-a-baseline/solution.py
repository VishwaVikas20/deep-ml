import numpy as np


def split_and_baseline(X, y, train_frac, val_frac, test_frac, seed):
    """Split rows into train/val/test folds, fit something on the training fold, predict the test fold.

    Returns
    -------
    test_predictions : np.ndarray, shape (len(test_idx),)
    train_idx, val_idx, test_idx : 1-D integer arrays forming a partition of range(len(y))
    """
    np.random.seed(seed)
    arr=np.arange(len(X))
    np.random.shuffle(arr)
    X_train_idx=arr[:int(train_frac*len(X))]
    X_test_idx=arr[int(train_frac*len(X)):int((train_frac+test_frac)*len(X))]
    X_val_idx=arr[int((train_frac+test_frac)*len(X)):]
    return y[X_test_idx],X_train_idx,X_val_idx,X_test_idx

