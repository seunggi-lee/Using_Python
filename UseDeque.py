from collections import deque

deq = deque()

print(deq)

deq.append(1)
deq.appendleft(2)

print(deq)

deq.appendleft(3)
deq.appendleft(4)
deq.appendleft(5)
deq.appendleft(6)

print(deq)

l = [1,1,1,1,1]

deq.extendleft(l)
print(deq)

for i in range(0, 4):
    print(deq.pop())

print(deq)

for i in range(0, 4):
    print(deq.popleft())
print(deq)

deq.remove(5)
print(deq)

deq.appendleft(3)
deq.appendleft(4)
deq.appendleft(5)
print(deq)
deq.rotate(3)

print(deq)
