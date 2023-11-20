import numpy as np

test = np.array([[1.0, 1, -1, 0], [1, 0, 0, -1], [-1, 1, -1, 2]])

clone = test.copy()

def reduce(matrix):
    n = len(matrix)

    m = len(matrix[0])

    id = np.identity(n, dtype=float)

    row = 0

    for j in range(m):

        zeroInd = -1

        for i in range(row, n):
            if matrix[i][j] != 0:
                zeroInd = i
                break

        if zeroInd != -1:
            matrix[[row, zeroInd]] = matrix[[zeroInd, row]]  # Bring row with leftmost nonzero entry up to top
            id[[row, zeroInd]] = id[[zeroInd, row]]

            fact = matrix[row][j]
            matrix[row] /= fact  # Make matrix[row][j] coeff equal to 1
            id[row] /= fact

            for r in range(n):
                if r != row and matrix[r][j] != 0:
                    p = matrix[r][j]
                    matrix[r] -= p * matrix[row]  # Row ops to wipe out elements in same column
                    id[r] -= p * id[row]

            row += 1

    print("RREF")
    print(matrix)

    if not np.any(matrix[-1]):
        print("no Inverse")
    else:
        print("Inverse: ")
        print(id)

    return id

inv = reduce(test)


