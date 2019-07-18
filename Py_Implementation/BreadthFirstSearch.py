import queue

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


# Below lists are to find adjacent squares from a given position, that covers the movements, left, right, up and down.
rowNums = [0, -1, 0, 1]
colNums = [-1, 0, 1, 0]

# validates if the cell is a valid cell to consider for next movement ...
def isSafe(x, y, nrow, ncol):
    if x >= 0 and x < nrow and y >= 0 and y < ncol:
        return True
    return False

def BFS(maze, src, dest, nrow, ncol):
    visited = []

    # if src or destination is an obstacle, we cannot have a path
    if maze[src.x][src.y] is not 1 or maze[dest.x][dest.y] is not 1:
        return -1

    for i in range(len(maze)):
        visited.append([False] * len(maze[i]))

    # mark the source as visisted
    visited[src.x][src.y] = True

    q = queue.Queue(maxsize=(nrow * ncol))

    # Add source to queue
    q.put(Node(src, 0))

    while not q.empty():
        current = q.get()
        point = current.coordinates
        print("value in point ==> (", point.x, ",", point.y, ") ==> cum-dist:", current.dist)

        # If coordinates of cuurent node are same as destination, the goal has been reached
        if point.x == dest.x and point.y == dest.y:
            print("current distance cost", current.dist)
            return current.dist

        for i in range(0, 4):
            row = point.x + rowNums[i]
            col = point.y + colNums[i]

            # add the adjacent node to queue if it is a valid coordinate, it is not an obstacle and has not been visited yet
            if isSafe(row, col, nrow, ncol) and maze[row][col] is not 0 and visited[row][col] is False:
                visited[row][col] = True
                newNode = Node(Point(row, col), current.dist + 1)
                q.put(newNode)
    # if path is not found, then return -1
    return -1


# Function call to BFS algo to find shortest path
def shortestPathInMaze(maze, src, dest):
    nrow = len(maze)
    ncol = len(maze[0])

    val = BFS(maze, src, dest, nrow, ncol)

    return val


if __name__ == '__main__':
    inputMaze = [[1, 0, 0, 0],
                 [1, 1, 0, 1],
                 [0, 1, 0, 0],
                 [1, 1, 1, 1]
                 ]
    src = [0, 0]
    dest = [3, 3]

    srcObject = Point(src[0], src[1])
    destObject = Point(dest[0], dest[1])

    val = shortestPathInMaze(inputMaze, srcObject, destObject)

    if val == -1:
        print("Path doesn't exist")
    else:
        print("Length of shortest path is: ", val)
