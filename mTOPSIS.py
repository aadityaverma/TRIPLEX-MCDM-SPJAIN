import numpy as np
def mtopsis(z_matrix, w_vector, is_benefit_z):
    """
    Return the Modified Technique for Order Preference by Similarity to Ideal
    Solution scores of the provided decision matrix with the provided weight
    vector.
    """
    # Perform sanity checks
    z_matrix = np.array(z_matrix, dtype=np.float64)
    w_vector = np.array(w_vector, dtype=np.float64)

    # mTOPSIS scores should always be sorted in descending order
    desc_order = True

    # Derive the positive and negative ideal solutions
    pos_ideal_sol = np.zeros(z_matrix.shape[1], dtype=np.float64)
    neg_ideal_sol = np.zeros(z_matrix.shape[1], dtype=np.float64)
    for j in range(z_matrix.shape[1]):
        if is_benefit_z[j]:
            pos_ideal_sol[j] = np.amax(z_matrix[:, j])
            neg_ideal_sol[j] = np.amin(z_matrix[:, j])
        else:
            pos_ideal_sol[j] = np.amin(z_matrix[:, j])
            neg_ideal_sol[j] = np.amax(z_matrix[:, j])

    # Compute the score of each alternative
    s_vector = np.zeros(z_matrix.shape[0], dtype=np.float64)
    for i in range(z_matrix.shape[0]):
        pos_ideal_dist = 0.0
        neg_ideal_dist = 0.0
        for j in range(z_matrix.shape[1]):
            pos_ideal_dist += (
                w_vector[j] * (pos_ideal_sol[j] - z_matrix[i, j])**2
            )
            neg_ideal_dist += (
                w_vector[j] * (z_matrix[i, j] - neg_ideal_sol[j])**2
            )
        pos_ideal_dist = np.sqrt(pos_ideal_dist)
        neg_ideal_dist = np.sqrt(neg_ideal_dist)
        denominator = neg_ideal_dist + pos_ideal_dist
        if denominator == 0.0:
            raise ValueError(
                "The sum of the negative ideal distance and the positive "
                + "ideal distance must not be equal to zero in order to use "
                + "the mTOPSIS method",
            )
        s_vector[i] = neg_ideal_dist / denominator

    return s_vector, desc_order