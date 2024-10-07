import numpy as np

def hilbert_matrix(n):
    """Generate an n x n Hilbert matrix."""
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H

# Example usage
n = 5
H = hilbert_matrix(n)
print("Hilbert Matrix of size", n)
print(H)