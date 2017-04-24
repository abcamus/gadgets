#--coding:utf-8 --


__version__ = 0.1
__author__ = {'name' : 'Albert Camus',
              'Email' : 'abcamus_dev@163.com',
              'Blog' : '',
              'QQ' : '',
              'Created' : ''}


from json.decoder import errmsg
import sys, tkFileDialog, os
import platform
import timer
import theme
from notewin import *

class Note():
    def __init__(self):
        self.tk = Tk()
        self.tk.title('宙斯的神殿')
        self.tk.after(500, self.updateTime)
        self.cur_idx = 1.0
        self.cur_pos = '1.0'
        #self.tk.iconbitmap('icons/48x48.ico')
    
        self.has_sub = False
        self.createUI()
        self.tk.bind('<Control-q>', self.bind_exit)
        self.tk.mainloop()

    def bind_exit(self, event):
        self.tk.destroy()

    def updateTime(self):
        import time
        time.strftime("%H:%M:%S")
        text = self.MainText.text
        if text.edit_modified():
            print "Text Modified"
            #TODO: timer handler
            self.insert = INSERT
            theme.parse(text, text.get(self.cur_pos, self.insert))
            self.cur_pos = text.index(INSERT)
            print "current pos = %s" %(self.cur_pos)
            text.edit_modified(False)
        self.tk.after(500, self.updateTime)
    
    def popup(self, event):
        self.submenubar.post(event.x_root, event.y_root)
    
    def SubOpen(self):
        self.subfilename = tkFileDialog.askopenfilename(initialdir = os.getcwd())
        self.filecontent = self.MainText.openFile(fname = self.subfilename)
        if self.filecontent is not None:
            self.MainText.SubText.delete(1.0, END)
            self.linenum = 1.0
            for eachline in self.filecontent:
                self.MainText.SubText.insert(self.linenum, eachline.decode('utf-8'))
                self.linenum += 1
    
    def CreateSubWin(self):
        if self.has_sub is True:
            # hide the sub window
            self.MainText.SubText.forget()
            self.has_sub = False
        else:
            self.has_sub = True
            self.MainText.text.pack(side=LEFT, fill=BOTH)
            self.MainText.SubText.pack(side=RIGHT, anchor=NW)
        
    def createUI(self):
        #create main menu
        self.MainText = MainUI(self.tk)

        # special for sub window editor
        '''
        self.MainText.SubText = Text(self.MainText.text, bg = 'green')
        self.MainText.menubar.add_command(label = 'subwin', command = self.CreateSubWin)
        self.submenubar = Menu(self.MainText.menubar)
        self.submenubar.add_command(label = 'open', command = self.SubOpen)
        self.tk.bind('<Button-3>', self.popup)
        '''

if __name__ == '__main__':  
    #timer.start()
    Note()
