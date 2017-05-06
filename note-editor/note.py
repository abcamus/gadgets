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
        self.cur_idx = 1
        self.cur_pos = '1.0'
        #self.tk.iconbitmap('icons/48x48.ico')
    
        self.has_sub = False
        self.createUI()
        self.tk.bind('<Control-q>', self.bind_exit)
        self.tk.mainloop()

    def bind_exit(self, event):
        self.tk.destroy()

    def updateTime(self):
        import parser
        main = self.MainText
        text = main.text
        cur_lineNum = len(text.get('1.0', END).split('\n'))-1
        StartLine = int(cur_lineNum*text.yview()[0])
        EndLine = int(cur_lineNum*text.yview()[1])
        #print text.yview()
        #print main.scrollbar.get()
        #print "Total Line = %d" %(main.TotalTextLine)
        main.linbar['text'] = ''
        for i in range(StartLine, EndLine):
            main.linbar['text'] += str(i+1)+'\n'
        if text.edit_modified():
            #print text.index(END)
            text.edit_modified(False)
            string = text.get('1.0', INSERT)
            parser.parse(main, string)
            #main.update_line_col()
        self.tk.after(100, self.updateTime)
            
    def createUI(self):
        #create main menu
        self.tk.Frame = Frame(height=720, width=1280)
        self.tk.Frame.pack()
        self.tk.Frame.pack_propagate(0)
        self.MainText = MainUI(self.tk)

if __name__ == '__main__':  
    #timer.start()
    Note()
