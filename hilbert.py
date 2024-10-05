import numpy as np

def hilbert_matrix(n):
    """Generate an n x n Hilbert matrix."""
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1 / (i + j + 1)
    return H

# Generate a 10x10 Hilbert matrix
n = 10
H = hilbert_matrix(n)

# Print the matrix
print("10x10 Hilbert Matrix:")
print(H)