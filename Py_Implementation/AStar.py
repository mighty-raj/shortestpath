import math

class Node():
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    #Returns a list of tuples as a path from the given start to the given end in the given maze

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    print("start node: ", start_node.position)

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        print("open_list: ")
        for p in open_list:
            print(p.position)

        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            print("index: ", index)
            print("item: ", item.position)
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #pop current off open list and add to closed list
        open_list.pop(current_index)
        print("pop from open_list: ")
        for p in open_list:
            print(p.position)

        closed_list.append(current_node)
        print("closed_list: ")
        for p in closed_list:
            print(p.position)

        #Found the goal
        if current_node == end_node:
            print("End node found, but something might have went wrong here after")
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Return reversed path\


        #Generate Children
        children = []
        for new_position in [(0,-1), (0,1),(-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]: #Adjacent Squares
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            #make sure walkable terrain
            if maze[node_position[0]][node_position[1]] !=1:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)
            print("children list: ")
            for p in children: print(p.position)

        # Loop through children
        for child in children:
            print("iterating children")
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = math.sqrt(((child.position[0]- end_node.position[0])**2) + ((child.position[1] - end_node.position[1])**2))
            child.f = child.g + child.h

            print("child: ", child.position, " g: ", child.g, " h: ", child.h, " f: ", child.f)

            #child is read in open_list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)
            print("open_list:")
            for p in open_list: print(p.position)


if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    src=(0,0)
    dest=(7,6)

    path = astar(maze, src, dest)

    print(path)