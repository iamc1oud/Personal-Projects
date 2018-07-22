# UNDER DEVELOPMENT
import sys
import os, time
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
from tkinter.filedialog import askdirectory
# import pygame
import subprocess
import speech_recognition as sr


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Cloudmax Player'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 450
        self.realnames = []
        self.listofsongs = []
        self.index = 0
        self.initUI()

    def control(self, command):
        if command == 'stop':
            #def playsong():
            subprocess.call(["mpg123",self.listofsongs[self.index]])
            print("Stopped/Playing")
        if command == 'previous':    
            self.index-=1
            subprocess.call(["mpg123",self.listofsongs[self.index]])
            print("Previous")
        if command == 'next':    
            self.index+=1
            subprocess.call(["mpg123",self.listofsongs[self.index]])
            print("Next")

            
        # TODO : Add a play and stop functionality in single button.
        self.playBtn = QPushButton('Play', self)
        self.playBtn.setToolTip('Play song')
        self.playBtn.move(110,400)
        #self.playBtn.clicked.connect(playsong)

        self.prevBtn = QPushButton('Previous', self)
        self.prevBtn.setToolTip('Previous song')
        self.prevBtn.move(20 ,400)
        #self.prevBtn.clicked.connect(prevsong)

        self.nextBtn = QPushButton('Next', self)
        self.nextBtn.setToolTip('Next song')
        self.nextBtn.move(210,400)
        #self.nextBtn.clicked.connect(nextsong)
    
    # choose the directory which has songs.
    def directorychooser(self):
        directory = askdirectory()
        print(directory)
        # Extract all mp3 songs from directory
        for files in os.listdir(directory):
            if files.endswith('.mp3'):
                self.listofsongs.append(files)
                print(self.listofsongs)

    def SpeechRecognizer(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    print('Say something...')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    if('next' in command):
                        self.control('next')
                        print('You said next...')
                    elif('previous' in command):
                        self.control('previous')
                        print('You said previous...')
                    elif('stop' in command):
                        self.control('stop')
                        print('Stop song activated.')
                    elif('play' in command):
                        self.control('stop')
                        print('Stop song activated.')
                    
                    time.sleep(2.3)
                except sr.UnknownValueError:
                    print('Google speech recignition could not understand audio')
                except sr.RequestError:
                    print('Could not request result due to network error.')

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.directorychooser()
        self.SpeechRecognizer()
        self.show()
       
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
    
