import os
global QueueData
global StartPointer
global EndPointer
QueueData = [" " for i in range(0, 20)] 
StartPointer = 0
EndPointer = 0

def Enqueue(DTA, EndPointer):
    global QueueData
    global StartPointer
    if EndPointer == 20:
        return False, EndPointer
    else:
        QueueData[EndPointer] = DTA
        EndPointer += 1
        return True, EndPointer

def ReadFile(QueueData, EndPointer):
    UserChoice = input("Please enter a filename: ")
    if os.path.isfile(UserChoice):
        f = open(UserChoice, "r")
        Flag = True
        DTA = f.readline().strip()
        while Flag == True and DTA != "":
            Flag, EndPointer = Enqueue(QueueData, EndPointer)
            DTA = f.readline().strip()
        f.close()
        if Flag == False:
            return 1, EndPointer
        else:
            return 2, EndPointer
    else:
        return -1, EndPointer

ReturnValue, EndPointer = ReadFile(QueueData, EndPointer)
if ReturnValue == -1:
    print("The text file could not be found. ")
elif ReturnValue == 1:
    print("The queue was full. ")
elif ReturnValue == 2:
    print("All items were added to the queue. ")

def Remove(QueueData, StartPointer, EndPointer):
    if (EndPointer - StartPointer) < 2:
        return "No items", StartPointer, EndPointer
    else:
        FirstItem = QueueData[StartPointer]
        StartPointer += 1
        SecondItem = QueueData[StartPointer]
        StartPointer += 1
        return (FirstItem + " " + SecondItem), StartPointer, EndPointer
Remove(QueueData, StartPointer, EndPointer)
