def lcslen(x, y):
    c = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            if xi == yj:
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c
