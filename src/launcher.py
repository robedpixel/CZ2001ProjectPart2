from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader
from BFS import complete_snap_multi_bfs_shortest_path_constant, snap_bfs_top_k_shortest, snap_bfs_shortest_path, output_to_file, complete_snap_bfs_top_k_shortest
import os

import time
print("clearing output file...")
if os.path.exists("output.txt"):
    os.remove("output.txt")
print("select hospital file")
hospital = HospitalLocationReader()
hospital.read_file()
hospital.get_hospital_locations()
print("select snap.py graph file")
reader = GraphFileReader()
reader.read_file()
reader.read_graph()
reader.display_status()

print("Which part of the project do you wish to test? a/b = 1 , c/d = 2")
user_input = int(input())
if user_input == 1:
    start_time = time.time()
    pathlist = complete_snap_multi_bfs_shortest_path_constant(reader.pungraph, hospital.hospitallocationlist, True)
    end_time = time.time()
    output_to_file(pathlist, True)
elif user_input == 2:
    print("There are " + str(len(hospital.hospitallocationlist)) + " hospitals")
    print("How many hospitals do you want to search a path for?:")
    num_hospitals_input = int(input())
    print("Input starting node range(input 0 to check for all nodes):")
    starting_range = int(input())
    if starting_range==0:
        start_time = time.time()
        pathlist = complete_snap_bfs_top_k_shortest(reader.pungraph, hospital.hospitallocationlist, num_hospitals_input, True)
        end_time = time.time()
    elif starting_range>0:
        print("Starting node = " + str(starting_range))
        print("Input ending node range:")
        ending_range = int(input())
        if ending_range>=starting_range:
            start_time = time.time()
            for x in range(starting_range,ending_range):
                pathlist = snap_bfs_top_k_shortest(x, reader.pungraph, hospital.hospitallocationlist, num_hospitals_input, True)
            end_time = time.time()
        else:
            print("error input")
    else:
        print("error input")
else:
    print("error input")

# Uncomment the type of search you want to do
# pathlist = snap_bfs_top_k_shortest(1, reader.pungraph, hospital.hospitallocationlist, num_hospitals_input, True)
# pathlist = snap_bfs_top_k_shortest(2, reader.pungraph, hospital.hospitallocationlist, num_hospitals_input, True)
# pathlist = complete_snap_bfs_top_k_shortest(reader.pungraph, hospital.hospitallocationlist, num_hospitals_input)

# uncomment to output results to a file
# output_to_file(pathlist)

for x in pathlist:
    print(x)
print("---time taken: %s seconds ---" % (end_time - start_time))