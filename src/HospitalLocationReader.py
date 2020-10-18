from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


class HospitalLocationReader:
    def __init__(self):
        self.filename = ""
        self.hospitallocationlist = list()

    def read_file(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

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

            return self.hospitallocationlist
            for number in self.hospitallocationlist:
                print(number)
            # close file gracefully
            f.close()
