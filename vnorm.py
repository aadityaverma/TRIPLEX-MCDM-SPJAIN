import numpy as np


def vector(x_matrix, is_benefit_x):
    """
    Return the normalized version of the provided matrix using the Vector
    Normalization method.
    """
    # Perform sanity checks
    x_matrix = np.array(x_matrix, dtype=np.float64)
    # Construct the normalized matrix
    z_matrix = np.zeros(x_matrix.shape, dtype=np.float64)
    for j in range(x_matrix.shape[1]):
        denominator = np.sqrt(np.sum(x_matrix[:, j] ** 2))
        if denominator == 0.0:
            raise ValueError(
                "The square root of a criterion's sum of squared values must "
                + "not be equal to zero in order to apply the Vector "
                + "normalization method",
            )
        z_matrix[:, j] = x_matrix[:, j] / denominator

    # The criteria have not been transformed into benefit or cost criteria
    is_benefit_z = is_benefit_x.copy()

    return z_matrix, is_benefit_z