from collections import defaultdict
import numpy as np

def nborda_count(matrix):
    # Check if the input matrix contains numeric values, indicating cardinal preferences.
    is_cardinal = all(isinstance(val, (int, float)) for val in matrix[0])

    # Calculate the number of candidates and ranks/scores.
    num_candidates = len(matrix)
    num_ranks = len(matrix[0])

    # Create a dictionary to store the scores for each candidate.
    scores = defaultdict(float)

    # Calculate Borda scores for each candidate.
    for candidate_idx in range(num_candidates):
        for rank_idx in range(num_ranks):
            if is_cardinal:
                # Cardinal preferences: Sum the scores.
                scores[candidate_idx] += matrix[candidate_idx][rank_idx]
            else:
                # Ordinal preferences: Assign scores based on ranks.
                scores[candidate_idx] += (num_ranks - rank_idx - 1)

    # Convert the dictionary to a list of tuples for sorting.
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

    # Calculate the rank for each candidate.
    rank = 1
    result = []
    last_score = None
    for candidate_idx, candidate_score in sorted_scores:
        if candidate_score == last_score:
            result[-1].append(candidate_idx)
        else:
            result.append([candidate_idx])
            last_score = candidate_score
            rank += 1

    return result

# Example usage:
# Define your preference matrix as a list of lists (matrix).
# preference_matrix = [
#     [3, 2, 1],  # Candidate 0's preferences (cardinal or ordinal)
#     [2, 3, 1],  # Candidate 1's preferences (cardinal or ordinal)
#     [1, 2, 3]   # Candidate 2's preferences (cardinal or ordinal)
# ]
# 
# # Calculate Nauru Borda Count
# result = nborda_count(preference_matrix)
# 
# # Print the result (ranked candidates)
# for rank, candidates in enumerate(result):
#     print(f"Rank {rank + 1}: Candidates {candidates}")
