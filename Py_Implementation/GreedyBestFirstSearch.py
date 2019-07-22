import queue
import math

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)

class GBFSNode(object):
    def __init__(self, parent=None, coordinates=None, dist=0, heuristic=0):
        self.parent=parent
        self.coordinates=coordinates
        self.dist=dist
        self.heuristic=heuristic

    def __eq__(self, other):
        return (self.heuristic == other.heuristic)

    def __ne__(self, other):
        return (self.heuristic != other.heuristic)

    def __lt__(self, other):
        return (self.heuristic < other.heuristic)

    def __le__(self, other):
        return (self.heuristic <= other.heuristic)

    def __gt__(self, other):
        return (self.heuristic > other.heuristic)

    def __ge__(self, other):
        return (self.heuristic >= other.heuristic)

    def __repr__(self):
        return "%s, (%s,%s)" % (self.heuristic, self.coordinates.x, self.coordinates.y)

def isSafe(x, y, nrow, ncol):
    if x >=0 and x < nrow and y>=0 and y < ncol:
        return True
    return False

def heuristic(currentNodeCoordinates, exitNodeCoordinates):
    #Using Euclidean Distance as a heuristic function
    return math.sqrt(((currentNodeCoordinates.x- exitNodeCoordinates.x)**2) + ((currentNodeCoordinates.y - exitNodeCoordinates.y)**2))

#adjacent squares, representing movements left, right, up and down
rowNums=[0,-1,0,1]
colNums=[-1,0,1,0]


def GBFS(maze, src, dest):

    maxQueueSize = 0
    expandedNodeCnt = 0

    nrow = len(maze)
    ncol = len(maze[0])

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
    srcHeuristic = heuristic(src, dest)
    srcNode = GBFSNode(None, src, 0, srcHeuristic)

    q.put(srcNode)

    while not q.empty():
        if q.qsize() > maxQueueSize:
            maxQueueSize = q.qsize()

        current = q.get()
        # print("Heuristic: ", current.heuristic, " cum-dist: ", current.dist, " (x,y): (", current.coordinates.x, ",", current.coordinates.y, ")")
        point = current.coordinates

        #If coordinates of cuurent node are same as destination, the goal has been reached
        if point.x == dest.x and point.y == dest.y:
            # print("current distance cost", current.dist)
            path = []
            cost = current.dist
            curnt = current
            while curnt is not None:
                tuple = (curnt.coordinates.x, curnt.coordinates.y)
                # print("new tuple:", tuple)
                path.append(tuple)
                curnt = curnt.parent
            # return (path[::-1], cost)  #Return reversed path
            return (path, cost, expandedNodeCnt, maxQueueSize)  #Return reversed path

        expandedNodeCnt += 1
        for i in range(0,4):
            row = point.x + rowNums[i]
            col = point.y + colNums[i]

            #add the adjacent node to queue if it is a valid coordinate, it is not an obstacle and has not been visited yet
            if isSafe(row, col, nrow, ncol) and maze[row][col] is not 0 and visited[row][col] is False:
                visited[row][col] = True
                newPoint = Point(row, col)
                newPointHeuristic = heuristic(newPoint, dest)
                newGBFSNode = GBFSNode(current, newPoint, current.dist + 1, newPointHeuristic)
                q.put(newGBFSNode)
    #if path is not found, then return -1
    # return -1

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

    (path, cost, expndCount, maxQueueSize) = GBFS(grid, srcObject, destObject)

    print("Path => ", path[::-1])
    print("Cost: ", cost)
    print("Total Expanded Nodes Count: ", expndCount)
    print("Maximum no.of nodes kept in memory: ", maxQueueSize)


