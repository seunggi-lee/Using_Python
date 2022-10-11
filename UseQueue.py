# from queue import Queue
#
# que1 = Queue()
# que2 = Queue()
# que1.put(0)
# que1.put(1)
# que1.put(2)
#
# for i in range(0, que1.qsize()):
#     print(que1.get())

from queue import Queue
print("Queue Example")

que = Queue()
que.put(1)
que.put(2)
que.put(3)

for i in range(0, que.qsize()):
    print(que.get())

from queue import LifoQueue
print("LifoQueue Example")

que = LifoQueue()
que.put(1)
que.put(2)
que.put(3)

for i in range(0, que.qsize()):
    print(que.get())

from queue import PriorityQueue
print("PriorityQueue Example")

que = PriorityQueue()
que.put((14,'ewqe'))
que.put((23,'qqq'))
que.put((1,'q'))

for i in range(0, que.qsize()):
    print(que.get())
