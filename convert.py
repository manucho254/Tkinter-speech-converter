import os
from gtts import gTTS
from tkinter import *
import speech_recognition as sr
from tkinter import messagebox


root = Tk()

root.title("Convert text to speech")

frame1 = Frame(root, 
               bg = "grey",  
               height = "150")
root.geometry('400x400')
root.resizable(width=100, height=100)
frame1.pack(fill = X) 
  
  
frame2 = Frame(root,  
               bg = "grey",  
               height = "750")
frame2.pack(fill=X) 

label = Label(frame1, text = "Text And Speach Converter",  
              font = "bold, 30", 
              bg = "cyan" , padx=6, pady=13,
              ) 
  
label.place(x = 100, y = 60) 

entry = Entry(frame2, width = 45,  
              bd = 6, font = 14, borderwidth=6) 
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=13)
entry.place(x = 130, y = 52) 
entry.insert(0, "")

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


button_text = Button(frame2, text="Text Convert" ,
    padx=30 , pady=10 , 
    bg = 'green',command=text_to_audio 
    )
w = Message(root, text="this is a message")
w.pack()
button_text.place(x = 100,  
          y = 130)
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

button_sound = Button(
     frame2, text="SPEAK" ,
    padx=30 , pady=10 , 
    bg = 'blue',command= Sound_to_text
    )

button_sound.place(x = 300,  
          y = 130)

# exit the progarm function
def button_exit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
    return

button_exit = Button(
    frame2, text="Exit" ,
    padx=30, pady=10, 
    bg = 'red', command=button_exit
    )

button_exit.place(x = 500,
          y = 130)

root.mainloop()