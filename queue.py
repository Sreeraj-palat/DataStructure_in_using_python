queue = []


def enqueue():
    element = input("enter the element")
    queue.append(element)
    print(element, 'is added to the queue')

def dequeue():
    if not queue:
        print('queue is empty')
    else:
        e = queue.pop(0)
        print('removed element',e)

while True:
    print('\n 1 for add element \n 2 for remove element \n 3 for exit')
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break;
    else:
        print('enter correct option')                              