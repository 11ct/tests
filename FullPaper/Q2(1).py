class HiddenBox():
    def __init__(self, UserBoxName, UserCreator, UserDateHidden, UserGameLocation):
        self.__BoxName = UserBoxName #String
        self.__Creator = UserCreator #String
        self.__DateHidden = UserDateHidden #String  
        self.__GameLocation = UserGameLocation #String
        self.__LastFinds = [[" " for i in range(0,2)] for j in range(0,10)] #Array
        self.__Active = False #Boolean
    
    def GetBoxName(self):
        return self.__BoxName
    
    def GetGameLocation(self):
        return self.__GameLocation
    

TheBoxes = [HiddenBox(" ", " ", " ", " ") for i in range(0, 10000)]

def NewBox(TheBoxes, BoxCounter):
    BoxName = input("Please enter the name of the box: ")
    Creator = input("Please enter the name of the creator: ")
    DateHidden = input("Please enter the date the box was hidden: ")
    GameLocation = input("Please enter the location of the box: ")
    TheBoxes[BoxCounter] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return (BoxCounter + 1)

NumberOfBoxes = NewBox(TheBoxes, 0)

class PuzzleBox(HiddenBox):
    def __init__(self, UserBoxName, UserCreator, UserDateHidden, UserGameLocation, UserPuzzleText, UserSolution):
        super().__init__(UserBoxName, UserCreator, UserDateHidden, UserGameLocation)
        self.__Puzzle = UserPuzzleText #String
        self.__Solution = UserSolution #String    
    

