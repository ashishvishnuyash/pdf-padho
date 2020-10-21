
# AUTHER aashish kumar shyam bihari sudhama upadhyay(VISHNU RAJ CYWAR)
from tkinter import *
import pyttsx3
import PyPDF2
from tkinter import filedialog

root=Tk()
root.minsize(400,200)
root.maxsize(400,200)
var = IntVar()
def f():
    pop=var.get()
    po=pop-1
    b = filedialog.askopenfile(mode='rb')

    pdfReader = PyPDF2.PdfFileReader(b)
    pages = pdfReader.numPages


    speaker = pyttsx3.init()
    for num in range(po, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        newVoiceRate = 145
        speaker.setProperty('rate', newVoiceRate)
        speaker.say(text)
        speaker.runAndWait()

if __name__ == '__main__':
    x=Label(text='BOOK READER',fg='black',font=("Algerian",19,"bold"),padx=100,pady=10,borderwidth=3)
    x.grid(row=1,column=1)
    l=Label(text='select page no.')
    l.grid(row=3,column=1)
    p=Entry(root,textvariable=var)
    p.grid(row=4,column=1)

    b=Button(root,text='SELECT PDF',command=f)
    b.grid(row=5,column=1)
    root.mainloop()


