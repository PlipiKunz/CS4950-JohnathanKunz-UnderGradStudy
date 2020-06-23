import pygame

from Characters import MainCharacter
from Room import Room
from Characters import SecondChar
from RoomObjectWrapper import RoomObjectWrapper



class RoomOne(Room):
    def __init__(self):
        sprite = [pygame.transform.scale(pygame.image.load('Images\\WigglyTuffs Guild.png'), (700,700))]
        roomNum = 0
        entrances = []
        entities = []
        roomWidth = sprite[0].get_width()
        print(roomWidth)
        roomHeight = sprite[0].get_height()

        secondChar = SecondChar.SecondCharac()
        secondChar2 = RoomObjectWrapper(secondChar, 0,0)
        secondChar2.changePos(300,300)

        entities = [secondChar2]

        super().__init__(sprite, roomNum, entrances, entities, roomWidth, roomHeight)

    def reset(self):
        sprite = [pygame.transform.scale(pygame.image.load('Images\\WigglyTuffs Guild.png'), (700, 700))]
        roomNum = 0
        entrances = []
        entities = []
        roomWidth = sprite[0].get_width()
        print(roomWidth)
        roomHeight = sprite[0].get_height()

        secondChar = SecondChar.SecondCharac()
        secondChar2 = RoomObjectWrapper(secondChar, 0, 0)
        secondChar2.changePos(300, 300)

        entities = [secondChar2]

        super().__init__(sprite, roomNum, entrances, entities, roomWidth, roomHeight)

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        controller.screen.fill((0,0,0))
        controller.screen.blit(self.roomSprite[0], (self.baseX, self.baseY))

        super().placeEntities(controller)

