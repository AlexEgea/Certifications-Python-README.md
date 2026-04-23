import numpy as np

def calculate(list):
    """
    Function that receives a list of 9 numbers and returns
    mean, variance, standard deviation, max, min and sum
    for rows, columns and the whole matrix.
    """

    # ---------------------------------------------------
    # STEP 1: Validate input
    # ---------------------------------------------------
    # Check if the list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # ---------------------------------------------------
    # STEP 2: Convert list to 3x3 matrix
    # ---------------------------------------------------
    # Reshape transforms the flat list into a 3x3 NumPy array
    matrix = np.array(list).reshape(3, 3)

    # Example:
    # Input: [0,1,2,3,4,5,6,7,8]
    # Matrix:
    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]]

    # ---------------------------------------------------
    # STEP 3: Perform calculations
    # ---------------------------------------------------
    # axis=0 → columns
    # axis=1 → rows
    # no axis → whole matrix (flattened)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # mean by columns
            matrix.mean(axis=1).tolist(),   # mean by rows
            matrix.mean().item()            # mean of all elements
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    # ---------------------------------------------------
    # STEP 4: Return result
    # ---------------------------------------------------
    return calculations