#Q1

global PlayerNames, PlayerScores

PlayerNames  = ["" for i in range(11)]
PlayerScores  = ["" for i in range(11)]
#PlayerScores = [[""]*2 for i in range(11)] # 2D array

def ReadHighScores():
    txtfile = open("HighScore.txt", "r")
    for item in range(11):
        PlayerNames[item] = txtfile.readline().strip()
        PlayerScores[item] = txtfile.readline().strip()
    txtfile.close()
    

def OutputHighScores():
    for y in range(11):
        print(PlayerNames[y], PlayerScores[y])

def main():
    global UserName, UserScore, PlayerNames, PlayerScores
    ReadHighScores()
    OutputHighScores()
    UserName = input("Please enter a username; [XYZ]: ").upper()
    while len(UserName) != 3:
        UserName = input("Invalid username, please enter a username; [XYZ]").upper()
    UserScore = int(input("Please enter a score; [1 to 100,000 inclusive]: "))
    while UserScore < 1 or UserScore > 100000:
        UserScore = int(input("Invalid score, please enter a score: "))
    
    return UserName, UserScore


def Reorder(player_name, player_score):
    for x in range(10):
        if player_score > int(PlayerScores[x]):
            for y in range(10, x, -1):
                PlayerScores[y] = PlayerScores[y-1]
                PlayerNames[y] = PlayerNames[y-1]
            PlayerScores[x] = player_score
            PlayerNames[x] = player_name
            break
    PlayerNames.pop(len(PlayerNames) - 1)
    PlayerScores.pop(len(PlayerScores) - 1)
    for k in range(10):
        print(PlayerNames[k], PlayerScores[k])


main()    
Reorder(UserName,UserScore)

def WriteTopTen():
    txtfile = open("NewHighScore.txt", "w")
    for item in range(10):
        txtfile.write(PlayerNames[item]+"\n")
        txtfile.write(str(PlayerScores[item])+"\n")
    txtfile.close

WriteTopTen()