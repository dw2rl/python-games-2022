# imports
import tkinter
from tkinter import filedialog


root = tkinter.Tk('Text Editor')
text = tkinter.Text(root)
text.grid()

# save-as function


def saveas():
    t = text.get('1.0', 'end-1c')
    location = filedialog.asksaveasfilename()
    file1 = open(location, 'w+')
    file1.write(t)
    file1.close()


button = tkinter.Button(root, text='Save', command=saveas)
button.grid()

root.mainloop()
