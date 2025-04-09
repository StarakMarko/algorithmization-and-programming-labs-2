matrix = [
    ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
    ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
    ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
    ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
    ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
    ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
    ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
    ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
    ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
    ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
]


def flood_fill(matrix, x, y, color):
    main_color = matrix[x][y]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(matrix, x, y, color):
        matrix[x][y] = color
        nonlocal visited
        visited[x][y] = True
        nonlocal main_color
        if x - 1 >= 0 and matrix[x - 1][y] == main_color and not visited[x - 1][y]:
            dfs(matrix, x - 1, y, color)
        if y - 1 >= 0 and matrix[x][y - 1] == main_color and not visited[x][y - 1]:
            dfs(matrix, x, y - 1, color)
        if (
            x + 1 < len(matrix)
            and matrix[x + 1][y] == main_color
            and not visited[x + 1][y]
        ):
            dfs(matrix, x + 1, y, color)
        if (
            y + 1 < len(matrix[0])
            and matrix[x][y + 1] == main_color
            and not visited[x][y + 1]
        ):
            dfs(matrix, x, y + 1, color)

    dfs(matrix, x, y, color)
    for i in matrix:
        print(i)
    return matrix


flood_fill(matrix, 3, 9, "C")
