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
import math

# functions go here

# Calculates the minimum distance classifier for a set of data
def calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , XY ):
    ''' This function takes the lists made from the file and finds all of the
    weather defined by X and Y and calculates the Minimum Distance Classifier
    for each of the list and returns them in the form:
    ( TempMean , HumiMean , WindMean , RainMean , UVMean , TempNorm , HumiNorm,
    WindNorm, RainNorm, UVNorm )
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
        Means = [ TempSum / len(Temp) , HumiSum / len(Humi) , WindSum / len(Wind) , RainSum / len(Rain) , UVSum / len(UV) ]
    except ZeroDivisionError:
        # There were non of the XY specified in the data, we will just return a
        #    single 0 for this
        return 0
    else:
        
        print(min(Temp) , max(Temp))
        
        # Calculate Norms. if statment indicates one value in set
        if float(max(Temp)) - float(min(Temp)) != 0:
            Means.append( (float(TempSum) - float(min(Temp)) ) / ( float(max(Temp)) - float(min(Temp)) ) )
        else:
            Means.append( 0 )
        if float(max(Humi)) - float(min(Humi)) != 0:
            Means.append( (float(HumiSum) - float(min(Humi)) ) / ( float(max(Humi)) - float(min(Humi)) ) )
        else:
            Means.append( 0 )
        if float(max(Wind)) - float(min(Wind)) != 0:
            Means.append( (float(WindSum) - float(min(Wind)) ) / ( float(max(Wind)) - float(min(Wind)) ) )
        else:
            Means.append( 0 )
        if float(max(Rain)) - float(min(Rain)) != 0:
            Means.append( (float(RainSum) - float(min(Rain)) ) / ( float(max(Rain)) - float(min(Rain)) ) )
        else:
            Means.append( 0 )
        if float(max(UV)) - float(min(UV)) != 0:
            Means.append( (float(UVSum) - float(min(UV)) ) / ( float(max(UV)) - float(min(UV)) ) )
        else:
            Means.append( 0 )
        
        return Means


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
            
    for i in WeatherList:
        i.replace( '\n' , '' )
        
    print( WeatherList )
    
    
    # we now find the means for each of the weather pattern
    # Hot
    HotSunnyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-sunny\n' )
    HotWindyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-windy\n' )
    HotOvercastMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-overcast\n' )
    HotRainyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-rainy\n' )
    HotHumidMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'hot-humid\n' )
    # Mild
    MildSunnyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-sunny\n' )
    MildWindyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-windy\n' )
    MildOvercastMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-overcast\n' )
    MildRainyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-rainy\n' )
    MildHumidMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'mild-humid\n' )
    # Cold
    ColdSunnyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-sunny\n' )
    ColdWindyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-windy\n' )
    ColdOvercastMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-overcast\n' )
    ColdRainyMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-rainy\n' )
    ColdHumidMeans = calculateMeans( TempList , HumiList , WindList , RainList , UVList , WeatherList , 'cold-humid\n' )
    
    print( ColdWindyMeans )
    
    
    #Print out the Class Centroids
    print( "Class Centroids(not normalized" )
    print( "Weather\t\tTemp\tHumi\tWind\tRain\tUV" )
    # Hot
    if HotSunnyMeans != 0:
        print( "hot-sunny\t", HotSunnyMeans[0], HotSunnyMeans[1], HotSunnyMeans[2], HotSunnyMeans[3], HotSunnyMeans[4], sep='\t' )
    if HotWindyMeans != 0:
        print( "hot-windy\t", HotWindyMeans[0], HotWindyMeans[1], HotWindyMeans[2], HotWindyMeans[3], HotWindyMeans[4], sep='\t' )
    if HotOvercastMeans != 0:
        print( "hot-overcast\t", HotOvercastMeans[0], HotOvercastMeans[1], HotOvercastMeans[2], HotOvercastMeans[3], HotOvercastMeans[4], sep='\t' )
    if HotRainyMeans != 0:
        print( "hot-rainy\t", HotRainyMeans[0], HotRainyMeans[1], HotRainyMeans[2], HotRainyMeans[3], HotRainyMeans[4], sep='\t' )
    if HotSunnyMeans != 0:
        print( "hot-humid\t", HotHumidMeans[0], HotHumidMeans[1], HotHumidMeans[2], HotHumidMeans[3], HotHumidMeans[4], sep='\t' )
    # Mild
    if MildSunnyMeans != 0:
        print( "mild-sunny\t", MildSunnyMeans[0], MildSunnyMeans[1], MildSunnyMeans[2], MildSunnyMeans[3], MildSunnyMeans[4], sep='\t' )
    if MildWindyMeans != 0:
        print( "mild-windy\t", MildWindyMeans[0], MildWindyMeans[1], MildWindyMeans[2], MildWindyMeans[3], MildWindyMeans[4], sep='\t' )
    if MildOvercastMeans != 0:
        print( "mild-overcast\t", MildOvercastMeans[0], MildOvercastMeans[1], MildOvercastMeans[2], MildOvercastMeans[3], MildOvercastMeans[4], sep='\t' )
    if MildRainyMeans != 0:
        print( "mild-rainy\t", MildRainyMeans[0], MildRainyMeans[1], MildRainyMeans[2], MildRainyMeans[3], MildRainyMeans[4], sep='\t' )
    if MildHumidMeans != 0:
        print( "mild-humid\t", MildHumidMeans[0], MildHumidMeans[1], MildHumidMeans[2], MildHumidMeans[3], MildHumidMeans[4], sep='\t' )
    # Cold
    if ColdSunnyMeans != 0:
        print( "cold-sunny\t", ColdSunnyMeans[0], ColdSunnyMeans[1], ColdSunnyMeans[2], ColdSunnyMeans[3], ColdSunnyMeans[4], sep='\t' )
    if ColdWindyMeans != 0:
        print( "cold-windy\t", ColdWindyMeans[0], ColdWindyMeans[1], ColdWindyMeans[2], ColdWindyMeans[3], ColdWindyMeans[4], sep='\t' )
    if ColdOvercastMeans != 0:
        print( "cold-overcast\t", ColdOvercastMeans[0], ColdOvercastMeans[1], ColdOvercastMeans[2], ColdOvercastMeans[3], ColdOvercastMeans[4] , sep='\t' )
    if ColdRainyMeans != 0:
        print( "cold-rainy\t", ColdRainyMeans[0], ColdRainyMeans[1], ColdRainyMeans[2], ColdRainyMeans[3], ColdRainyMeans[4], sep='\t' )
    if ColdHumidMeans != 0:
        print( "cold-humid\t", ColdHumidMeans[0], ColdHumidMeans[1], ColdHumidMeans[2], ColdHumidMeans[3], ColdHumidMeans[4], sep='\t' )
        
    print( '\n' )

    
    Total = 0
    Right = 0
    TestDate = []
    TestTemp = []
    TestHumi = []
    TestWind = []
    TestRain = []
    TestUV = []
    TestWeather = []
    
    j = 0

    # Read in each line of the test file and run the prediction on it
    for line in testFile:
        
        # separate the string to make it easier to parse, this will split based
        # on spaces and we will have empty strings that will need to be parced
        # out later
        elements = line.split( " " )
        
        
        
        if elements[0] != "Date":
            i = 0
            # 1st string will be the date,
            while elements[i] == '':
                i += 1
            TestDate[j] = elements[i]
            i += 1            
            # 2nd string we want is the Temp
            while elements[i] == '':
                i += 1
            TestTemp[j] = elements[i]
            i += 1
            # 3rd string we want is the Humidity
            while elements[i] == '':
                i += 1
            TestHumi[j] = elements[i]
            i += 1
            # 4th string we want is the Wind
            while elements[i] == '':
                i += 1
            TestWind[j] = elements[i]
            i += 1
            # 5th string we want is the Rain
            while elements[i] == '':
                i += 1
            TestRain[j] = elements[i]
            i += 1
            # 6th string we want is the UV index
            while elements[i] == '':
                i += 1
            TestUV[j] = elements[i]
            i += 1
            # last string we want is the weather desciption
            while elements[i] == '':
                i += 1
            TestWeather[j] = elements[i].rstrip(elements[-1:])
            Total += 1
        else:
            # first line printout
            print( line , "\t\tPredicted" )
        j += 1
        
    

    

    
    


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
        
