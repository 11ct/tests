#Q2

class Character:
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        self.CharacterName = CharacterName #String
        self.DateOfBirth = DateOfBirth #String
        self.Intelligence = Intelligence #Float
        self.Speed = Speed #Integer

    def GetIntelligence(self):
        return self.Intelligence
    
    def GetName(self):
        return self.CharacterName
    
    def SetIntelligence(self, value):
        self.Intelligence = self.Intelligence + value
    
    def Learn(self):
        self.Intelligence = self.Intelligence*1.1
    
    def ReturnAge(self, DOB):
        Age = 2023 - int(DOB[0:4])
        return Age
    
FirstCharacter = Character("Royal", "20190701", 70, 30)
FirstCharacter.Learn()
print("First Character's Name:",FirstCharacter.CharacterName,
      "Age:", FirstCharacter.ReturnAge(FirstCharacter.DateOfBirth),
      "Intelligence:", FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed, Element):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.Element = Element #String
    
    def Learn(self, Element):
        if Element == "fire" or "water":
            self.Intelligence = self.Intelligence*1.2
        elif Element == "earth":
            self.Intelligence = self.Intelligence*1.3
        else:
            self.Intelligence = self.Intelligence*1.1

FirstMagic = MagicCharacter("Light", "20180303", 75, 22, "fire")
FirstMagic.Learn("fire")
print("First Magic Character's Name:", FirstMagic.CharacterName,
      "Age:", FirstMagic.ReturnAge(FirstMagic.DateOfBirth),
      "Intelligence:", FirstMagic.GetIntelligence())