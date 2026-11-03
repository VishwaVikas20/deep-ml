import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    batch_X=X[batch_indices]
    batch_y=y[batch_indices]
    m,n=batch_X.shape
    y_hat=batch_X@weights + bias
    grad_w=-2*batch_X.T@(batch_y-y_hat)/m
    grad_b=-2*(batch_y-y_hat).sum()/m
    bias=bias-lr*(grad_b)
    weights=weights-lr*grad_w
    return np.append(weights, bias)
