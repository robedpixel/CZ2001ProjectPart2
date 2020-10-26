import snap
import numpy as np
import typing

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


# this function does breadth first search on a snap.py graph, it returns the node at which it has found a hospital
# and a list of the shortest path
def snap_bfs_shortest_path(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list) -> typing.Tuple[
    int, list]:
    # Create array of same size as number of nodes of graph
    numnodes = graph.GetNodes()
    hospitalarray = np.zeros((numnodes, 1), dtype=bool)
    visitedarray = np.zeros((numnodes, 1), dtype=bool)
    # load array with values in hospital list
    for location in hospital_locations_list:
        hospitalarray[location] = True

    visitedarray[starting_node] = True

    # maintain a queue of paths
    queue = list()
    # push the first path into the queue
    queue.append([starting_node])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print("Current node: " + str(node))
        # path found
        if hospitalarray[node]:
            print("Hospital found at node: ", str(node))
            return node, path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        current_node = graph.GetNI(int(node))
        for Id in current_node.GetOutEdges():
            if not visitedarray[Id]:
                visitedarray[Id] = True
                new_path = list(path)
                new_path.append(Id)
                queue.append(new_path)
                print("edge (%d %d) not visited yet" % (current_node.GetId(), Id))


# This function returns a list of paths from 1 node to the nearest hospital
def snap_bfs_top_k_shortest(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list,
                            paths_to_find: int) -> list:
    list_of_paths = list()
    if paths_to_find < 0:
        print("can't find zero or negative paths!")
        return
    if paths_to_find > len(hospital_locations_list):
        print("can't find more paths than there are hospitals!")
        return
    for x in range(paths_to_find):
        hospitalnode, path = snap_bfs_shortest_path(starting_node, graph, hospital_locations_list)
        list_of_paths.append(path)
        hospital_locations_list.remove(hospitalnode)
    return list_of_paths


def complete_snap_bfs_top_k_shortest(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list,
                                     paths_to_find: int) -> list:
    outputlist = list()
    for NI in graph.Nodes():
        paths = snap_bfs_top_k_shortest(NI.GetId(), graph, hospital_locations_list, paths_to_find)
        outputlist.extend(paths)
    return outputlist


def output_to_file(bfs_path_list: list):
    file1 = open("output.txt", "a")
    for path in bfs_path_list:
        file1.write("From node " + str(path[0]) + " to hospital at node " + str(path[-1]) + "\n")
        file1.write("Distance: " + str(len(path)) + "\n")
        file1.write("Path: " + str(path) + "\n")
        file1.write("\n")
    file1.close()


# DEPRECATED basic breadth first search on a snap.py graph
def snap_bfs(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list) -> int:
    # Create array of same size as number of nodes of graph
    numnodes = graph.GetNodes()
    hospitalarray = np.zeros((numnodes, 1), dtype=bool)
    visitedarray = np.zeros((numnodes, 1), dtype=bool)
    # load array with values in hospital list
    for location in hospital_locations_list:
        hospitalarray[location] = True

    visitedarray[starting_node] = True
    queue.append(starting_node)
    i = 0
    while queue:
        s = queue.pop(0)
        print("Current node: " + str(s))
        if hospitalarray[s]:
            print("Hospital found at node: ", s)
            return s
            break
        else:
            i += 1;
            current_node = graph.GetNI(int(s))
            for Id in current_node.GetOutEdges():
                if not visitedarray[Id]:
                    visitedarray[Id] = True
                    queue.append(Id)
                    print("edge (%d %d) not visited yet" % (current_node.GetId(), Id))


# DEPRECATED
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
# bfs(visited, graph, 'A')
