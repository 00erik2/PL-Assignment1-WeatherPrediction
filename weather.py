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
    '''attempts to open a file, exits program if unable to'''
    try:
        file = open( trainingFileName )
    except ( IOError ):
        print( "Error: Unable to open file:", filename )
        sys.exit()
    return file


# Takes the to files and runs the prediction algorithm on the training file and
# then compairs the predictions to the test file and prints out the results
def runPrediction( trainFile , testFile ):
    
    # get the input from the training File
    # for each of the lines of the file
    for line in trainFile:
        
        # separate the string to make it easier to parse, this will split based
        # on spaces and we will have empty strings that will need to be parced
        # out later
        elements = line.split( " " )
        
        # Skip over the first line of the file
        if elements[0] != "Date":
            
            # 1st string will be the date, we can skip this
            # 2nd string we want is the Temp we need to incrament passed the
            #     empty strings to get to it
            i = 1
            while line[i] == '':
                i += 1
            TempList.append( line[i] )
            i += 1
            # 3rd string we want is the Humidity
            while line[i] == '':
                i += 1
            HumiList.append( line[i] )
            i += 1
            # 4th string we want is the Wind
            while line[i] == '':
                i += 1
            WindList.append( line[i] )
            i += 1
            # 5th string we want is the Rain
            while line[i] == '':
                i += 1
            RainList.append( line[i] )
            i += 1
            # 6th string we want is the UV index
            while line[i] == '':
                i += 1
            UVList.append( line[i] )
            i += 1
            # last string we want is the weather desciption
            while line[i] == '':
                i += 1
            WeatherList.append( line[i] )
            
        #debug
        print( "Temp: ", TempList[0] )
        print( "Humidity: ", HumiList[0] )
        print( "Wind: ", WindList[0] )
        print( "Rain: ", RainList[0] )
        print( "UV: ", UVList[0] )
        print( "Weather: ", WeatherList[0] )
            
        
    
    


# allows to run the module as a program
# gets the filenames from the command line, then has them opened and sends the
#   files to a function that takes care of the comutations. Then closes the
#   files and exits.
if __name__ == '__main__':
    if len( sys.argv ) > 2:
        # we have command line args
        # open the files for reading
        trainingFileName = sys.argv[1]
        testingFileName = sys.argv[2]
        
        # attempt to open the files
        trainingFile = openfile( trainingFileName )
        testingFile = openfile( testingFileName )
        
        runPrediction( trainingFile , testingFile )
        
        
        
        # closing the file
        trainingFile.close()
        testingFile.close()
    else:
        print( "Error: not enough arguments were specified!" )
        
