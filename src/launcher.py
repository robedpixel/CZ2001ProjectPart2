from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader
from BFS import snap_bfs_top_k_shortest, output_to_file, complete_snap_bfs_top_k_shortest
import time

print("select hospital file")
hospital = HospitalLocationReader()
hospital.read_file()
hospital.get_hospital_locations()
print("select snap.py graph file")
reader = GraphFileReader()
reader.read_file()
reader.read_graph()
reader.display_status()

print("There are " + str(len(hospital.hospitallocationlist)) + " hospitals")
print("How many hospitals do you want to search a path for?:")
num_hospitals_input = int(input())


start_time = time.time()

# Uncomment the type of search you want to do
pathlist = snap_bfs_top_k_shortest(1, reader.pungraph, hospital.hospitallocationlist, num_hospitals_input)
# pathlist = complete_snap_bfs_top_k_shortest(reader.pungraph, hospital.hospitallocationlist, num_hospitals_input)

end_time = time.time()

# uncomment to output results to a file
# output_to_file(pathlist)

for x in pathlist:
    print(x)
print("---time taken: %s seconds ---" % (end_time - start_time))