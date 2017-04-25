class token():
    def __init__(self):
        self.type = None
        self.content = ''

class lexer():
    def __init__(self, content):
        self.cur_token = token()
        self.string = content
        self.cur_idx = 0
        self.cur_ch = self.string[self.cur_idx]

    def get_next_ch(self):
        if self.cur_idx >= len(self.string)-1:
            return None
        else:
            self.cur_idx += 1
            self.cur_ch = self.string[self.cur_idx]
    
    def eat(self, type):
        if type == 'Number':
            while self.cur_ch.isdigit():
                self.cur_token.content += self.cur_ch
                self.get_next_ch()
        self.cur_token.type = type

    def skip_whitespace():
        while cur_ch == ' ':
            self.get_next_ch()

    def get_next_token(self):
        if self.cur_ch.isdigit():
            self.eat('Number')
        return (self.cur_token, self.string[self.cur_idx:-1])

def get_token(content):
    mylexer = lexer(content)
    return mylexer.get_next_token()

def parse(text, string):
    print string
