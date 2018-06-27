class Token(object):
    pass

class Term(object):
    pass

class Plus(Token):
    def __str__(self):
        return "Plus"

class Num(Token):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "%s" % self.value


def lex(source):
    tokenlist = []
    for i in range(len(source)):
        if(source[i].isdigit()):
            tokenlist.append(Num(int(source[i])))
        elif(source[i] == "+"):
            tokenlist.append(Plus())
        else:
            pass

    return tokenlist
