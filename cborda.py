import numpy as np


def borda_count(matrix):
    # Check if the input matrix is empty
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []

    num_candidates = len(matrix)
    num_voters = len(matrix[0])

    # Initialize scores for each candidate
    scores = [0] * num_candidates

    # Check if the input matrix contains ordinal or cardinal values
    if isinstance(matrix[0][0], int):
        # Cardinal values: Calculate the Borda Count
        for voter_rankings in matrix:
            for candidate, score in enumerate(voter_rankings):
                scores[candidate] += score

    elif isinstance(matrix[0][0], list):
        # Ordinal values: Calculate the Borda Count based on rankings
        for voter_rankings in matrix:
            for rank, candidate in enumerate(voter_rankings):
                for c in candidate:
                    scores[c] += num_candidates - rank - 1

    # Create a list of tuples containing candidate indices and scores
    candidate_scores = [(i, score) for i, score in enumerate(scores)]

    # Sort candidates by score in descending order
    candidate_scores.sort(key=lambda x: x[1], reverse=True)

    # Determine the ranks
    rank = 1
    last_score = None
    ranked_candidates = []
    for candidate, score in candidate_scores:
        if score == last_score:
            ranked_candidates[-1].append(candidate)
        else:
            ranked_candidates.append([candidate])
            last_score = score
        rank += 1

    return ranked_candidates


# Example usage:
# matrix = [
#     [1, 2, 3],
#     [2, 3, 1],
#     [3, 1, 2]
# ]
#
# result = borda_count(matrix)
# for i, group in enumerate(result):
#     print(f"Rank {i + 1}: {', '.join([str(candidate) for candidate in group])}")
