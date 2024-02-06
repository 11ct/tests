#Q3

global NumOfItems
global HeadPointer
global TailPointer
global QueueArray
QueueArray = [" " for i in range(10)]
HeadPointer = 0
TailPointer = 0
NumOfItems = 0

def Enqueue(DTA):
    global NumOfItems
    global HeadPointer
    global TailPointer
    global QueueArray
    if NumOfItems == 10:
        print("Queue is full")
        return False
    QueueArray[TailPointer] = DTA
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumOfItems += 1
    return True

def Dequeue():
    global NumOfItems
    global HeadPointer
    global TailPointer
    global QueueArray
    
    if NumOfItems == 0:
        print("Queue is empty")
        return False
    else:
        DTR = QueueArray[HeadPointer]
        HeadPointer += 1
        if HeadPointer >= 9:
            HeadPointer = 0
        NumOfItems -= 1
        return DTR


for x in range(11):
    UserInput = input("Pleease enter a string value: ")
    if Enqueue(UserInput):
        print("Enqueue was successful")
    else:
        print("Enqueue was not successful")
for y in range(2):
    print(Dequeue())
    
