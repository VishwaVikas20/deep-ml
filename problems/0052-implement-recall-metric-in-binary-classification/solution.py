import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    TP=0
    FN=0
    for idx,v in enumerate(y_true):
        if v==1:
            if y_pred[idx]==1:
                TP+=1
            if y_pred[idx]==0:
                FN+=1
    recall=TP/(TP+FN)
    if (TP+FN)==0:
        return 0.
    return recall
