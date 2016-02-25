import sys
import shutil
import re


def adventRead(n):
    print ("adventRead " + str(n))
    # open file with r+b (allow write and binary mode)
    f = open("../resources/AdventProject" + str(n)+"_1.txt", 'r')   
    # read entire content of file into memory
    f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
    for line in f:
        print ( line )
        print (line.size())
    # clear file content 
    f.close()
    return f_content
