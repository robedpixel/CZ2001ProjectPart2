import snap
from BFS import snap_bfs_shortest_path_constant, snap_bfs_shortest_path, output_to_file, complete_snap_bfs_top_k_shortest
from RandomGraphGenerator import RandomGraphGenerator
from RandomHospitalLocationGen import gen_ran_hospital_locations
import time

hospitallist = list()
num_nodes = 100
num_edges = 200
num_hospitals_to_search = 4
num_hospitals = 16
graphobject = RandomGraphGenerator(num_nodes, num_edges)
randomgraph = graphobject.retrieve_random_graph()
hospitallist = gen_ran_hospital_locations(num_nodes, num_hospitals)
start_time = time.time()
pathlist = snap_bfs_shortest_path_constant(randomgraph,hospitallist)
#pathlist = complete_snap_bfs_top_k_shortest(randomgraph, hospitallist, num_hospitals_to_search, False)
end_time = time.time()
for i in pathlist:
    print(i)
print("---time taken: %s seconds ---" % (end_time - start_time))