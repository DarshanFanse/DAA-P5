def LCS(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Initialize matrices
    cost = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[""] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill cost and direction matrices
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                cost[i][j] = cost[i - 1][j - 1] + 1
                b[i][j] = 'D'  # Diagonal (match)
            elif cost[i - 1][j] >= cost[i][j - 1]:
                cost[i][j] = cost[i - 1][j]
                b[i][j] = 'U'  # Up
            else:
                cost[i][j] = cost[i][j - 1]
                b[i][j] = 'S'  # Side (left)

    return cost, b


def Print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return ""
    if b[i][j] == 'D':
        return Print_LCS(b, X, i - 1, j - 1) + X[i - 1]
    elif b[i][j] == 'U':
        return Print_LCS(b, X, i - 1, j)
    else:
        return Print_LCS(b, X, i, j - 1)


if __name__ == "__main__":
    X = "AGCCCTAAGGGCTACCTAGCTT"
    Y = "GACAGCCTACAAGCGTTAGCTTG"

    cost, b = LCS(X, Y)
    lcs_seq = Print_LCS(b, X, len(X), len(Y))

    print("LCS length:", cost[len(X)][len(Y)])
    print("LCS sequence:", lcs_seq)
