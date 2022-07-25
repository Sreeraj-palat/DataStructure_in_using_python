#implement stack using list

from secrets import choice


stack = []

def push():
    element = input('Enter the element')
    stack.append(element)
    print(stack)

def popElement():
    if not stack:
        print('stack is empty')
    else:
        e = stack.pop()
        print('removed element :', e)
        print(stack)

while True:
    print('select 1 - for Push \n 2 for pop \n 3 for Exit')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        popElement()
    elif choice == 3:
        break;
    else:
        print('Enter the correct option')



