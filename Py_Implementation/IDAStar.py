import math
import sys

nrows = [0,0,1,-1]
ncols = [1,-1,0,0]

def heuristic(src,dest):
    return abs(src.position[0] - dest.position[0])+abs(src.position[1] - dest.position[1])
    #return math.sqrt(pow(src.position[0] - dest.position[0],2) + pow(src.position[1] - dest.position[1],2))

def is_goal(node,dest):
    return node.position == dest.position

class Node:
    def __init__(self,position):
        self.position = position

def search(maze, path, g, dest, bound,visited):



    node = path[len(path)-1]

    f = g+heuristic(node,dest)

    if f > bound:
        return f

    if is_goal(node,dest):
        return -1
    min = sys.maxsize

    for nextnode in nextNodes(maze,node):
        if visited[nextnode.position[0]][nextnode.position[1]] == False:
            path.append(nextnode)
            visited[nextnode.position[0]][nextnode.position[1]] = True
            temp = search(maze,path,heuristic(node,nextnode),dest,bound,visited)
            if temp == -1:
                return -1
            if temp<min:
                min = temp

            path.pop()
    return min


def nextNodes(maze,src):

    nextNodeList = []
    for i in range(0,len(nrows)):
        newRowPosition = src.position[0]+nrows[i]
        newColPosition = src.position[1]+ncols[i]
        new_node_position = (newRowPosition, newColPosition)
        if new_node_position[0]<len(maze) and new_node_position[1]<len(maze[0]) and new_node_position[0] >= 0 and new_node_position[1] >= 0 and maze[new_node_position[0]][new_node_position[1]] == 1:
            nextNodeList.append(Node(new_node_position))
    return nextNodeList

def idaStar(maze,src,dest):
    bound = heuristic(src,dest)
    g = heuristic(src,src)
    path = [src]

    while 1 :

        visited = []

        for i in range(0, len(maze)):
            visited.append([False] * len(maze[i]))

        visited[src.position[0]][src.position[1]] = True

        temp = search(maze,path,g,dest,bound,visited)
        if temp == -1:
            return (path,bound)
        if temp> heuristic(src,dest):
            return ()
        bound = temp


def is_not_in(node,nodeList):
    return node.position not in nodeList


if __name__ == '__main__':
    src = (0, 2)
    dest = (5, 10)

    srcPoint = Node(src)
    destPoint = Node(dest)
    inputMaze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
                 [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    try:
        (path,bound) = idaStar(inputMaze,srcPoint,destPoint)
        for i in path:
            print(i.position)
        print(bound)
    except:
        print('path not found')

