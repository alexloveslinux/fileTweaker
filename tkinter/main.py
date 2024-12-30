from tkinter import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from tkinter import ttk
from os import *
from shutil import *

fn = [('All files', '*.*')]

def createfile():
    fd.asksaveasfile(mode='x', filetypes=fn, defaultextension=fn)

def modifyfile():
    modifyfile = fd.askopenfile(mode='r+', filetypes=fn, defaultextension=fn)
    edit = sd.askstring('Edit', 'Enter text to add:')
    modifyfile.write(edit)

def deletefile():
    deletefile = fd.askopenfile(filetypes=fn, defaultextension=fn)
    deletefile.close()
    remove(deletefile.name)

def readfile():
    readfile = fd.askopenfile(mode='r', filetypes=fn, defaultextension=fn)
    mb.showinfo('File content', readfile.read())

root = Tk()
root.title('PWK')
root.geometry('200x200')
root.resizable(False, False)
create = ttk.Button(root, text='Create file', command=createfile)
create.pack(pady=10)
modify = ttk.Button(root, text='Modify file', command=modifyfile)
modify.pack(pady=10)
delete = ttk.Button(root, text='Delete file', command=deletefile)
delete.pack(pady=10)
readbtn = ttk.Button(root, text='Read file', command=readfile)
readbtn.pack(pady=10)
root.mainloop()