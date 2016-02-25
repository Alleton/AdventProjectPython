
from tkinter import *
from tkinter import ttk
import services.advent

class Advent:
    def __init__(self, master, size=15):
        
        CheckVarTest = IntVar()
        self.master = master
        self.size = size
        self.busy = 0
        
        self.topframe  = Frame(master, bg="yellow", width=300, height=300, padx=10, pady=10)
        self.topframe.pack(side=TOP) 
        self.b_go = Button(self.topframe ,
                           text = "Go")
        self.b_go.pack(fill=X)
        
        self.chkT = Checkbutton(self.topframe, text = "Test", variable = CheckVarTest, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        self.chkT.pack(fill=Y)

        

        self.content = ttk.Frame(master)
        self.content.pack(side=BOTTOM)
        boutons = []

        for x in range(0,5):
            for y in range(0,5):
                #bxy = Button(content,text= x*5 + y + 1 , command=bCallBack( x*5 + y + 1)).grid(row=x,column=y)
                bxy = x*5 + y + 1
#                 boutons.append(Button(self.content,text= bxy , 
#                                       command= lambda: bCallBack(position= bxy)).grid(row=x,column=y))
                boutons.append( Button(self.content,text= bxy , 
                                       command= lambda posi=bxy :bCallBack(position= posi)).grid(row=x,column=y)) 


def bCallBack(position):
    print( position)
    methodTocall = getattr(services.advent, "_adventDay" + str(position))
    methodTocall()