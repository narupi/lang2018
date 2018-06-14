def cal(symbol,a,b):
    if symbol == "+":
        return int(a)+int(b)


por = []

por = list(input().split())

stack = []

for i in por:
    if i.isdigit():
        stack.append(int(i))

    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(cal(i,a,b))

print(stack[0])

