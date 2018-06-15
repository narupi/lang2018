class Token(object):
    pass

class Term(object):
    pass

class Plus(Token):
    def __str__(self):
        return "Plus"

class Num(Token):
    def __init__(self, value):
        self.value  = value

    def __str__(self):
        return "%s" % self.value

class Add(Term):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "(%s) + (%s)" % (self.num1, self.num2)

#divide input data
def lexer(source):
    tokenlist = []
    for i in range(len(source)):
        #souce[i] is number
        if(source[i].isdigit()):
            tokenlist.append(Num(int(source[i])))
        #souce[i] is '+'
        elif(source[i] == "+"):
            tokenlist.append(Plus)
        else:
            pass
    
    return tokenlist

def parser(tokens):
    stack = []
    for i in range(len(tokens)):
        if(tokens[i].__class__ == Num): 
            stack.append(Num(tokens[i]))
        elif(tokens[i] == "Plus"):
            stack.append(Add(stack,pop(),stack.pop()))
      
    return stack.pop()

def eval(term):
    if(term.__class__ == Add):
        return eval(term.num1) + eval(term.num2)
    elif(term.__class__ == Num):
        return term.value
    else :
        pass

def main():
    num = input()
    token = lexer(num)
    print(token)
    stack = parser(token)
    result = eval(stack)

if __name__ == '__main__':
    main()

