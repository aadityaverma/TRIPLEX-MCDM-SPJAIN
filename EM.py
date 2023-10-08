import numpy as np

def em(z_matrix):
    """
    Returns the weight vector of the provided decision matrix using the Entropy
    Measure method.
    """
    # Perform sanity checks
    z_matrix = np.array(z_matrix, dtype=np.float64)

    # Compute the normalization constant
    k_constant = 1.0 / np.log(z_matrix.shape[0])

    # Compute the entropy of each criterion
    e_vector = np.zeros(z_matrix.shape[1], dtype=np.float64)
    for j in range(z_matrix.shape[1]):
        tmp_sum = 0.0
        for i in range(z_matrix.shape[0]):
            if z_matrix[i, j] > 0.0:
                tmp_sum += z_matrix[i, j] * np.log(z_matrix[i, j])
        e_vector[j] = -k_constant * tmp_sum

    # The importance of each criterion corresponds to
    # its normalized degree of divergence
    return (1.0 - e_vector) / np.sum(1.0 - e_vector)