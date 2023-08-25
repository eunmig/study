# enQueue(item)
def enQ(data):
    global rear
    # if rear == Qsize-1:    # 가득 차면
    #     print('Q is Full')
    # else:
        rear += 1
        Q[rear] = data

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)
rear += 1       #enqueue(3)
Q[rear] = 3
enQ(3)


# deQueue()
def deQ():
    global front
    # if front == rear:   # 비어있으면
    #     print('Q가 비어있음')
    #     return
    # else:
        front += 1
        return Q[front]

enQ(1)
enQ(2)
enQ(3)
front += 1
tmp = Q[front]

#
Q = []
Q.append(1)     # enqueue(3)
Q.append(2)
Q.append(3)
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))