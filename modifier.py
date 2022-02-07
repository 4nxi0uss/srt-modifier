fileName = "XXXVI Nadzwyczajna Sesja Rady Miejskiej w Zatorze 07 09 2021"

file = open( "przed dodaniem\\"+ fileName +".srt", "r", encoding="utf-8")
file1 = open( "po dodaniu tekstu maszynowego\\"+ fileName +"_dodano_tekst_maszynowy.srt", "w", encoding="utf-8")

tak = file.readlines()
d = 0
c = 0
for i in tak:
    d = d+1
    if i[0] == "0" or i[0] == "1" or i[0] == "2" or i[0] == "3" or i[0] == "4" or i[0] == "5" or i[0] == "6" or i[0] == "7" or i[0] == "8" or i[0] == "9" or i[0] == " " or i[0] == "":
        # f = f+1
        file1.write(i)
    else:
        if c+1 == d or c+2 == d :
            c = d
            file1.write(i)
        else:
            c = d
            file1.write("[Tłumaczenie  Maszynowe]: " + i)