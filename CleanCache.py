'''
This module is used for cleaning cache.
'''

import os

cwd = os.getcwd()
cacheList = []
for dirpath, dirnames, filenames in os.walk(cwd):
    if '__pycache__' in dirnames:
        cachePath = os.path.join(dirpath, '__pycache__')
        cacheList.append(cachePath)

#cleaning the directory before removing it
for directory in cacheList:
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            fullpath = os.path.join(dirpath, filename)
            os.remove(fullpath)
        print('%s cleaned.' % dirpath[len(cwd):]) #this len() function is used for friendly display
        os.rmdir(dirpath)
        print('%s removed.' % dirpath[len(cwd):])

from tkinter.messagebox import showinfo
showinfo('Finished!', 'Cleaning complete!')
