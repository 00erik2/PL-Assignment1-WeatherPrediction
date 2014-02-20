# weather.py
# Author: Erik Hattervig
# Weather Prediction Program for SDSMT CSC 461 Programming Languages Spring 2014 Class
# Due Date: 2/19/14
#
# Decription: The perpose of this program is to take a set of weather data
#   povided by the user and calculate the minimum distance classifier from a 
#   normalized set of data for the set and predict the weather for a different 
#   set of data. The program will then check the results of that data and 
#   calculate how accurate it was as a percent.
#
# Run Instructions: python weather.py <trainningfile> <testingfile>
#

import sys
import math

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
    # Compute the Mean of each value, then the norms and return them
    
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
        # Calculate Norms. if statment indicates one value in set
        Means.append( (float(Means[0]) - float(min(TempList)) ) / ( float(max(TempList)) - float(min(TempList)) ) )
        Means.append( (float(Means[1]) - float(min(HumiList)) ) / ( float(max(HumiList)) - float(min(HumiList)) ) )
        Means.append( (float(Means[2]) - float(min(WindList)) ) / ( float(max(WindList)) - float(min(WindList)) ) )
        Means.append( (float(Means[3]) - float(min(RainList)) ) / ( float(max(RainList)) - float(min(RainList)) ) )
        Means.append( (float(Means[4]) - float(min(UVList)) ) / ( float(max(UVList)) - float(min(UVList)) ) )
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
    
    
    # we now find the means (normalized and not) for each of the weather patterns
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
    
    print(HotSunnyMeans[0])
    
    #Print out the Class Centroids in a nice format
    print( "Class Centroids(not normalized)" )
    print( '{0:25} {1:16} {2:15} {3:15} {4:15} {5:20}'.format( "Weather", "Temp", "Humi", "Wind", "Rain", "UV" ) )
    # Hot
    if HotSunnyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format( "hot-sunny", HotSunnyMeans[0], HotSunnyMeans[1], HotSunnyMeans[2], HotSunnyMeans[3], HotSunnyMeans[4] ) )
    if HotWindyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("hot-windy", HotWindyMeans[0], HotWindyMeans[1], HotWindyMeans[2], HotWindyMeans[3], HotWindyMeans[4] ) )
    if HotOvercastMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("hot-overcast", HotOvercastMeans[0], HotOvercastMeans[1], HotOvercastMeans[2], HotOvercastMeans[3], HotOvercastMeans[4]) )
    if HotRainyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("hot-rainy", HotRainyMeans[0], HotRainyMeans[1], HotRainyMeans[2], HotRainyMeans[3], HotRainyMeans[4] ) )
    if HotHumidMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("hot-humid", HotHumidMeans[0], HotHumidMeans[1], HotHumidMeans[2], HotHumidMeans[3], HotHumidMeans[4] ) )
    # Mild
    if MildSunnyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("mild-sunny", MildSunnyMeans[0], MildSunnyMeans[1], MildSunnyMeans[2], MildSunnyMeans[3], MildSunnyMeans[4]) )
    if MildWindyMeans != 0:
        print( '{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("mild-windy", MildWindyMeans[0], MildWindyMeans[1], MildWindyMeans[2], MildWindyMeans[3], MildWindyMeans[4]) )
    if MildOvercastMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("mild-overcast",MildOvercastMeans[0], MildOvercastMeans[1], MildOvercastMeans[2], MildOvercastMeans[3], MildOvercastMeans[4]))
    if MildRainyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("mild-rainy", MildRainyMeans[0], MildRainyMeans[1], MildRainyMeans[2], MildRainyMeans[3], MildRainyMeans[4]) )
    if MildHumidMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("mild-humid", MildHumidMeans[0], MildHumidMeans[1], MildHumidMeans[2], MildHumidMeans[3], MildHumidMeans[4]) )
    # Cold
    if ColdSunnyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("cold-sunny",ColdSunnyMeans[0], ColdSunnyMeans[1], ColdSunnyMeans[2], ColdSunnyMeans[3], ColdSunnyMeans[4]) )
    if ColdWindyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("cold-windy", ColdWindyMeans[0], ColdWindyMeans[1], ColdWindyMeans[2], ColdWindyMeans[3], ColdWindyMeans[4]) )
    if ColdOvercastMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("cold-overcast", ColdOvercastMeans[0], ColdOvercastMeans[1], ColdOvercastMeans[2], ColdOvercastMeans[3], ColdOvercastMeans[4]) )
    if ColdRainyMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("cold-rainy", ColdRainyMeans[0], ColdRainyMeans[1], ColdRainyMeans[2], ColdRainyMeans[3], ColdRainyMeans[4]) )
    if ColdHumidMeans != 0:
        print('{0:15} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f} {5:15.2f}'.format("cold-humid", ColdHumidMeans[0], ColdHumidMeans[1], ColdHumidMeans[2], ColdHumidMeans[3], ColdHumidMeans[4]) )
        
    print( '\n' )

    # initalize these varables to a begining state
    Total = 0
    Right = 0
    TestData = [[],[],[],[],[],[]]
    TestWeather = []

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
            TestData[0].append(elements[i])
            i += 1            
            # 2nd string we want is the Temp
            while elements[i] == '':
                i += 1
            TestData[1].append(elements[i])
            i += 1
            # 3rd string we want is the Humidity
            while elements[i] == '':
                i += 1
            TestData[2].append(elements[i])
            i += 1
            # 4th string we want is the Wind
            while elements[i] == '':
                i += 1
            TestData[3].append(elements[i])
            i += 1
            # 5th string we want is the Rain
            while elements[i] == '':
                i += 1
            TestData[4].append(elements[i]) 
            i += 1
            # 6th string we want is the UV index
            while elements[i] == '':
                i += 1
            TestData[5].append(elements[i])
            i += 1
            # last string we want is the weather desciption
            while elements[i] == '':
                i += 1
            TestWeather.append(elements[i])
            Total += 1
            
        # increment the total number of test data
        Total += 1
    
    # printout titles for this section
    print( '{0:25} {1:16} {2:15} {3:15} {4:15} {5:15} {6:20} {7:20}'.format("Date" , "Temp", "Humi", "Wind", "Rain", "UV" , "Weather" , "Predicted" ) )
    
    #Compute perdiction and output for each of the inputs
    i = 0
    for WeatherIncr in TestWeather:
        # Calculate Norms for test Data
        TestTempNorm = ( float(TestData[1][i]) - float(min(TestData[1])) ) / ( float(max(TestData[1])) - float(min(TestData[1])) ) 
        TestHumiNorm = ( float(TestData[2][i]) - float(min(TestData[2])) ) / ( float(max(TestData[2])) - float(min(TestData[2])) ) 
        TestWindNorm = ( float(TestData[3][i]) - float(min(TestData[3])) ) / ( float(max(TestData[3])) - float(min(TestData[3])) )  
        TestRainNorm = ( float(TestData[4][i]) - float(min(TestData[4])) ) / ( float(max(TestData[4])) - float(min(TestData[4])) )  
        TestUVNorm = ( float(TestData[5][i]) - float(min(TestData[5])) ) / ( float(max(TestData[5])) - float(min(TestData[5])) )  
        
        # Find the best minimum distance classifier
        if HotSunnyMeans != 0:
            bestdist = math.sqrt( (HotSunnyMeans[5] - TestTempNorm)**2 + (HotSunnyMeans[6] - TestHumiNorm)**2 + (HotSunnyMeans[7] - TestWindNorm )**2 + (HotSunnyMeans[8] - TestRainNorm )**2 + (HotSunnyMeans[9] - TestUVNorm)**2 )
            bestMatch = "hot-sunny\n"            
        if HotWindyMeans != 0:
            dist = math.sqrt( (HotWindyMeans[5] - TestTempNorm)**2 + (HotWindyMeans[6] - TestHumiNorm)**2 + (HotWindyMeans[7] - TestWindNorm )**2 + (HotWindyMeans[8] - TestRainNorm )**2 + (HotWindyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "hot-windy\n"
        if HotOvercastMeans != 0:
            dist = math.sqrt( (HotOvercastMeans[5] - TestTempNorm)**2 + (HotOvercastMeans[6] - TestHumiNorm)**2 + (HotOvercastMeans[7] - TestWindNorm )**2 + (HotOvercastMeans[8] - TestRainNorm )**2 + (HotOvercastMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "hot-overcast\n"
        if HotRainyMeans != 0:
            dist = math.sqrt( (HotRainyMeans[5] - TestTempNorm)**2 + (HotRainyMeans[6] - TestHumiNorm)**2 + (HotRainyMeans[7] - TestWindNorm )**2 + (HotRainyMeans[8] - TestRainNorm )**2 + (HotRainyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "hot-rainy\n"
        if HotHumidMeans != 0:
            dist = math.sqrt( (HotHumidMeans[5] - TestTempNorm)**2 + (HotHumidMeans[6] - TestHumiNorm)**2 + (HotHumidMeans[7] - TestWindNorm )**2 + (HotHumidMeans[8] - TestRainNorm )**2 + (HotHumidMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "hot-humid\n"
        if MildSunnyMeans != 0:
            dist = math.sqrt( (MildSunnyMeans[5] - TestTempNorm)**2 + (MildSunnyMeans[6] - TestHumiNorm)**2 + (MildSunnyMeans[7] - TestWindNorm )**2 + (MildSunnyMeans[8] - TestRainNorm )**2 + (MildSunnyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "mild-sunny\n"
        if MildWindyMeans != 0:
            dist = math.sqrt( (MildWindyMeans[5] - TestTempNorm)**2 + (MildWindyMeans[6] - TestHumiNorm)**2 + (MildWindyMeans[7] - TestWindNorm )**2 + (MildWindyMeans[8] - TestRainNorm )**2 + (MildWindyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "mild-windy\n"
        if MildOvercastMeans != 0:
            dist = math.sqrt( (MildOvercastMeans[5] - TestTempNorm)**2 + (MildOvercastMeans[6] - TestHumiNorm)**2 + (MildOvercastMeans[7] - TestWindNorm )**2 + (MildOvercastMeans[8] - TestRainNorm )**2 + (MildOvercastMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "mild-overcast\n"
        if MildRainyMeans != 0:
            dist = math.sqrt( (MildRainyMeans[5] - TestTempNorm)**2 + (MildRainyMeans[6] - TestHumiNorm)**2 + (MildRainyMeans[7] - TestWindNorm )**2 + (MildRainyMeans[8] - TestRainNorm )**2 + (MildRainyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "mild-rainy\n"
        if MildHumidMeans != 0:
            dist = math.sqrt( (MildHumidMeans[5] - TestTempNorm)**2 + (MildHumidMeans[6] - TestHumiNorm)**2 + (MildHumidMeans[7] - TestWindNorm )**2 + (MildHumidMeans[8] - TestRainNorm )**2 + (MildHumidMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "mild-humid\n"
        if ColdSunnyMeans != 0:
            dist = math.sqrt( (ColdSunnyMeans[5] - TestTempNorm)**2 + (ColdSunnyMeans[6] - TestHumiNorm)**2 + (ColdSunnyMeans[7] - TestWindNorm )**2 + (ColdSunnyMeans[8] - TestRainNorm )**2 + (ColdSunnyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "cold-sunny\n"
        if ColdWindyMeans != 0:
            dist = math.sqrt( (ColdWindyMeans[5] - TestTempNorm)**2 + (ColdWindyMeans[6] - TestHumiNorm)**2 + (ColdWindyMeans[7] - TestWindNorm )**2 + (ColdWindyMeans[8] - TestRainNorm )**2 + (ColdWindyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "cold-windy\n"
        if ColdOvercastMeans != 0:
            dist = math.sqrt( (ColdOvercastMeans[5] - TestTempNorm)**2 + (ColdOvercastMeans[6] - TestHumiNorm)**2 + (ColdOvercastMeans[7] - TestWindNorm )**2 + (ColdOvercastMeans[8] - TestRainNorm )**2 + (ColdOvercastMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "cold-overcast\n"
        if ColdRainyMeans != 0:
            dist = math.sqrt( (ColdRainyMeans[5] - TestTempNorm)**2 + (ColdRainyMeans[6] - TestHumiNorm)**2 + (ColdRainyMeans[7] - TestWindNorm )**2 + (ColdRainyMeans[8] - TestRainNorm )**2 + (ColdRainyMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "cold-rainy\n"
        if ColdHumidMeans != 0:
            dist = math.sqrt( (ColdHumidMeans[5] - TestTempNorm)**2 + (ColdHumidMeans[6] - TestHumiNorm)**2 + (ColdHumidMeans[7] - TestWindNorm )**2 + (ColdHumidMeans[8] - TestRainNorm )**2 + (ColdHumidMeans[9] - TestUVNorm)**2 )
            if dist < bestdist:
                bestdist = dist
                bestMatch = "cold-humid\n"
        
        # We have the prediction, print out the info and check if we are right
        print('{0:15} {1:15} {2:15} {3:15} {4:15} {5:15} {6:20} {7:20}'.format( TestData[0][i] , TestData[1][i] , TestData[2][i] , TestData[3][i] , TestData[4][i] , TestData[5][i] , TestWeather[i][:-1] , bestMatch[:-1] ) )
        
        if bestMatch == WeatherIncr:
            Right += 1
        # incramenter
        i += 1
        
    # print out results
    print( 'weaterPredictions: {0:2.1f}% correct'.format(( Right / Total ) * 100 ))
    
    
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
        
