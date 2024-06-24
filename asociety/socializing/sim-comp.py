def compute_friendship_potential(A, B, alpha=0.5, beta=0.5, threshold=2):
    def similarity_score(A_i, B_i):
        return 1 - abs(A_i - B_i)

    def complementarity_score(A_i, B_i, threshold):
        return 1 if abs(A_i - B_i) >= threshold else 0

    similarities = [similarity_score(A[i], B[i]) for i in range(5)]
    complementarities = [complementarity_score(A[i], B[i], threshold) for i in range(5)]

    S_total = sum(similarities) / 5
    C_total = sum(complementarities) / 5

    F = alpha * S_total + beta * C_total

    return F

# Example usage:
A = [3, 4, 2, 5, 2]  # Scores for Individual A
B = [3, 4, 2, 5, 2]  # Scores for Individual B

friendship_potential = compute_friendship_potential(A, B)
print(f"Friendship Potential Score: {friendship_potential}")
