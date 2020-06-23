import pygame
from Room import Room


class Room0(Room):
    def __init__(self):
        sprite = [pygame.transform.scale(pygame.image.load('Images\\Bliss_(Windows_XP).png'), (700,700))]
        roomNum = 0
        entrances = []
        entities = []
        roomWidth = sprite[0].get_width()
        print(roomWidth)
        roomHeight = sprite[0].get_height()
        super().__init__(sprite, roomNum, entrances, entities, roomWidth, roomHeight)

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        controller.screen.fill((0,0,0))
        controller.screen.blit(self.roomSprite[0], (self.baseX, self.baseY))
