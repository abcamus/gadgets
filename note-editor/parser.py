import platform

'''
This file defines Token class and Lexer class
'''
class Token():
    def __init__(self):
        self.type = None
        self.content = ''
        self.s_line = 1
        self.s_col = 0
        self.e_line = 1
        self.e_col = 0

operation_list = ['+', '-', '*', '/']
def isoperator(char):
    if char in operation_list:
        return True
    else:
        return False

class Lexer():
    '''
    state = 'PROCESS', 'DONE'
    '''
    def __init__(self):
        self.token_list = []
        self.token_num = 0
        self.cur_line = 1
        self.cur_col = 0
        self.systype = platform.system()

    def update_pos(self):
        if self.cur_ch == '\n':
            self.cur_line += 1
        else:
            self.cur_col += 1

    def get_next_char(self):
        if self.cur_idx+1 <= len(self.string)-1:
            self.cur_idx += 1
            self.cur_ch = self.string[self.cur_idx]
            self.update_pos()
        else:
            self.cur_ch = None


    def update_token(self, Found_token):
        if Found_token and self.cur_ch != None:
            (self.token.e_line, self.token.e_col) = self.step_back()
        else:
            (self.token.e_line, self.token.e_col) = (self.cur_line, self.cur_col)
        self.token.end_pos = str(self.token.e_line)+'.'+str(self.token.e_col)

    def step_back(self):
        if self.cur_ch == '\n':
            return (self.cur_line-1, self.cur_col)
        else:
            return (self.cur_line, self.cur_col-1)

    def skip_whitespace(self):
        while self.cur_ch == ' ':
            self.token.content += self.cur_ch
            self.get_next_char()
        self.token.type = 'WhiteSpace'
        # move back the cur_pos
        self.update_token(True)
        # found token
        self.token_list.append(self.token)
        self.new_token()

    def eatID(self):
        self.token.type = 'Identifier'
        while self.cur_ch != None and (self.cur_ch.isalpha() or self.cur_ch.isdigit()):
            self.token.content += self.cur_ch
            self.get_next_char()

        print "cur char = %s" %(self.cur_ch)
        self.update_token(True)
        print "token pos = %s" %(self.token.end_pos)
        self.token_list.append(self.token)
        self.new_token()

    
    def new_token(self):
        self.token = Token()
        self.token.type = None
        self.token.content = ''
        self.token.s_line = self.cur_line
        self.token.s_col = self.cur_col
        self.token.start_pos = str(self.token.s_line)+'.'+str(self.token.s_col)
        print "New token start at: %s" %(self.token.start_pos)

    def update(self, string):
        # parse a new token
        self.cur_line = 1
        self.cur_col = 0
        self.string = string
        self.token_list = []
        self.new_token()
        self.cur_idx = 0
        self.cur_ch = self.string[0]

        while self.cur_ch != None:
            if self.cur_ch == ' ':
                self.skip_whitespace()
            elif self.cur_ch.isalpha():
                self.eatID()
            else:
                print "Unknown type"
        print "Updated"
        
lexer = Lexer()

from Tkinter import *
def parse(main, string):
    text = main.text
    print str(string)
    if len(string) > 0:
        lexer.update(str(string))
    for token in lexer.token_list:
        #text.tag_add(token.type, token.start_pos, token.end_pos)
        print "Token: %s(%s-%s)" %(token.content, token.start_pos, token.end_pos)
