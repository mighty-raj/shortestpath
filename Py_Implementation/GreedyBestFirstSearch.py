import queue
import math

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Node():
    def __init__(self, coordinates, dist):
        self.coordinates = coordinates
        self.dist = dist

class PQNode(object):
    def __init__(self, priority, node):
        self.priority = priority
        self.node = node

    def __eq__(self, other):
        return (self.priority == other.priority)

    def __ne__(self, other):
        return (self.priority != other.priority)

    def __lt__(self, other):
        return (self.priority < other.priority)

    def __le__(self, other):
        return (self.priority <= other.priority)

    def __gt__(self, other):
        return (self.priority > other.priority)

    def __ge__(self, other):
        return (self.priority >= other.priority)

    def __repr__(self):
        return "%s, (%s,%s)" % (self.priority, self.node.coordinates.x, self.node.coordinates.y)


def isSafe(x, y, nrow, ncol):
    if x >=0 and x < nrow and y>=0 and y < ncol:
        return True
    return False

def heuristic(currentNodeCoordinates, exitNodeCoordinates):
    return math.sqrt(((currentNodeCoordinates.x- exitNodeCoordinates.x)**2) + ((currentNodeCoordinates.y - exitNodeCoordinates.y)**2))

#adjacent squares, representing movements left, right, up and down
rowNums=[0,-1,0,1]
colNums=[-1,0,1,0]


def BFSPQ(maze, src, dest, nrow, ncol):
    visited = []

    #if src or destination is an obstacle, we cannot have a path
    if maze[src.x][src.y] is not 1 or maze[dest.x][dest.y] is not 1:
        return -1

    for i in range(len(maze)):
        visited.append([False] * len(maze[i]))

    #mark the source as visisted
    visited[src.x][src.y] = True

    q=queue.PriorityQueue(maxsize = (nrow * ncol))

    #Add source to queue
    srcNode = Node(src,0)
    endNode = Node(dest, 0)
    q.put(PQNode(heuristic(srcNode.coordinates, endNode.coordinates), srcNode))

    while not q.empty():
        current = q.get()
        print("Heuristic: ", current.priority, " cum-dist: ", current.node.dist, " (x,y): (", current.node.coordinates.x, ",", current.node.coordinates.y, ")")
        point = current.node.coordinates
        #             print("value in point ==> (", point.x,",", point.y,") ==> cum-dist:", current.node.dist)

        #If coordinates of cuurent node are same as destination, the goal has been reached
        if point.x == dest.x and point.y == dest.y:
            print("current distance cost", current.node.dist)
            return current.node.dist


        for i in range(0,4):
            row = point.x + rowNums[i]
            col = point.y + colNums[i]

            #add the adjacent node to queue if it is a valid coordinate, it is not an obstacle and has not been visited yet
            if isSafe(row, col, nrow, ncol) and maze[row][col] is not 0 and visited[row][col] is False:
                visited[row][col] = True
                newNode = Node(Point(row, col), current.node.dist + 1)
                newNodeHeuristic = heuristic(newNode.coordinates, endNode.coordinates)
                #                     print("New Node Heuristic: ", newNodeHeuristic, ", point: (", row, ",", col, ")")
                newPQNode = PQNode(newNodeHeuristic, newNode)
                q.put(newPQNode)
    #if path is not found, then return -1
    return -1

def shortestPathInMaze(maze, src, dest):
    nrow = len(maze)
    ncol = len(maze[0])

    val = BFSPQ(maze, src, dest, nrow, ncol)

    return val

if __name__ == '__main__':
    grid=[[1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0,0,0,1,1],
          [1,1,0,0,1,1,1,1,0,1,1],
          [1,1,0,0,1,1,1,1,0,1,1],
          [1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1],
          [1,1,0,0,0,0,0,0,0,1,1],
          [1,1,1,1,1,1,1,1,1,1,1]
          ]

    #Computation call for Best First Search
    src = [0,2]
    dest = [5,10]

    srcObject = Point(src[0], src[1])
    destObject = Point(dest[0], dest[1])

    val = shortestPathInMaze(grid, srcObject, destObject)

    if val == -1:
        print("Path doesn't exist")
    else:
        print("Length of shortest path is: ", val)

