from GameObject import GameObject

class RoomObjectWrapper:
    def __init__(self, object, xPos, yPos):
        self.object = object

        self.roomXPos = 0
        self.roomYPos = 0
        self.object.HitBox.upperLeft[0] = 0
        self.object.HitBox.upperLeft[1] = 0

        self.changePos(xPos, yPos)

    def changePos(self, xChange, yChange):
        self.roomXPos += xChange
        self.roomYPos += yChange
        self.object.HitBox.upperLeft[0] = self.roomXPos
        self.object.HitBox.upperLeft[1] = self.roomYPos

    def draw(self, controller, baseX=0, baseY=0):
        self.object.drawSelf(self.roomXPos, self.roomYPos, controller)
