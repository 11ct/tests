#Q2

class Balloon():
    def __init__(self, DefenceItem, Colour):
        self.__Health = 100
        self.__DefenceItem = DefenceItem
        self.__Colour = Colour

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, n):
        self.__Health += n

    def CheckHealth(self):
        if self.__Health < 1:
            return True
        return False
    
def Defend(UserBalloon):
    Strength = int(input("Enter the opponent's strength: "))
    UserBalloon.ChangeHealth(-Strength)
    UserBalloon.ChangeHealth
    print(f"You defended with{str(UserBalloon.GetDefenceItem())}")
    if UserBalloon.CheckHealth():
        print("You lost the game")
    else:
        print("You won the game")
    return UserBalloon
    
UserDefence = input("Please enter a defence item.")
UserColour = input("Please enter a colour.")
Balloon1= Balloon(UserDefence, UserColour)    

