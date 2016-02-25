'''
Created on 16 févr. 2016

@author: jf
Gui to solve Advent
'''
from tkinter import Tk
import adventView.adView


def main():
    root = Tk()
    adventView.adView.Advent(root)
    root.title("Advent")
    root.mainloop()
if __name__ == '__main__':
    main()