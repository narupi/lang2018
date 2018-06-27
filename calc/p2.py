import lexer as L

class Term(object):
    pass


class Add(Term):
    def __init__(self: L.Num, num1:L.Num, num2:L.Num):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "(%s) + (%s)" % (self.num1 , self.num2)

class ParseError(Exception):

'''
def parse(tokens):
    stack = []
    for i in range(len(tokens)):
        if(tokens[i].__class__ == L.Num):
            stack.append(L.Num(tokens[i]))

        elif(type(tokens[i]) == L.Plus):
            stack.append(Add(stack.pop(),stack.pop()))

        else :
            pass

    return stack.pop()

'''
def pase(token):
    next_token, term = term_parser(token)
    if( len(next_token) != 0 ):
        raise ParseError
    
    return term


def add_parser(token):
    

def num_parser:

def symbol_parser(token):

def term_parser:
