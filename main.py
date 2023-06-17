# This is a sample Python script.
import shutil
from  tkinter import *
import os
import time
from datetime import datetime
from pathlib import Path
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def CreateNewDirectories(newDirectoryPath):
    if not os.path.exists(newDirectoryPath):
        os.makedirs(newDirectoryPath)

def formatDate(parrentDirectoryPath, directory):
    creationTime = os.stat(os.path.join(parrentDirectoryPath, directory))
    rawDate = time.ctime(creationTime.st_ctime)
    localDate = datetime.strptime(rawDate, "%a %b %d %H:%M:%S %Y")
    return localDate

def groupFoldersByDate(parrentDirectoryPath):

   for directory in  os.listdir(parrentDirectoryPath):

       localDate = formatDate(parrentDirectoryPath, directory)
       directoryPath = "%s/%s" % (parrentDirectoryPath, directory)
       destinationDirectoryPath = "%s/%d" % (parrentDirectoryPath, localDate.year)
       CreateNewDirectories(destinationDirectoryPath)
       if( not directory.isnumeric()):
            shutil.move(directoryPath, destinationDirectoryPath )



root = Tk()
root.title("sort")
root.geometry('300x300')



btn = Button(root, text = 'Click me !', bd = '5',
                          command = lambda: groupFoldersByDate("C:/Users/Dawid-K/projects"))
btn.pack()
root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
