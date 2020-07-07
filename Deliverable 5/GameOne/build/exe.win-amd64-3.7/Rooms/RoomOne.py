import pygame
from Room import Room
from Characters import SecondChar
from RoomObjectWrapper import RoomObjectWrapper
from Objects import Door
from DoorWay import DoorWay

class RoomOne(Room):
    def __init__(self):
        self.reset()

    def reset(self):
        sprite = [pygame.transform.scale(pygame.image.load('Images\\WigglyTuffs Guild.png'), (700, 700))]
        roomNum = 1
        entrances = []
        entities = []
        roomWidth = sprite[0].get_width()
        print(roomWidth)
        roomHeight = sprite[0].get_height()

        secondChar = SecondChar.SecondCharac()
        secondChar2 = RoomObjectWrapper(secondChar, 300, 300)
        entities = [secondChar2]

        doorObject = Door.Door()
        doorObject.facing = "R"
        door1 = DoorWay(doorObject, 0, 0, 0, 500)
        entrances = [door1]

        super().__init__(sprite, roomNum, entrances, entities, roomWidth, roomHeight)

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        controller.screen.fill((0,0,0))
        controller.screen.blit(self.roomSprite[0], (self.baseX, self.baseY))

        super().placeEntities(controller)

