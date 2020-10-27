from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import snap

class GraphFileReader:
    """
    A Class to read a file containing a snap.py graph and load it into a PUNGraph object which can then
    be accessed

    """
    def __init__(self):
        self.filename = ""
        self.Fin = ""
        self.pungraph = ""

    def read_file(self):
        """
        Displays a gui file prompt to read a snap.py file
        """
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename(title='Select snap.py graph File')  # show an "Open" dialog box and return the path to the selected file

    def read_graph(self) -> snap.PUNGraph:
        self.pungraph = snap.LoadEdgeList(snap.PUNGraph, self.filename, 0, 1)
        return self.pungraph

    def display_status(self):
        print(type(self.pungraph))
        print("number of nodes:" + str(self.pungraph.GetNodes()))
        # Snap.py graph uses numbers to identify nodes
        # for NI in self.pungraph.Nodes():
        #    print("node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))
