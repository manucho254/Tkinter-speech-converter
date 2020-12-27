import os
from gtts import gTTS
from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
import time 


root = Tk()

root.title("Convert text to speech")

root.geometry('530x300')
root.resizable(width=0, height=0)
   
label = Label(root, text = "Text And Speach Converter",  
              font = "bold, 30", 
              bg = "green", fg="white" , padx=6, pady=13,
              )
label.grid(row=0,columnspan=3, padx=10, pady=10)

entry = Entry(root, width = 45,  
              bd = 6, font = 14, borderwidth=6) 
entry.grid(row=1, column=1, columnspan=1, padx=10, pady=13)

# text to audio conversion function
def text_to_audio():

    language = 'en'


    try:
        myaudio = gTTS(
        text=entry.get(),
        lang=language,
        slow=False
        )
    except:
        messagebox.showerror("error", "text missing")
    myaudio.save('simp.mp3')
    os.system('start simp.mp3')


w = Message(root, text="this is a message")


# sound to text conversion function
def Sound_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        try:
            audio_data = r.record(source, duration=4)
            text = r.recognize_google(audio_data)
            with open("speech.txt", "a") as pin:
                pin.write(text + "\n")
        except:
            messagebox.showerror("error", "try again")

# exit the progarm function
def button_exit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
    return

button_text = Button(root, text="CONVERT TEXT" ,
    padx=30 , pady=10 , 
    bg = 'green',fg="white",command=text_to_audio 
    )
w = Message(root, text="this is a message")
button_text.place(x = 100,  
          y = 180)

button_sound = Button(
     root, text="SPEAK" ,
    padx=30 , pady=10 , 
    bg = 'green', fg="white",command= Sound_to_text
    )

button_sound.place(x = 300,  
          y = 180)

button_exit = Button(
    root, text="Exit" ,
    padx=30, pady=10, 
    bg = 'red', command=button_exit
    )

button_exit.place(x = 220,
          y = 250)

root.mainloop()
