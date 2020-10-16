from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import snap

class GraphFileReader:
    def __init__(self):
        self.filename = ""
        self.Fin = ""
        self.pungraph = ""

    def read_file(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    def read_graph(self):
        self.pungraph = snap.LoadEdgeList(snap.PUNGraph, self.filename, 0, 1)

    def display_status(self):
        print(type(self.pungraph))
        print("number of nodes:" + str(self.pungraph.GetNodes()))
