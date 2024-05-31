from tkinter import *
from pytube import YouTube

def downloader():
    try:
        url = YouTube(link.get())
        video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download()
        status_label.config(text='DOWNLOADED')
    except Exception as e:
        status_label.config(text='Error during download')

# GUI setup
program = Tk()
program.geometry('500x300')
program.resizable(0, 0)
program.title("YouTube Video Downloader")

Label(program, text='YouTube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(program, text='Put the link:', font='arial 15 bold').place(x=160, y=60)
Entry(program, width=70, textvariable=link).place(x=32, y=90)

Button(program, text='DOWNLOAD', font='arial 15 bold', bg='white', padx=2, command=downloader).place(x=160, y=150)

status_label = Label(program, text='', font='arial 15', bg='white')
status_label.place(x=150, y=210)

program.mainloop()
