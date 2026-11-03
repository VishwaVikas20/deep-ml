import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    n_samples=X.shape[0]
    for i in range(n_iter):
        idx=i%n_samples
        y_hat=np.dot(weights,X[idx])
        grad=-2*(y[idx]-y_hat)*X[idx]
        weights=weights-learning_rate*grad

    return weights
