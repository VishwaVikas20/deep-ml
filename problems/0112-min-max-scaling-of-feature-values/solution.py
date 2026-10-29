def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    max_v=float("-inf")
    min_v=float("inf")
    for i in x:
        if i>max_v:
            max_v=i
        if i<min_v:
            min_v=i
    d=max_v-min_v
    for i in range(len(x)):
        x[i]=(x[i]-min_v)/d
    return x