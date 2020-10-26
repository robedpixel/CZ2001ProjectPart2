from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader
from BFS import snap_bfs

print("select hospital file")
hospital = HospitalLocationReader()
hospital.read_file()
hospital.get_hospital_locations()
print ("select snap.py graph file")
reader = GraphFileReader()
reader.read_file()
reader.read_graph()
reader.display_status()
snap_bfs(1, reader.pungraph, hospital.hospitallocationlist)
