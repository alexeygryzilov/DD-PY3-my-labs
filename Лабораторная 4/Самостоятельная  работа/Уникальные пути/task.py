def unique_paths(m: int, n: int) -> int:
    routes = [[0] * m for i in range(n)]

    for j in range(m):
        routes[0][j] = 1
    for i in range(1, n):
        routes[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            routes[i][j] = routes[i - 1][j] + routes[i][j - 1]
    for line in routes:
        print(line)

    return routes[-1][-1]


if __name__ == '__main__':
    print(unique_paths(3, 7))  # 28
