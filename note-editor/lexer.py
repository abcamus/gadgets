
class Token():
    def __init__(self):
        self.type = None
        self.content = ''
        self.line = 0
        self.col = 0

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
        self.token = Token()
        self.token_list = []
        self.token_num = 0
        self.cur_line = 0
        self.cur_col = 0

    def update(self, char, line, col):
        # parse a new token
        if char.isdigit():
            if self.token.type == None:
                self.token.type = 'Number'
            elif self.token.type == 'Number':
                self.token.content += char
            else:
                token_list.append(self.token)
                self.start_token(char) 
        if isoperator(char):
            self.token.type = 'Operator'
            self.token.content = char
            self.token_list.append(self.token)
            self.new_token(line, col)
        return self.token

    def new_token(self, line, col):
        self.token = Token()
        self.token.type = None
        self.token.content = ''
        self.token.line = line
        self.token.col = col
    
lexer = Lexer()

from Tkinter import *
def parse(main, string):
    text = main.text
    text.delete(main.cur_pos, INSERT)
    main.col += len(string)
    for char in string: 
        lexer.update(char, 1, 0)
        if len(lexer.token_list) == lexer.token_num + 1:
            token = lexer.token_list[-1]
            print token.type, token.content
            text.insert('insert', token.content, token.type)
            lexer.token_num += 1
