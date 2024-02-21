global ArrayNodes
ArrayNodes = [[-1 for i in range(0,3)] for  j in range(0,20)]

ArrayNodes[0] = [1,20,5]
ArrayNodes[1] = [2,15,-1] 
ArrayNodes[2] = [-1,3,3]
ArrayNodes[3] = [-1,9,4] 
ArrayNodes[4] = [-1,10,-1]
ArrayNodes[5] = [-1,58,-1]
ArrayNodes[6] = [-1,-1,-1]



RootNodes = []

for j in range(len(ArrayNodes)):
    RootNodes.append(ArrayNodes[j][1])

FreeNode = 6
RootPointer = 0

def SearchValue(RootPointer, Value):
    global ArrayNodes
    if RootPointer == -1:
        return -1
    else:
        if ArrayNodes[RootPointer][1] == Value:
            return RootPointer
        else:
            if ArrayNodes[RootPointer][1] == -1:
                return -1
    if ArrayNodes[RootPointer][1] > Value:
        return SearchValue(ArrayNodes[RootPointer][0], Value)
    if ArrayNodes[RootPointer][1] < Value:
        return SearchValue(ArrayNodes[RootPointer][2], Value)

def PostOrder(RootNodes):
    if RootNodes[0] != -1:
        PostOrder(ArrayNodes[RootNodes[0]])
    if RootNodes[2] != -1:
        PostOrder(ArrayNodes[RootNodes[2]])
    print(str(RootNodes[1]))

Result = SearchValue(RootPointer, 15)
if Result == -1:
    print("The value was not found. ")
else:
    print(str(Result), "is the index of the value.")
PostOrder(ArrayNodes[RootPointer])
