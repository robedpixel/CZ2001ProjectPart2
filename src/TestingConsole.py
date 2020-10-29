import snap
from BFS import snap_bfs_top_k_shortest, output_to_file, complete_snap_bfs_top_k_shortest
from RandomGraphGenerator import RandomGraphGenerator
from RandomHospitalLocationGen import gen_ran_hospital_locations
import time

hospitallist = list()
graphobject = RandomGraphGenerator(400, 800)
randomgraph = graphobject.retrieve_random_graph()
hospitallist = gen_ran_hospital_locations(100, 4)
start_time = time.time()
pathlist = complete_snap_bfs_top_k_shortest(randomgraph, hospitallist, 4, False)
end_time = time.time()

print("---time taken: %s seconds ---" % (end_time - start_time))