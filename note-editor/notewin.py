from Tkinter import *
import platform
import theme

class MainUI(Frame):
    '''
    'sl' is short for showline
    default font: monaco-13
    '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.sysstr = platform.system()
        #create main menu
        self.menubar = Menu(parent)
        self.attribute = {'font':('Monaco', 13), 'bg':"#1B1D1E", 'fg':"#F8F8F2", 'sl':False}
        if self.sysstr == "Linux":
            print "Linux System"
            self.attribute['font'] = ('Monaco', 13)
        elif self.sysstr == "Windows":
            #TODO: add system specific sttribute configuration
            self.attribute['font'] = ('Simsun', 13)
        else:
            self.attribute['font'] = ('Monaco', 13)
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
        self.text = Text(font = self.attribute['font'], bg=self.attribute['bg'], fg=self.attribute['fg'], insertwidth=1, insertbackground="#f0f0f0", tabs='1c')
        self.linbar = Label(font = self.attribute['font'], width=4)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)
        theme.init(self.text)
        self.line = 1
        self.column = 0

        # bind keys
        self.text.bind("<Control-a>", self.sel_all)
        self.text.bind("<Control-s>", self.save)
        self.filecontent = None

    '''
    binding functions
    '''
    def sel_all(self, event):
        print event.keysym
        if self.filecontent != None:
            #self.text.get(1.0, END)
            self.selected = True
            self.text['bg'] = '#a0a0a0'

    def save(self, event):
        if self.fname == "default.txt":
            self.fname = tkFileDialog.asksaveasfilename(initialdir = os.getcwd())
            if not self.fname:
                self.fname = "default.txt"
        print "Saving file to %s" %(self.fname)
        txtContent = self.text.get(1.0, END)  
        self.saveFile(content = txtContent) 
        
    def ShowLineNum(self):
        self.linenum = 1.0
        self.filecontent = self.text.get(1.0, END).split('\n')
        for line in self.filecontent:
            if self.attribute['sl'] is False:
                self.linbar.pack(side = LEFT, fill = Y, expand = YES)
                '''
                self.strNum = str(int(self.linenum))
                for i in range(4-len(str(int(self.linenum)))):
                    self.strNum = '0'+self.strNum 
                self.text.insert(self.linenum, self.strNum, 'bg')
                self.text.insert(INSERT, '  '+line+'\n')
                '''
                self.linbar["text"] += str(int(self.linenum))+'\n'
            else:
                self.linbar.forget()
                self.text.insert(self.linenum, line)
            self.linenum += 1
        self.attribute['sl'] = not self.attribute['sl']
    
    def open(self):
        self.fname = tkFileDialog.askopenfilename(initialdir = os.getcwd())
        if len(self.fname) == 0:
            return
        if self.filecontent != None:
            self.text.delete(1.0, END)
        self.filecontent = self.openFile(fname = self.fname)
        self.linenum = 1.0
        if self.filecontent is not None:
            for line in self.filecontent:
                self.text.insert(self.linenum, line.decode('utf8'))
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
