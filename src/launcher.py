from HospitalLocationReader import HospitalLocationReader
from GraphFileReader import GraphFileReader

#reader = HospitalLocationReader()
#reader.read_file()
#reader.get_hospital_locations()
reader = GraphFileReader()
reader.read_file()
reader.read_graph()
reader.display_status()
