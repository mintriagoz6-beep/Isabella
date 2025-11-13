# ...existing code...
from typing import List, Tuple

Matrix2x2 = List[List[float]]

def add(A: Matrix2x2, B: Matrix2x2) -> Matrix2x2:
    return [[A[0][0] + B[0][0], A[0][1] + B[0][1]],
            [A[1][0] + B[1][0], A[1][1] + B[1][1]]]

def pretty(A: Matrix2x2) -> str:
    return f"[{A[0][0]:.4g}\t{A[0][1]:.4g}]\n[{A[1][0]:.4g}\t{A[1][1]:.4g}]"

if __name__ == "__main__":
    A: Matrix2x2 = [[1, 2], [3, 4]]
    B: Matrix2x2 = [[2, 0], [1, 2]]

    print("Matriz A:")
    print(pretty(A))
    print("\nMatriz B:")
    print(pretty(B))

    print("\nA + B =")
    print(pretty(add(A, B)))