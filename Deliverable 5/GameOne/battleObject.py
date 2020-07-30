class battleObject:
    def __init__(self, sprs, attacks, health, text):
        self.hp = health
        self.attacks = attacks
        self.sprs = sprs
        self.text = text

    def changeHealth(self, amount):
        self.hp += amount

    def getSprite(self, turn):
        return self.sprs[0]

    def getText(self, turn):
        pass

    def getMessage(self, turn):
        pass

    def runAttack(self, turn):
        pass

    def getInteracts(self, turn):
        return ["Add File", "Close Cabinet", "Insult", "Do Nothing"]

    def respondInteract(self, turn, option):
        if(option==0):
            return True, "Thanks, I am happy now"
        elif(option==1):
            return False, "Whoops, shouldnt have left that open"
        elif(option==2):
            return False, "Well arent you lovely, NOT"
        else:
            return False, "Uh, are you gonna do anything?"

