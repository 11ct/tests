#DECLARE TheData: ARRAY OF STRING
TheData = [20, 3, 4, 8, 12, 99, 4, 24, 4]

def InsertionSort(TheData):
    FirstElement = 0
    for Count in range(FirstElement,len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue+1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1

def OutputData(TheData):
    for i in range(len(TheData)):
        print(TheData[i], end=" ")

print("Before sorting: ")
OutputData(TheData)
InsertionSort(TheData)
print("\nAfter sorting: ")
OutputData(TheData)

def Found(TheData):
    UserInput = int(input("Please enter a number: "))
    if UserInput in TheData:
        print("Found")
        return True
    else:
        print("Not Found")
        return False
Found(TheData)