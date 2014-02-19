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

# Calculates the minimum distance classifier for a set of data
def calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , XY ):
    ''' This function takes the lists made from the file and finds all of the
    weather defined by X and Y and calculates the Minimum Distance Classifier
    for each of the list and returns them in the form:
    ( TempMean , HumiMean , WindMean , RainMean , UVMean )
    '''
    # create the lists that I will need
    Temp = []
    Humi = []
    Wind = []
    Rain = []
    UV = []
    
    # find each of the X-Y weathers in the main lists and put the corisponding 
    #    elements into the new list to be processed
    i = 0
    for type in WeatherList:
        
        # Check if the Weather at this point is the one we are looking for
        if WeatherList[int(i)] == XY:
            
            # if it is we need to put all of the assosiated data in our new
            #     lists
            Temp.append( TempList[i] )
            Humi.append( HumiList[i] )
            Wind.append( WindList[i] )
            Rain.append( RainList[i] )
            UV.append( UVList[i] )
        i += 1
    
    # We now have all of the needed values
    # Compute the Mean of each value and return them
    
    TempSum = 0
    HumiSum = 0
    WindSum = 0
    RainSum = 0
    UVSum = 0
    
    for i in Temp:
        TempSum += float(i)
    for i in Humi:
        HumiSum += float(i)
    for i in Wind:
        WindSum += float(i)
    for i in Rain:
        RainSum += float(i)
    for i in UV:
        UVSum += float(i)
    
    # return the mean Values
    try:
        results = ( TempSum / len(Temp) , HumiSum / len(Humi) , WindSum / len(Wind) , RainSum / len(Rain) , UVSum / len(UV) )
    except ZeroDivisionError:
        # There were non of the XY specified in the data, we will just return a
        #    single 0 for this
        return 0
    else:
        return results


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
    
    TempList = []
    HumiList = []
    WindList = []
    RainList = []
    UVList = []
    WeatherList = []
    
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
            while elements[i] == '':
                i += 1
            TempList.append( elements[i] )
            i += 1
            # 3rd string we want is the Humidity
            while elements[i] == '':
                i += 1
            HumiList.append( elements[i] )
            i += 1
            # 4th string we want is the Wind
            while elements[i] == '':
                i += 1
            WindList.append( elements[i] )
            i += 1
            # 5th string we want is the Rain
            while elements[i] == '':
                i += 1
            RainList.append( elements[i] )
            i += 1
            # 6th string we want is the UV index
            while elements[i] == '':
                i += 1
            UVList.append( elements[i] )
            i += 1
            # last string we want is the weather desciption
            while elements[i] == '':
                i += 1
            WeatherList.append( elements[i] )
    
    # remove the "\n" at the end of each of the weathers
    '''for i in WeatherList:
        WeatherList[i].rstrip(WeatherList[i][-3:])'''
    
    # we now find the means for each of the weather pattern
    # Hot
    HotSunnyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-sunny\n' )
    HotWindyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , "hot-windy\n" )
    HotOvercastValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-overcast\n' )
    HotRainyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-rainy\n' )
    HotHumidValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-humid\n' )
    # Mild
    MildSunnyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-sunny\n' )
    MildWindyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-windy\n' )
    MildOvercastValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-overcast\n' )
    MildRainyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-rainy\n' )
    MildHumidValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-humid\n' )
    # Cold
    ColdSunnyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-sunny\n' )
    ColdWindyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-windy\n' )
    ColdOvercastValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-overcast\n' )
    ColdRainyValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-rainy\n' )
    ColdHumidValues = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-humid\n' )
    
    #debug
    print( HotSunnyValues )
    print( HotWindyValues )
    print( HotOvercastValues )
    print( HotRainyValues )
    print( HotHumidValues )
    print( MildSunnyValues )
    print( MildWindyValues )
    print( MildOvercastValues )
    print( MildRainyValues )
    print( MildHumidValues )
    
    print( ColdSunnyValues )
    print( ColdWindyValues )
    print( ColdOvercastValues )
    print( ColdRainyValues )
    print( ColdHumidValues )




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
        
        # run the prediction function on the 2 files
        runPrediction( trainingFile , testingFile )
        
        # closing the file
        trainingFile.close()
        testingFile.close()
    else:
        print( "Error: not enough arguments were specified!" )
        
