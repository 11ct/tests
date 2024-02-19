global Queue, HeadPointer, TailPointer
Queue = [" " for i in range(50)] #Stores 50 IDs of type STRING
HeadPointer = -1
TailPointer = 0


def Enqueue(IDs):
    global HeadPointer
    global TailPointer
    global Queue
    if HeadPointer == 49:
        print("Queue is full")
        return False
    Queue[TailPointer] = IDs
    if TailPointer >= 49:
        TailPointer = 0
    else:
        TailPointer += 1
    HeadPointer += 1
    return True

def Dequeue():
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

def ReadData():
    f = open("QueueData.txt", "r")
    for i in range(50):
        Data = f.readline().strip()
        Enqueue(Data)
    f.close()

class RecordData:
    def __init__(self, ID, Total):
        self.ID = ID #String to store game ID
        self.Total = Total #Total number of times a game ID appears in the text file

global NumberRecords
Records = [] #Stores up to 50 items of type RecordData
NumberRecords = 0 #Stoes the number currently in the array Records

def TotalData():
    global Records
    global NumberRecords
    global Flag
    Flag = True
    DataAccessed = Dequeue()
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords-1):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
                break
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

def OutputRecords():
    global Records
    global NumberRecords
    for x in range(0, NumberRecords):
        print(f"ID {Records[x].ID} Total {Records[x].Total}")

ReadData()
TotalData()
OutputRecords()