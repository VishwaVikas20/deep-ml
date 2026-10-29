import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code 
	mean=np.mean(data,axis=0)
	std=np.std(data,axis=0)
	minimum=data.min(axis=0)
	maximum=data.max(axis=0)
	standardized_data=(data-mean)/(std)
	normalized_data=(data-minimum)/(maximum-minimum)
	return standardized_data.tolist(), normalized_data.tolist()