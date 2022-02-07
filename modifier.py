fileName = "file name in the same directory"

inputFile = open( "input path to the directory\\"+ fileName +".srt", "r", encoding="utf-8")
outputFile = open( "output path to the directory\\"+ fileName +"_second part of the output name.srt", "w", encoding="utf-8")

inputFileLines = inputFile.readlines()
lineNumber = 0
lineBuffor = 0
for i in inputFileLines:
    lineNumber = lineNumber+1
    if i[0] == "0" or i[0] == "1" or i[0] == "2" or i[0] == "3" or i[0] == "4" or i[0] == "5" or i[0] == "6" or i[0] == "7" or i[0] == "8" or i[0] == "9" or i[0] == " " or i[0] == "":
        outputFile.write(i)
    else:
        if lineBuffor+1 == lineNumber or lineBuffor+2 == lineNumber :
            lineBuffor = lineNumber
            outputFile.write(i)
        else:
            lineBuffor = lineNumber
            outputFile.write("[text in every first line of text, in file]: " + i)
