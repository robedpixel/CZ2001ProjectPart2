import snap
import numpy as np

graph = {
    'A': ['B', True],
    'B': ['D', 'E'],
    True: ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue
check = [False, False, True, False, False, False];
nodenum = [];


def snap_bfs(visited, graph: snap.PUNGraph, node: int, hospital_locations_list: list):
    # Create array of same size as number of nodes of graph
    numnodes = graph.GetNodes()
    hospitalarray = np.zeros((numnodes, 1), dtype=bool)
    # load array with values in hospital list
    for location in hospital_locations_list:
        hospitalarray[location] = True


    visited.append(node)
    queue.append(node)
    j = 0;
    i = 0;
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if (hospitalarray[i] == True):
            print("Hospital found at node: ", i + 1)
            break
        else:
            i += 1;
            print(i);
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    j = 0;
    i = 0;
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if (check[i] == s):

            # nodenum[j]=[i]; // if we want to store the position of all the TRUE hospitals with their nodes
            # j+=1;
            print("Hospital found at node: ", i + 1)
            break


        else:
            i += 1;
            print(i);
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


# Driver Code
bfs(visited, graph, 'A')
