global arrayData
arrayData = [10,5,6,7,1,12,13,15,21,8]
Searchvalue = int(input("Please enter a value to search: "))


def linearSearch(array, value):
    for x in range(0, len(array)):
        if array[x] == value:
            print("The value was found.")
            return True
    print("The value was not found.")
    return False

linearSearch(arrayData, Searchvalue)


def bubbleSort(theArray):
    temp = 0
    for x in range(0, len(theArray)):
        for y in range(0, len(theArray)-x-1):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp

bubbleSort(arrayData)
for u in range(0, len(arrayData)):
    print(arrayData[u])