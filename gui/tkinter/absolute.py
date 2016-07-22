#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we lay out images
using absolute positioning.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

        
    def initUI(self):
      
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")
        
        bard = Image.open("images/bardejov.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
        
        rot = Image.open("images/rotunda.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=400, y=20)        
        
        minc = Image.open("images/mincol.jpg")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=20, y=300)        
              

def main():
  
    root = Tk()
    root.geometry("800x550+100+100")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  