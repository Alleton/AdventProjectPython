'''
Created on 17 févr. 2016

@author: jf
    solve day1 
''' 
import services.readfile

class AdventDay1():
    '''
    classdocs
    '''


    def __init__(self,test):
        '''
        Constructor
        '''
        self.nom=""
        self.opening= 0
        self.closing=0
        self.testing=test
       
    
    def __run__(self):
        print("Class AdventDay1 --run--")
        print ("Test = " + str(self.testing ))
        
        part2=True
        #FileContent = services.readfile.adventRead(1)
        
        
        
        f = open("../resources/AdventProject1.txt", 'r')   
        # read entire content of file into memory
        #f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
        for line in f:
            print ( line )
            print (len(line))
            for index in range (0 , len(line)) :
                if (line[index] == '(' ):
                    self.opening = self.opening + 1
        
                if (line[index] == ')' ):
                    self.closing = self.closing + 1
        
                if ( part2 and self.opening - self.closing == -1 ) :
                    print ("Done Part2 at " + str(index + 1))
                    part2=False
    # clear file content 
        f.close()
        
        #print( " len = " + str(len(FileContent) ) )
        
        
        
        
        return (" return AdventDay1 Part1 " + str ( self.opening - self.closing ) ) 
    