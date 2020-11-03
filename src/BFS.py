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

def snap_bfs_shortest_path_constant(graph: snap.PUNGraph, hospital_locations_list: list) -> list:
    numnodes = graph.GetNodes()
    visitedarray = np.zeros((numnodes, 1), dtype=bool)
    output = list()
    # maintain a queue of paths
    queue = list()
    # push the hospital nodes into the queue

    for hospital in hospital_locations_list:
        queue.append([hospital])
        visitedarray[hospital] = True
        output.append([hospital])

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print("Current node: " + str(node))
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        current_node = graph.GetNI(int(node))
        for Id in current_node.GetOutEdges():
            if not visitedarray[Id]:
                # if not visitedarray[Id]:
                # visitedarray[Id] = True
                visitedarray[Id] = True
                new_path = list(path)
                new_path.append(Id)
                queue.append(new_path)
                output.append(new_path)
                print("edge (%d %d) not visited yet" % (current_node.GetId(), Id))
    return output

def snap_bfs_shortest_path(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list, num_hospitals_to_search: int) -> typing.Tuple[
    int, list]:
    """
    This function does breadth first search on a snap.py graph, it returns the node at which it has found a hospital
    and a list of the shortest path
    """
    # Create array of same size as number of nodes of graph
    #numnodes = graph.GetNodes()
    #hospitalarray = np.zeros((numnodes, 1), dtype=bool)
    #visitedarray = np.zeros((numnodes, 1), dtype=bool)

    output = list();
    visitedarray = list()
    found = 0
    #visitedarray.append(starting_node)
    #visitedarray[starting_node] = True

    # maintain a queue of paths
    queue = list()
    # push the hospital nodes into the queue

    for hospital in hospital_locations_list:
        queue.append([hospital])
        visitedarray.append([hospital, hospital])

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print("Current node: " + str(node))
        # path found
        if node == starting_node:
            print("Hospital path found")
            output.append(path)
            found += 1
            if found == num_hospitals_to_search:
                return output
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        current_node = graph.GetNI(int(node))
        for Id in current_node.GetOutEdges():
            if [path[0], Id] not in visitedarray:
            # if not visitedarray[Id]:
                #visitedarray[Id] = True
                visitedarray.append([path[0], Id])
                new_path = list(path)
                new_path.append(Id)
                queue.append(new_path)
                print("edge (%d %d) not visited yet" % (current_node.GetId(), Id))
    return output


def complete_snap_bfs_top_k_shortest(graph: snap.PUNGraph, hospital_locations_list: list,
                                     paths_to_find: int, bool_save_to_file: bool) -> list:
    """
    This function returns a list of paths from every node to the nearest k hospitals,
    uses snap_bfs_top_k_shortest function to check the nearest path to each hospital for each node
    """
    outputlist = list()
    for NI in graph.Nodes():
        paths = snap_bfs_shortest_path(NI.GetId(), graph, hospital_locations_list, paths_to_find)
        outputlist.extend(paths)
        if bool_save_to_file:
            output_to_file(paths)
    return outputlist


def output_to_file(bfs_path_list: list):
    """
    This function saves a list returned by any of the breadth-first-search functions
    into a file
    """
    file1 = open("output.txt", "a")
    for path in bfs_path_list:
        file1.write("From node " + str(path[-1]) + " to hospital at node " + str(path[0]) + "\n")
        file1.write("Distance: " + str(len(path)-1) + "\n")
        path.reverse()
        file1.write("Path: " + str(path) + "\n")
        file1.write("\n")
    file1.close()

