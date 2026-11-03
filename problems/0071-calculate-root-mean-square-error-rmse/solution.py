import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	e=y_true-y_pred
	MSE=(e**2).mean()
	rmse_res=np.sqrt(MSE)
	return np.round(rmse_res,3)
