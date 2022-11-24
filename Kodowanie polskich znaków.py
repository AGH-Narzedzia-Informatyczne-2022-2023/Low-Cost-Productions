

f = open("filename", "r", encoding="utf-8")
f.read()
import codecs

try:
   
    from tkFileDialog import askopenfilename
    from Tkinter import Tk, LabelFrame, Button, OptionMenu, StringVar
except ImportError:

    from tkinter.filedialog import askopenfilename
    from tkinter import Tk, LabelFrame, Button, OptionMenu, StringVar



zestawieZnakow = ("windows-1250", "iso-8859-2", "windows-1252") 
stareKodowaniePliku = wybierajZestawZnakow(zestawieZnakow) 

imiePlikuOryginalnego = askopenfilename() 
plikOryginalny = codecs.open(imiePlikuOryginalnego, 'r', stareKodowaniePliku)

ostatkniaKropka = imiePlikuOryginalnego.rfind(".") 
imieNowegoPliku = imiePlikuOryginalnego[:ostatkniaKropka] + "_UTF-8"+imiePlikuOryginalnego[ostatkniaKropka:]

nowyPlik = codecs.open(imieNowegoPliku, 'w', 'utf-8')

for kreska in plikOryginalny.readlines():
    nowyPlik.write(kreska) 

plikOryginalny.close()
nowyPlik.close()

#kodowanie polskiech znaków