
import numpy as np

def vikor(decision_matrix, weights=None, benefit_criteria=None):
    if weights is None:
        weights = [1] * len(decision_matrix[0])
    if benefit_criteria is None:
        benefit_criteria = [True] * len(decision_matrix[0])

    # Step 1: Normalize the decision matrix
    decision_matrix = np.array(decision_matrix)
    norm_decision_matrix = decision_matrix / decision_matrix.sum(axis=0)

    # Step 2: Determine the weighted normalized decision matrix
    weighted_norm_decision_matrix = norm_decision_matrix * weights

    # Step 3: Determine the ideal and negative-ideal solutions
    if benefit_criteria:
        ideal_solution = np.max(weighted_norm_decision_matrix, axis=0)
        negative_ideal_solution = np.min(weighted_norm_decision_matrix, axis=0)
    else:
        ideal_solution = np.min(weighted_norm_decision_matrix, axis=0)
        negative_ideal_solution = np.max(weighted_norm_decision_matrix, axis=0)

    # Step 4: Calculate the separation measures, Si and Ri
    Si = np.sum(np.abs(weighted_norm_decision_matrix - ideal_solution), axis=1)
    Ri = np.max(np.abs(weighted_norm_decision_matrix - ideal_solution), axis=1)

    # Step 5: Calculate the closeness to the ideal solution, Qi
    Qi = 0.5 * Si + 0.5 * Ri

    return Qi

# Example usage:
# decision_matrix = [[7, 9, 9, 8], [8, 7, 8, 7], [9, 6, 8, 9], [6, 7, 8, 6]]
# weights = [0.4, 0.3, 0.1, 0.2]
# benefit_criteria = [True, True, True, True]
#
# print(vikor(decision_matrix, weights, benefit_criteria))
