# weather.py
# Author: Erik Hattervig
# Weather Prediction Program for SDSMT CSC 461 Programming Languages Spring 2014 Class
#
# Decription: The perpose of this program is to take a set of weather data
#   povided by the user and calculate the minimum distance classifier for the
#   set and predict the weather for a different set of data. The program will
#   then check the results of that data and calculate how accurate it was as a
#   percent.

import sys

# functions go here


# attempts to open a file for input and exits the program if unable to
def openfile( filename ):
    try:
        file = open( trainingFileName )
    except ( IOError ):
        print( "Error: Unable to open file:", filename )
        sys.exit()
    return file



# allows to run the module as a program
if __name__ == '__main__':
    if len( sys.argv ) > 2:
        # we have command line args
        # open the files for reading
        trainingFileName = sys.argv[1]
        testingFileName = sys.argv[2]
        
        # attempt to open the files
        trainingFile = openfile( trainingFileName )
        testingFile = openfile( testingFileName )
        
        print( "files opened!" )
        
        # closing the file
        trainingFile.close()
        testingFile.close()
    else:
        print( "Error: not enough arguments were specified!" )
        
        
