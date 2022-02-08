import glob
import os

file_location = os.path.join('C:\\','path','to','input','directory','*.srt')

filenames = glob.glob(file_location)

for file in filenames :

    inputFile = open( file , "r", encoding="utf-8")
    outputFile = open( file_location.split("*")[0]+"output Directory\\" + file.removeprefix(file_location.split("*")[0]).removesuffix(".srt") +"_second part of the output name.srt", "w", encoding="utf-8")

    inputFileLines = inputFile.readlines()
    
    lineNumber = 0
    lineBuffor = 0
    
    for i in inputFileLines:
        
        lineNumber = lineNumber+1
        
        if i[0] == "0" or i[0] == "1" or i[0] == "2" or i[0] == "3" or i[0] == "4" or i[0] == "5" or i[0] == "6" or i[0] == "7" or i[0] == "8" or i[0] == "9" or i[0] == " " or i[0] == "":
            outputFile.write(i)
            
        elif lineBuffor+1 == lineNumber or lineBuffor+2 == lineNumber :
                lineBuffor = lineNumber
                outputFile.write(i)
                
        else:
                lineBuffor = lineNumber
                outputFile.write("[text in first line of text in every block of text]: " + i)
                
    inputFile.close()
    outputFile.close()
