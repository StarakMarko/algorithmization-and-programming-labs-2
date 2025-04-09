# В1 Р3


def flood_fill(filename):
    file = open(filename, "r")
    height_width = file.readline().strip()
    x, y = file.readline().strip().split(",")
    x = int(x)
    y = int(y)
    color = file.readline().strip().strip("‘’'\"")

    matrix = []
    for line in file:
        if line.strip():
            cleaned = line.strip().strip("[],")
            row = [item.strip().strip("‘’'\"") for item in cleaned.split(",")]
            matrix.append(row)

    file.close()
    main_color = matrix[x][y]
    visited = []
    queue = [[x, y]]

    def neighbors(matrix, x, y, color):
        ind = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        neighbors_lst = []
        for x, y in ind:
            if (
                x >= 0
                and y >= 0
                and x < len(matrix)
                and y < len(matrix[0])
                and matrix[x][y] == color
            ):
                neighbors_lst.append([x, y])
        return neighbors_lst

    while len(queue) > 0:
        x, y = queue.pop(0)
        visited.append([x, y])
        matrix[x][y] = color
        for a, b in neighbors(matrix, x, y, main_color):
            if [a, b] not in visited:
                queue.append([a, b])
    file = open("output.txt", "w")
    for row in matrix:
        print(row)
        file.write(str(row) + "\n")
    file.close()

    return matrix


if __name__ == "__main__":
    flood_fill("input.txt")
