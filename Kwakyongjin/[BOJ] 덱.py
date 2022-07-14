from collections import deque
import sys

deque = deque()
n = int(input())
for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push_front':
        deque.appendleft(order[1])
    elif order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif order[0] == 'front': 
        if deque:
            data = deque.popleft()
            deque.appendleft(data)
            print(data)
        else:
            print(-1)
    elif order[0] == 'back': 
        if deque:
            data = deque.pop()
            deque.append(data)
            print(data)
        else:
            print(-1)
