
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	error=(y_true-y_pred)
	SS_res=((error**2)).sum()
	SS_total=((y_true-y_true.mean())**2).sum()
	sq_r=1-SS_res/SS_total
	return sq_r
