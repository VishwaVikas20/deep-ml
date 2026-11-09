import numpy as np
def precision(y_true, y_pred):
	# Your code here
	TP=0
	for idx,t in enumerate(y_true):
		if t==1 and y_pred[idx]==1:
			TP+=1
	FP=y_pred.sum()-TP
	Precision=TP/(TP+FP)
	if TP+FP==0:
		return 0.
	if Precision:
		return Precision