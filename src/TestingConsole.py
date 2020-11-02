import snap
from BFS import snap_bfs_top_k_shortest, output_to_file, complete_snap_bfs_top_k_shortest
from RandomGraphGenerator import RandomGraphGenerator
from RandomHospitalLocationGen import gen_ran_hospital_locations
import time

hospitallist = list()
num_nodes = 400
num_edges = 800
num_hospitals = 8
graphobject = RandomGraphGenerator(num_nodes, num_edges)
randomgraph = graphobject.retrieve_random_graph()
hospitallist = gen_ran_hospital_locations(num_nodes, num_hospitals)
start_time = time.time()
pathlist = snap_bfs_top_k_shortest(1, randomgraph, hospitallist, 4, True)
#pathlist = complete_snap_bfs_top_k_shortest(randomgraph, hospitallist, 4, False)
end_time = time.time()

print("---time taken: %s seconds ---" % (end_time - start_time))