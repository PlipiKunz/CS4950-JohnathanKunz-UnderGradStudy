from GameObject import GameObject

class RoomObjectWrapper:
    def __init__(self, object, xPos, yPos):
        self.object = object
        self.roomXPos = xPos
        self.roomYPos = yPos

    def draw(self, controller, baseX=0, baseY=0):
        self.object.drawSelf(self.roomXPos - baseX, self.roomYPos - baseY, controller)
