import glob
import os
import msvcrt

file_location = os.path.join('C:\\','path','to','input','directory','*.srt')

file_names = glob.glob(file_location)

def pause():
  print("\nPress any key to continue . . . ")
  msvcrt.getch()

def transcription ():
    file_progres = 0
    for file in file_names:

        input_file = open(file, "r", encoding="utf-8")
        output_file = open(file_location.split("*")[0] + "output directory\\" + file.removeprefix(file_location.split("*")[0]).removesuffix(".srt") + "_second part of the output name.srt", "w", encoding="utf-8")

        input_file_lines = input_file.readlines()

        input_file.close()

        line_number = 0
        line_buffor = 0

        for i in input_file_lines:

            line_number = line_number + 1

            try:

                if i[0] == "0" or i[0] == "1" or i[0] == "2" or i[0] == "3" or i[0] == "4" or i[0] == "5" or i[0] == "6" or i[0] == "7" or i[0] == "8" or i[0] == "9" or i[0] == " " or i[0] == "":
                    output_file.write(i)

                elif line_buffor + 1 == line_number or line_buffor + 2 == line_number:
                    line_buffor = line_number
                    output_file.write(i)

                else:
                    line_buffor = line_number
                    output_file.write("[text in first line of text in every block of text]: " + i)
                
            except:
                print("error")

        output_file.close()

        file_progres = file_progres + 1
        print("Progres: ", round((file_progres/len(file_names))*100, 2),"%")
    print("Program has finished with success!")
    pause()

transcription()
