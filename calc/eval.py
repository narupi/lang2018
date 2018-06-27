import parser as P
import lexer as L

def eval_term(term):
    if(term.__class__ == L.Num):
        ret = str(term.value)
        return int(ret)
    
    elif(term.__class__ == P.Add):
        return eval_term(term.num1) + eval_term(term.num2)

    else:
        pass


