import snap
from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader
from BFS import complete_snap_multi_bfs_shortest_path_constant, snap_bfs_shortest_path, output_to_file, complete_snap_bfs_top_k_shortest
from RandomGraphGenerator import RandomGraphGenerator
from RandomHospitalLocationGen import gen_ran_hospital_locations
import time

hospitallist = list()
num_nodes = 100
num_edges = 100
num_hospitals_to_search = 8
num_hospitals = 16
graphobject = RandomGraphGenerator(num_nodes, num_edges)
randomgraph = graphobject.retrieve_random_graph()
hospitallist = gen_ran_hospital_locations(num_nodes, num_hospitals)
start_time = time.time()
pathlist = complete_snap_multi_bfs_shortest_path_constant(randomgraph, hospitallist, False)
output_to_file(pathlist, True)
#pathlist = complete_snap_bfs_top_k_shortest(randomgraph, hospitallist, num_hospitals_to_search, True)
end_time = time.time()
for i in pathlist:
    print(i)
print("---time taken: %s seconds ---" % (end_time - start_time))