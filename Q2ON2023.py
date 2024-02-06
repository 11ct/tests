#Q2

class Character:
    def __init__(self, Name, XPostion, YPosition):
        self.Name = Name #String
        self.XPosition = XPostion #Integer
        self.YPosition = YPosition #Integer
        
    def GetXPosition(self):
        return self.XPosition

    def SetXPosition(self, x):
        self.XPosition = self.XPosition + x
        if self.XPosition > 10000:
            self.XPosition = 10000
        if self.XPosition < 0:
            self.XPosition = 0

    def GetYPosition(self):
        return self.YPosition

    def SetYPosition(self, y):
        self.YPosition = self.YPosition + y
        if self.YPosition > 10000:
            self.YPosition = 10000
        if self.YPosition < 0:
            self.YPosition = 0
        
    def Move(self, direction):
        match direction:
            case "up":
                self.SetYPosition(10)
            case "down":
                self.SetYPosition(-10)
            case "left":
                self.SetXPosition(-10)
            case "right":
                self.SetXPosition(10)

Jack = Character("Jack", 50, 50)

class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)
    
    def Move(self, direction):
        match direction:
            case "up":
                self.SetYPosition(20)
            case "down":
                self.SetYPosition(-20)
            case "left":
                self.SetXPosition(-20)
            case "right":
                self.SetXPosition(20)

Karla = BikeCharacter("Karla", 100, 50)

UserChoice = input("Please select the character that you would like to move[Jack/Karla]: ").lower()
while UserChoice != "jack" and UserChoice != "karla":
        print("Please enter a valid character")
        UserChoice = input("Please select the character that you would like to move[Jack/Karla]: ").lower()
UserDirection = input("Please select the direction that you would like to move[up/down/left/right]: ").lower()
while UserDirection != "up" and UserDirection != "down" and UserDirection != "left" and UserDirection != "right":
        print("Please enter a valid direction")
        UserDirection = input("Please select the direction that you would like to move[up/down/left/right]: ").lower()
if UserChoice == "jack":
    Jack.Move(UserDirection)
    print(f"Jack's new position is X = {Jack.GetXPosition()}, Y = {Jack.GetYPosition()}")
elif UserChoice == "karla":
    Karla.Move(UserDirection)
    print(f"Karla's new position is X = {Karla.GetXPosition()}, Y = {Karla.GetYPosition()}")
