def enq(data):
    global rear
    if (rear + 1)%cQsize == front:
        # front = (front+1)%cQsize
        print('cQ is full')
    else:
        rear = (rear+1)%cQsize
        cQ[rear] = data

def deq():
    global front
    front = (front+1)%cQsize
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
print(deq())    # 1
print(deq())    # 2
enq(4)
print(deq())    # 1
print(deq())    # 2