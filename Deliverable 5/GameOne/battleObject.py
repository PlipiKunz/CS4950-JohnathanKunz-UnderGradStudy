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
        pass

    def respondInteract(self, turn, option):
        pass

