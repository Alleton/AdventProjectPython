import sys
import shutil
import re

def adventReplace(n):

    # open file with r+b (allow write and binary mode)
    f = open("adventDay2.py", 'r')   
    # read entire content of file into memory
    f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
    f_content = re.sub('2', str(n), f_content)
    # return pointer to top of file so we can re-write the content with replaced string
    f.seek(0)
    # clear file content 
    f.close()
    
    
    f = open("adventDay" + str(n)+".py", 'a')   
    
    f.truncate()
    
    # re-write the content with the updated content
    f.write(f_content)
    # close file
    f.close()
