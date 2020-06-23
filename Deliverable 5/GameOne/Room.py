import pygame

class Room:
    def __init__(self, roomSprite, roomNumber, entrances, entities, roomWidth, roomHeight):
        self.roomSprite = roomSprite
        self.roomNumber = roomNumber
        self.entrances = entrances
        self.entities = entities

        self.width = roomWidth
        self.height = roomHeight

        self.baseX = 0
        self.baseY = 0

    def reset(self):
        self.baseX = 0
        self.baseY = 0

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def moveRoom(self, xDif, yDif,):
        self.baseX += xDif
        self.baseY += yDif


    def placeEntities(self, controller):
        for wrapper in self.entities:
            x = wrapper.roomXPos + self.baseX
            y = wrapper.roomYPos + self.baseY
            wrapper.object.drawSelf(x, y, controller)

    def entityCollisionCheck(self, controller):
        for wrapper in self.entities:
            if (wrapper.object.HitBox.hasCollidedCheck(controller.mainCharacter.object.HitBox, self.baseX, self.baseY)):
                return False

        return True

    def doorwayCollisionCheck(self, controller):
        for door in self.entrances:
            if(door.ownHitBox.hasCollidedCheck(controller.mainCharacter.HitBox)):
                controller.changeRoom(door.destinationRoom, door.destinationRoomIndex)
                break
