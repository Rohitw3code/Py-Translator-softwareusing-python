#--------Author-Rohit Kumar-------------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
import pyttsx3 
import threading
import os 

root=Tk()
root.geometry("755x800")
root.config(bg="white")
root.title("Py-Translator")
#-------------------------------------------------------
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
style.configure('TButton', font = 
               ('calibri',23),  
                    borderwidth = '1')
#------------------------------
LANGUAGES = {
    'af': 'afrikaans',    'sq': 'albanian',    'am': 'amharic',    'ar': 'arabic',    'hy': 'armenian',
    'az': 'azerbaijani',    'eu': 'basque',    'be': 'belarusian',    'bn': 'bengali',
    'bs': 'bosnian',   'bg': 'bulgarian',    'ca': 'catalan',    'ceb': 'cebuano',
    'ny': 'chichewa',    'zh-cn': 'chinese (simplified)',    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',    'hr': 'croatian',    'cs': 'czech',    'da': 'danish',
    'nl': 'dutch',    'en': 'english',    'eo': 'esperanto',    'et': 'estonian',
    'tl': 'filipino',    'fi': 'finnish',    'fr': 'french',    'fy': 'frisian',
    'gl': 'galician',    'ka': 'georgian',    'de': 'german',    'el': 'greek',
    'gu': 'gujarati',    'ht': 'haitian creole',    'ha': 'hausa',    'haw': 'hawaiian',
    'iw': 'hebrew',    'hi': 'hindi',    'hmn': 'hmong',    'hu': 'hungarian',
    'is': 'icelandic',    'ig': 'igbo',    'id': 'indonesian',    'ga': 'irish',
    'it': 'italian',    'ja': 'japanese',    'jw': 'javanese',    'kn': 'kannada',
    'kk': 'kazakh',    'km': 'khmer',    'ko': 'korean',    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',    'lo': 'lao',    'la': 'latin',    'lv': 'latvian',
    'lt': 'lithuanian',    'lb': 'luxembourgish',    'mk': 'macedonian',   'mg': 'malagasy',
    'ms': 'malay',    'ml': 'malayalam',    'mt': 'maltese',    'mi': 'maori',
    'mr': 'marathi',    'mn': 'mongolian',    'my': 'myanmar (burmese)',    'ne': 'nepali',    'no': 'norwegian',
    'ps': 'pashto',    'fa': 'persian',    'pl': 'polish',    'pt': 'portuguese',
    'pa': 'punjabi',    'ro': 'romanian',    'ru': 'russian',    'sm': 'samoan',
    'gd': 'scots gaelic',    'sr': 'serbian',    'st': 'sesotho',    'sn': 'shona',
    'sd': 'sindhi',    'si': 'sinhala',    'sk': 'slovak',    'sl': 'slovenian',
    'so': 'somali',    'es': 'spanish',    'su': 'sundanese',    'sw': 'swahili',
    'sv': 'swedish',    'tg': 'tajik',    'ta': 'tamil',    'te': 'telugu',
    'th': 'thai',    'tr': 'turkish',    'uk': 'ukrainian',    'ur': 'urdu',
    'uz': 'uzbek',    'vi': 'vietnamese',   'cy': 'welsh',    'xh': 'xhosa',
    'yi': 'yiddish',    'yo': 'yoruba',    'zu': 'zulu',    'fil': 'Filipino',
    'he': 'Hebrew'}
#-------------------------------------------------------------------------------------------------
lang=list(LANGUAGES.values())
show=0
engine = pyttsx3.init()
file=0
def speak(txt,ck):
   global LANGUAGES,file
   LANGCODES = dict(map(reversed, LANGUAGES.items()))   
   if ck==1:
      try:
         from gtts import gTTS
         sp=Label(root,text="wait...",font=('Comic Sans MS',25),bg="white")
         sp.place(x=100,y=440)
         myobj = gTTS(text=txt, lang=LANGCODES[lang[combo.current()]], slow=False) 
         myobj.save(f"welcome{file}.mp3")
         sp.place_forget()
      except:
         messagebox.showinfo("Spam", "you have not installed playsound,pip install gTTS")         
      os.system(f"mpg321 welcome{file}.mp3")
      try:
         from playsound import playsound
         playsound(f'welcome{file}.mp3')
      except:
         messagebox.showinfo("Spam", "you have not installed playsound,pip install playsound")
   else:
      engine.say(txt)
      engine.runAndWait()
   file+=1

def convert(value):
   global LANGUAGES
   trans.delete('1.0','end')
   trans.insert(END,'Translating.....')
   LANGCODES = dict(map(reversed, LANGUAGES.items()))   
   translator = Translator()  # initalize the Translator object   
   translations = translator.translate([value], dest=LANGCODES[lang[combo.current()]])  # translate two phrases to Hindi
   trans.delete('1.0','end')
   for translation in translations:  # print every translation
       trans.insert(END,translation.text)

def Translate():
   global show
   value=trans01.get("1.0",END)
   if value.isspace():
      print("info",messagebox.showinfo("Spam", "No Text"))
   else:      
      if show==0:
         speak02.place(x=10,y=447)
         trans.place(x=10,y=500)
         show=1
         threading.Thread(target=convert,args=(value,)).start()
      else:
         threading.Thread(target=convert,args=(value,)).start()
#--------Author-Rohit Kumar-------------------------------------
         #--------------------------------------------
tit=Label(root,text="py-Translator",font=('Comic Sans MS',30),bg="white")
tit.place(x=210,y=20)

canvas=Canvas(root,width=53,height=58)
canvas.place(x=500,y=20)
profile=PhotoImage(file='trans.png')
canvas.create_image(0,0,anchor=NW,image=profile)
#-----------------------------------------------------
trans=Text(width=45,height=5,insertbackground='red',insertwidth=3,foreground='green',font=('Comic Sans MS', 20))

#---Image-Button--------------------------------------
speak01=Button(root,justify = LEFT,bg="white",
               command=lambda:threading.Thread(target=speak,args=(trans01.get("1.0",END),0)).start())
photo01=PhotoImage(file="speak01.png")
speak01.config(image=photo01,width="48",height="45")
speak01.place(x=10,y=190)

speak02=Button(root,justify = LEFT,bg="black",
               command=lambda:threading.Thread(target=speak,args=(trans.get("1.0",END),1)).start())
photo02=PhotoImage(file="speak02.png")
speak02.config(image=photo02,width="48",height="45")



#-----------------------------------------------------
#-------------------------------------------------------

tr=Label(root,text="English         to",font=('Comic Sans MS',20),bg="white")
tr.place(x=100,y=125)

combo = ttk.Combobox(root,values=lang,font = ("Comic Sans MS", 16))
combo.place(x=400,y=130)
combo.current(37)

T=ttk.Button(text="Translate",command=Translate)
T.place(x=500,y=180)

trans01=Text(width=45,height=5,insertbackground='red',insertwidth=3,foreground='purple',font=('Comic Sans MS', 20))
trans01.place(x=10,y=250)

#-------------------------------------------------------

root.mainloop()
#--------Author-Rohit Kumar-------------------------------------