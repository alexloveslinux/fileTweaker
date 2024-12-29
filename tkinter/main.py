# Modules
from tkinter import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from os import *
from shutil import *
import os

# Class
class App:
    # Main function
    def __init__(self, root):
        self.root = root
        self.root.title('PWK')
        self.root.geometry('200x100')
        self.copy = Button(self.root, text='Copy', command=self.copy)
        self.copy.pack()
        self.delete = Button(self.root, text='Delete', command=self.delete)
        self.delete.pack()
    # Copy function
    def copy(self):
        filenames = [('All files', '*.*')]
        source = fd.askopenfilename(filetypes=filenames, defaultextension=filenames)
        if source:
            destination_dir = fd.askdirectory()
            if destination_dir:
                destination = os.path.join(destination_dir, os.path.basename(source))
                copy2(source, destination)
    # Delete function
    def delete(self):
        filenames = [('All files', '*.*')]
        deletefile = fd.askopenfilename(filetypes=filenames, defaultextension=filenames)
        if deletefile:
            remove(deletefile)
# Main loop
root = Tk()
app = App(root)
root.mainloop()