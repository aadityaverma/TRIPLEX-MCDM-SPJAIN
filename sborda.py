def borda_score(matrix):
    num_candidates = len(matrix)
    num_columns = len(matrix[0])

    # Check if the matrix contains ordinal rankings or cardinal scores
    is_ordinal = all(isinstance(matrix[i][j], int) for i in range(num_candidates) for j in range(num_columns))

    scores = {}  # Dictionary to store Borda scores for each candidate

    for j in range(num_columns):
        # Create a list of tuples where each tuple contains the candidate index and their ranking or score
        if is_ordinal:
            ranked_candidates = [(i, matrix[i][j]) for i in range(num_candidates)]
        else:
            ranked_candidates = [(i, num_columns - matrix[i][j]) for i in range(num_candidates)]

        # Sort candidates based on their ranking or score
        ranked_candidates.sort(key=lambda x: x[1])

        # Calculate Borda scores for each candidate
        for i, (_, ranking_or_score) in enumerate(ranked_candidates):
            if i not in scores:
                scores[i] = 0
            scores[i] += ranking_or_score

    # Sort candidates based on their Borda scores
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted list of candidates and their Borda scores
    result = [(candidate_index, score) for candidate_index, score in sorted_scores]
    return result

# Example usage:
# Define a matrix with rankings or scores (can be ordinal or cardinal)
# matrix = [
#     [1, 2, 3],
#     [3, 1, 2],
#     [2, 3, 1]
# ]
#
# borda_scores = calculate_borda_score(matrix)
# for candidate_index, score in borda_scores:
#     print(f"Candidate {candidate_index + 1}: Borda Score = {score}")
