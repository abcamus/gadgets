#-*-coding:utf8 -*-


__version__ = 0.1
__author__ = {'name' : 'Albert Camus',
              'Email' : 'abcamus_dev@163.com',
              'Blog' : '',
              'QQ' : '',
              'Created' : ''}


from json.decoder import errmsg
import sys, tkFileDialog, os
from Tkinter import *

class MainUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        #create main menu
        self.menubar = Menu(parent)
        # 'sl' is short for showline
        self.attribute = {'font':'Monaco', 'bg':0x000000, 'sl':False}
        self.fname = 'default.txt'
        # create file menu
        self.fmenu = Menu(self.menubar, tearoff = 0)
        self.fmenu.add_command(label = 'Open', command = self.open)
        #fmenu.add_separator()
        self.fmenu.add_command(label = 'Save', command = self.save)
        self.fmenu.add_command(label = 'Exit', command = self.exit)
        self.menubar.add_cascade(label = "File", menu = self.fmenu)
        
        # create edit menu
        editmenu = Menu(self.menubar, tearoff = 0)
        editmenu.add_command(label = 'line number', command = self.ShowLineNum)
        self.menubar.add_cascade(label = 'Edit', menu = editmenu)
        # create help menu
        helpmenu = Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label = 'About The Author', command = self.aboutAuthor)
        self.menubar.add_cascade(label = 'Help', menu = helpmenu)
        parent['menu'] = self.menubar
        # Text config
        self.text = Text(font = self.attribute['font'])
        self.text.pack(fill = BOTH, expand = YES)
        self.text.tag_config('bg', background='#a0a000')
    
    def save(self):
        txtContent = self.text.get(1.0, END)  
        self.saveFile(content = txtContent) 
        
    def ShowLineNum(self):
        self.linenum = 1.0
        self.text.delete(1.0, END)
        for line in self.filecontent:
            if self.attribute['sl'] is False:
                self.blankets = ''
                for i in range(4-len(str(int(self.linenum)))):
                    self.blankets += ' '
                self.text.insert(self.linenum, str(int(self.linenum))+self.blankets, 'bg')
                self.text.insert(INSERT, ' '+line)
            else:
                self.text.insert(self.linenum, line)
            self.linenum += 1
        self.attribute['sl'] = not self.attribute['sl']
    
    def open(self):
        self.filename = tkFileDialog.askopenfilename(initialdir = os.getcwd())
        self.filecontent = self.openFile(fname = self.filename)
        self.linenum = 1.0
        if self.filecontent is not None:
            for line in self.filecontent:
                self.text.insert(self.linenum, line.decode('gb2312'))
                self.linenum += 1
            
    '''
     The fname is file name with full path  
    ''' 
    def openFile(self, fname = None):
        if fname is None:
            return -1
        self.fname = fname
        try:
            myFile = open(fname, 'r+')
        except IOError, errmsg:
            print 'Open file error:', errmsg
        else:
            content = myFile.readlines()
            myFile.close()
            return content

    def saveFile(self, content = None):  
        if content is None:
            return -1

        myFile = open(self.fname,'w')
        myFile.write(content.encode('gb2312'))
        myFile.flush()
        myFile.close()
        return 0

    def exit(self):
        sys.exit(0)
    
    def printScale(self, text):
        print 'text = ', text
        
    def printItem(self):
        print 'add_separator'
    
    def destroy_ui(self, ui):
        ui.destroy()
        
    def aboutAuthor(self):
        author_ui = Toplevel()
        author_ui.title('About')
        #author_ui.iconbitmap('icons/48x48.ico')
        author_ui.geometry('200x80')
        about_string = Label(author_ui, text = 'Author: Albert Camus')
        confirmButton = Button(author_ui, text = 'Confirm',
                               command = lambda: self.destroy_ui(author_ui))
        about_string.pack()
        confirmButton.pack()

class Note():
    def __init__(self):
        self.tk = Tk()
        self.tk.title('宙斯的神殿')
        #self.tk.iconbitmap('icons/48x48.ico')
    
        #self.tk.geometry('1440x900')
        self.has_sub = False
        self.createUI()
        self.tk.mainloop()
    
    def popup(self, event):
        self.submenubar.post(event.x_root, event.y_root)
    
    def SubOpen(self):
        self.subfilename = tkFileDialog.askopenfilename(initialdir = os.getcwd())
        self.filecontent = self.MainText.openFile(fname = self.subfilename)
        if self.filecontent is not None:
            self.MainText.SubText.delete(1.0, END)
            self.linenum = 1.0
            for eachline in self.filecontent:
                self.MainText.SubText.insert(self.linenum, eachline.decode('gb2312'))
                self.linenum += 1
    
    def CreateSubWin(self):
        if self.has_sub is True:
            # hide the sub window
            self.MainText.SubText.forget()
            self.has_sub = False
        else:
            self.has_sub = True
            self.MainText.SubText.pack(side = 'right', anchor = NW)
        
    def createUI(self):
        #create main menu
        self.MainText = MainUI(self.tk)
        
        # special for sub window editor
        self.MainText.SubText = Text(self.MainText.text, bg = 'green')
        self.MainText.menubar.add_command(label = 'subwin', command = self.CreateSubWin)
        self.submenubar = Menu(self.MainText.menubar)
        self.submenubar.add_command(label = 'open', command = self.SubOpen)
        self.tk.bind('<Button-3>', self.popup)


if __name__ == '__main__':  
    Note()
