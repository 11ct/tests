def Unknown(x, y):
    if x<y:
        print(x+y)
        return (Unknown(x+1, y)*2)
    elif x == y:
            return 1
    else:
        print(x+y)
        return (Unknown(x-1, y)//2)

print("The parameters are 10 and 15")
print("The result is", Unknown(10,15))

print("The parameters are 10 and 10")
print("The result is", Unknown(10,10))

print("The parameters are 15 and 10")
print("The result is", Unknown(15,10))

def IterativeUnknown(x,y):
    Total = 1
    while x != y:
        print(x+y)
        if x < y:
            x += 1
            Total *= 2
        else:
            x -= 1
            Total = int(Total/2)
    return Total
        
print("The parameters are 10 and 15")
print("The result is", IterativeUnknown(10,15))

print("The parameters are 10 and 10")
print("The result is", IterativeUnknown(10,10))

print("The parameters are 15 and 10")
print("The result is", IterativeUnknown(15,10))