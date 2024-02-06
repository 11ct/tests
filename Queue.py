global Queue, HeadPointer, TailPointer
Queue = [" " for i in range(50)] #Stores 50 IDs of type STRING
HeadPointer = -1
TailPointer = 0

def Enqueue(ID):
    global HeadPointer
    global TailPointer
    global Queue
    if HeadPointer == 49:
        print("Queue is full")
        return False
    Queue[TailPointer] = ID
    if TailPointer >= 49:
        TailPointer = 0
    else:
        TailPointer += 1
    HeadPointer += 1
    return True

def Dequeue(DTR):
    global HeadPointer
    global TailPointer
    global Queue
    if HeadPointer == -1:
        print("Queue is empty")
        return False
    else:
        DTR = Queue[HeadPointer]
        if HeadPointer >= 49:
            HeadPointer = 0
        else:
            HeadPointer += 1
        return DTR


