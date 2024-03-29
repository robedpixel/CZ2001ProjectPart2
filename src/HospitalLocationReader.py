from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


class HospitalLocationReader:
    """
    A Class to read a file containing the assignment's defined format for storing hospital nodes and then store
    the information in a list within a class

    """
    def __init__(self):
        self.filename = ""
        self.hospitallocationlist = list()

    def read_file(self):
        """
        Displays a gui file prompt to read a file containing hospital node locations
        """
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename(title='Select Hospital Text File')  # show an "Open" dialog box and return the path to the selected file

    def get_hospital_locations(self) -> list:
        print("reading: " + self.filename)
        if self.filename:
            f = open(self.filename, "r")

            firstline = f.readline()
            # remove first two characters
            firstline = firstline[2:]
            # read in number of hospitals, set it to limit
            limit = int(firstline.strip())
            # read all the locations of the hospitals
            count = 0
            while count < limit:
                count += 1

                # Get next line from file
                line = f.readline()
                # if line is empty
                # end of file is reached
                if not line:
                    break

                #load hospital location into list
                self.hospitallocationlist.append(int(line.strip()))

            for number in self.hospitallocationlist:
                print(number)
            # close file gracefully
            f.close()
            return self.hospitallocationlist
