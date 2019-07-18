# Objects of this class would be used to define coordinates in the matrix
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Objects of this class would be used to define every entry in the matrix including its coordinates and distance from source
class Node():
    def __init__(self, coordinates, dist):
        self.coordinates = coordinates
        self.dist = dist

# validates if the cell is a valid cell to consider for next movement ...
def isSafe(row, col, nrow, ncol):
    if row >=0 and row < nrow and col >=0 and col < ncol:
        return True
    return False


# Below lists are to find adjacent squares from a given position, that covers the movements, left, right, up and down.
rowNums = [0,-1,0,1]
colNums = [-1,0,1,0]


def DFS(maze, src, dest, nrow, ncol):

    visited = []

    if maze[src.x][src.y] is not 1 or maze[dest.x][dest.y] is not 1:
        return -1

    for i in range(len(maze)):
        visited.append([False] * len(maze[i]))

    visited[src.x][src.y] = True

    stack = []*(nrow*ncol)

    stack.append(Node(src,0))

    while not len(stack) == 0:
        current = stack.pop()

        point = current.coordinates
        print("value in point ==> (", point.x,",", point.y,") ==> cum-dist:", current.dist)

        if point.x == dest.x and point.y == dest.y:
            return current.dist

        for i in range(0, 4):
            row = point.x + rowNums[i]
            col = point.y + colNums[i]

            if isSafe(row, col, nrow, ncol) and maze[row][col] is not 0 and visited[row][col] is not True:
                visited[row][col] = True
                newNode = Node(Point(row, col), current.dist + 1)
                stack.append(newNode)

    #if no path found return -1
    return -1

# Function call to DFS algo to find shortest path
def shortestPathInMaze(maze, src, dest):
    nrow = len(maze)
    ncol = len(maze[0])

    val = DFS(maze, src, dest, nrow, ncol)

    return val

if __name__ == '__main__':
    inputMaze = [[1,0,0,0],
                 [1,1,0,1],
                 [0,1,0,0],
                 [1,1,1,1]
                 ]
    src = [0,0]
    dest=[3,3]

    srcObject = Point(src[0], src[1])
    destObject = Point(dest[0], dest[1])

    val = shortestPathInMaze(inputMaze, srcObject, destObject)

    if val == -1:
        print("path not found")
    else:
        print("Length of the shortest path is: ", val)
