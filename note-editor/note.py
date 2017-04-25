#--coding:utf-8 --


__version__ = 0.1
__author__ = {'name' : 'Albert Camus',
              'Email' : 'abcamus_dev@163.com',
              'Blog' : '',
              'QQ' : '',
              'Created' : ''}


from json.decoder import errmsg
import sys, tkFileDialog, os
import timer
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
        import lexer
        text = self.MainText.text
        if text.edit_modified():
            print "Text Modified"
            #TODO: timer handler
            lexer.parse(text, text.get('1.0', INSERT))
            text.edit_modified(False)
        self.tk.after(100, self.updateTime)
            
    def createUI(self):
        #create main menu
        self.MainText = MainUI(self.tk)

if __name__ == '__main__':  
    #timer.start()
    Note()
