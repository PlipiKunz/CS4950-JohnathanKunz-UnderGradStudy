import pygame

from DoorWay import DoorWay
from Objects import Door
from Objects import Cabinet
from Room import Room
from RoomObjectWrapper import RoomObjectWrapper


class Room0(Room):
    def __init__(self):
        self.reset()

    def reset(self):
        sprite = [pygame.transform.scale(pygame.image.load('Images\\Bliss_(Windows_XP).png'), (700, 700))]
        roomNum = 0
        entrances = []
        entities = []
        roomWidth = sprite[0].get_width()
        print(roomWidth)
        roomHeight = sprite[0].get_height()

        doorObject = Door.Door()
        doorObject.facing = "L"
        door1 = DoorWay(doorObject, 1, 0, 625, 0)

        doorObject = Door.Door()
        doorObject.facing = "R"
        door2 = DoorWay(doorObject, 0, 2, 0, roomHeight//2)

        doorObject = Door.Door()
        doorObject.facing = "L"
        door3 = DoorWay(doorObject, 0, 1, 625, roomHeight//2)

        doorObject = Door.Door()
        doorObject.facing = "D"
        door4 = DoorWay(doorObject, 0, 4, roomWidth//2, 0)

        doorObject = Door.Door()
        doorObject.facing = "U"
        door5 = DoorWay(doorObject, 0, 3, roomWidth // 2, 600, )

        entrances = [door1, door2, door3, door4, door5]
        cabinent = Cabinet.Cabinent()

        entities = [RoomObjectWrapper(cabinent, 300, 300)]

        super().__init__(sprite, roomNum, entrances, entities, roomWidth, roomHeight)

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        controller.screen.fill((0,0,0))
        controller.screen.blit(self.roomSprite[0], (self.baseX, self.baseY))

        super().placeEntities(controller)
