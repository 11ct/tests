#Q2
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question #STRING
        self.__answer = answer #INTEGER
        self.__points = points #INTEGER
        

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        if int(self.__answer) == answer:
            return True
        else:
            return False
    
    def getPoints(self, attempts):
        if attempts == 1:
            return (self.__points)
        elif attempts == 2:
            return (self.__points)//2
        elif attempts == 3 or 4:
            return (self.__points)//4
        else:
            return 0

#arrayTreasure[0:4] as TreasureChest
arrayTreasure = []
def readData():
    global arrayTreasure
    try:
        f = open("TreasureChestData.txt", "r")
        for i in range(5):
            questions = f.readline().strip()
            answers = f.readline().strip()
            points = f.readline().strip()
            arrayTreasure.append(TreasureChest(questions, answers, points))
        f.close()
    except IOError:
        print("File not found")       
    return arrayTreasure 


readData()
QNum = int(input("Enter a question number between 1 and 5: "))
if QNum > 0 or QNum < 6:
    attempts = 0
    verify = False
    while verify == False:
        UserAnswer = int(input(arrayTreasure[QNum-1].getQuestion()))
        verify = arrayTreasure[QNum-1].checkAnswer(UserAnswer)
        attempts += 1
    print(int(arrayTreasure[QNum-1].getPoints(attempts)))
