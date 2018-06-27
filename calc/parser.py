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
    pass

def parse(token):
    next_token, term = term_parser(token)
    #but term 
    if( len(next_token) != 0 ):
        raise ParseError
    
    return term


def add_parser(token):
    #check num
    next_token, t1 = num_parser(token)
    #check  + symbol
    next_token = use_token(next_token, L.Plus)
    #check term
    next_token, t2 = term_parser(next_token)
    return next_token, Add(t1, t2)

def num_parser(token):
    next_token = use_token(token, L.Num)
    return next_token, L.Num(token[0].value)

def use_token(token, cls):
    #can't parse
    if( len(token) == 0 ):
        raise ParseError
    
    elif( token[0].__class__ == cls ):
        #use token[0]
        return token[1:]

    else:
        raise ParseError


def term_parser(token):
    #add term parse
    try:
        return add_parser(token)
    except ParseError:
        #can't parse
        #next num parse
        try:
            return num_parser(token)
        except ParseError:
            #faild parse
            raise ParseError

