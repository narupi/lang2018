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

    def __init__(self: Num, num1:Num, num2:Num):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "(%s) + (%s)" % (self.num1 , self.num2)

#divide input data
def lexer(source):
    tokenlist = []
    for i in range(len(source)):
        #souce[i] is number
        if(source[i].isdigit()):
            tokenlist.append(Num(int(source[i])))
        #souce[i] is '+'
        elif(source[i] == "+"):
#            print("Plus sitai ne")
            tokenlist.append(Plus())
        else:
            pass
    
    return tokenlist

def parser(tokens):
    stack = []
   # print(tokens)
    for i in range(len(tokens)):
  #  print(type(tokens[i]))
        if(tokens[i].__class__ == Num): 
            #            print("Number")
            stack.append(Num(tokens[i]))
#            print(stack)
        elif(type(tokens[i]) == Plus):
   #       print("Plus stitai ne ")
            stack.append(Add(stack.pop(),stack.pop()))
 #           print(stack)
        else :
            pass

#    print(stack)
    return stack.pop()
'''
def parser(tokens):
    stack = []
    for i in range(len(tokens)):
        if(tokens[i].__class__ == Num):

        elif(type(tokens[i]) == Plus):

        else :
            pass
'''


def eval(term):
    if(term.__class__ == Num):
        #must cast 
        ret = str(term.value)

        return int(ret)

    elif(term.__class__ == Add):
#        print(term.num1)
 #       print(term.num2)
        return eval(term.num1) + eval(term.num2)
#        print("a")
    else :
        pass

def main():
    num = input()
    token = lexer(num)
   # for i in token:
  #      print(str(i))

#    print(str(token))
    stack = parser(token)
#    print("debug")
#debug 
    result = eval(stack)
    print(result)

if __name__ == '__main__':
    main()

