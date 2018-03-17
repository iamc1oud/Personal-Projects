import tkinter as ttk
import webbrowser
from tkinter import *
import speech_recognition as sr
from pygame import mixer

root = ttk.Tk()

# Main Window
root.title('My Search Engine')
# root.iconbitmap()
root.geometry("470x50")
label1 = ttk.Label(root, text='Query')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1)

btn2 = StringVar()
'''
def buttonClick():
    mixer.init()
    mixer.music.load('chime1.mp3')
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone(as source):
        try:
            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio, key=))
    pass
'''


# Callback() function is passed to the button and gives result in Google results.
def callback():
    """Callback function"""
    if btn2.get() == 'Google':
        webbrowser.open('https://google.com/search?q=' + entry1.get())
    elif btn2.get() == 'DuckDuckGo':
        webbrowser.open('https://duckduckgo.com/?q=' + entry1.get())

    elif btn2.get() == 'Amazon':
        webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + entry1.get())
    elif btn2.get() == 'Youtube':
        webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())


# Get() is called when user enter the Return button
def get(event):
    if btn2.get() == 'Google':
        webbrowser.open('https://google.com/search?q=' + entry1.get())
    elif btn2.get() == 'DuckDuckGo':
        webbrowser.open('https://duckduckgo.com/?q=' + entry1.get())
    elif btn2.get() == 'Amazon':
        webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + entry1.get())
    elif btn2.get() == 'Youtube':
        webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())


# Search button
button1 = ttk.Button(master=root, text='Search', width=10, command=callback, relief=SOLID, borderwidth=2)
button1.grid(row=0, column=2)
entry1.bind('<Return>', get)

# Buttons for different engines
MyButton2 = ttk.Radiobutton(root, text='Google', value='Google', variable=btn2)
MyButton2.grid(row=1, column=0, columnspan=1)
MyButton3 = ttk.Radiobutton(root, text='DuckDuckGo', value='DuckDuckGo', variable=btn2, width=10)
MyButton3.grid(row=1, column=1, columnspan=1)
MyButton4 = ttk.Radiobutton(master=root, text='Amazon', value='Amazon', variable=btn2)
MyButton4.grid(row=1, column=2, columnspan=1)
MyButton5 = ttk.Radiobutton(master=root, text='Youtube', value='Youtube', variable=btn2, width=10)
MyButton5.grid(row=1, column=3, columnspan=1)

entry1.focus()
ttk.mainloop(0)
