from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader
from BFS import snap_bfs_top_k_shortest

print("select hospital file")
hospital = HospitalLocationReader()
hospital.read_file()
hospital.get_hospital_locations()
print ("select snap.py graph file")
reader = GraphFileReader()
reader.read_file()
reader.read_graph()
reader.display_status()
pathlist = snap_bfs_top_k_shortest(1, reader.pungraph, hospital.hospitallocationlist,2)
for x in pathlist:
    print(x)
