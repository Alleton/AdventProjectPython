'''
Created on 12 févr. 2016
try first window creation
@author: jf
'''

from tkinter import *
import sys
from tkinter.constants import TOP


class Advent:
     def __init__(self, master, size=15):
        self.master = master
        self.size = size
        self.busy = 0

        self.topframe  = Frame(master)
        self.topframe.pack(side=TOP) 
        self.b_go = Button(self.topframe ,
                           text = "Go")
        self.b_go.pack(fill=X)


        self.botframe = Frame(master)
        self.botframe.pack(side=BOTTOM)

        self.botleftframe = Frame(self.botframe)
        self.botleftframe.pack(side=LEFT, fill=Y)
        
        self.botrightframe = Frame(self.botframe)
        self.botrightframe.pack(side=RIGHT, fill=Y)


        self.b_qsort = Button(self.botleftframe,
                        text =  "Day 1", command=self.c_qsort)

        self.b_qsort.pack(fill=X)
        

     def c_qsort(self):
        print("Day1")
        print(sys.path)

#         self.b_qsort = Button(self.botleftframe,
#                               text="Quicksort", command=self.c_qsort)
#         self.b_qsort.pack(fill=X)
#         self.b_isort = Button(self.botleftframe,
#                               text="Insertion sort", command=self.c_isort)
#         self.b_isort.pack(fill=X)
#         self.b_ssort = Button(self.botleftframe,
#                               text="Selection sort", command=self.c_ssort)
#         self.b_ssort.pack(fill=X)
#         self.b_bsort = Button(self.botleftframe,
#                               text="Bubble sort", command=self.c_bsort)
#         self.b_bsort.pack(fill=X)
    
def c1_qsort(self):
    #    self.run(quicksort)
    print("Day1")
    pass
    




def main():
    root = Tk()
    #root.title("Advent")
    demo = Advent(root)
    root.title("Advent")
    #root.protocol('WM_DELETE_WINDOW', demo.c_quit)
    root.mainloop()

if __name__ == '__main__':
    main()