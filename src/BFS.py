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

def complete_snap_multi_bfs_shortest_path_constant(graph: snap.PUNGraph, hospital_locations_list: list, is_actual_road_network : bool) -> list:
    numnodes = graph.GetNodes()

    # This code is needed because not all nodes are sequential for the actual road network graphs
    if is_actual_road_network:
        for NI in graph.Nodes():
            if NI.GetId() > numnodes:
                numnodes = NI.GetId()

    visitedarray = np.zeros((numnodes+1, 1), dtype=bool)
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
                visitedarray[Id] = True
                new_path = list(path)
                new_path.append(Id)
                queue.append(new_path)
                output.append(new_path)
                print("edge (%d %d) not visited yet" % (current_node.GetId(), Id))
    return output

def snap_bfs_shortest_path(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list) -> typing.Tuple[
    int, list]:
    """
    This function does breadth first search on a snap.py graph, it returns the node at which it has found a hospital
    and a list of the shortest path
    """
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
    return -1, list()


def snap_bfs_top_k_shortest(starting_node: int, graph: snap.PUNGraph, hospital_locations_list: list,
                            paths_to_find: int, bool_save_to_file: bool) -> list:
    """
    This function returns a list of paths from 1 node to the nearest k hospitals,
    uses snap_bfs_shortest_path function to check the nearest path to each hospital
    """
    list_of_paths = list()
    p_hospital_locations_list = hospital_locations_list.copy()
    if paths_to_find < 0:
        print("can't find zero or negative paths!")
        return
    if paths_to_find > len(hospital_locations_list):
        print("can't find more paths than there are hospitals!")
        return
    for x in range(paths_to_find):
        hospitalnode, path = snap_bfs_shortest_path(starting_node, graph, p_hospital_locations_list)
        if path:
            list_of_paths.append(path)
            p_hospital_locations_list.remove(hospitalnode)
    if bool_save_to_file:
        output_to_file(list_of_paths, False)
    return list_of_paths


def complete_snap_bfs_top_k_shortest(graph: snap.PUNGraph, hospital_locations_list: list,
                                     paths_to_find: int, bool_save_to_file: bool) -> list:
    """
    This function returns a list of paths from every node to the nearest k hospitals,
    uses snap_bfs_top_k_shortest function to check the nearest path to each hospital for each node
    """
    outputlist = list()
    for NI in graph.Nodes():
        paths = snap_bfs_top_k_shortest(NI.GetId(), graph, hospital_locations_list, paths_to_find, bool_save_to_file)
        outputlist.extend(paths)
    return outputlist

def output_to_file(bfs_path_list: list, is_list_reversed: bool):
    """
    This function saves a list returned by any of the breadth-first-search functions
    into a file
    """
    file1 = open("output.txt", "a")
    if is_list_reversed:
        for path in bfs_path_list:
            file1.write("From node " + str(path[-1]) + " to hospital at node " + str(path[0]) + "\n")
            file1.write("Distance: " + str(len(path)-1) + "\n")
            path.reverse()
            file1.write("Path: " + str(path) + "\n")
            file1.write("\n")
    else:
        for path in bfs_path_list:
            file1.write("From node " + str(path[0]) + " to hospital at node " + str(path[-1]) + "\n")
            file1.write("Distance: " + str(len(path)-1) + "\n")
            file1.write("Path: " + str(path) + "\n")
            file1.write("\n")
    file1.close()

