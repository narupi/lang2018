from lexer import lex
from parser import parse
from eval import eval_term

def main():
    num = input()
    token = lex(num)
    stack = parse(token)
    result = eval_term(stack)
    print(result)

if __name__ == '__main__':
    main()
