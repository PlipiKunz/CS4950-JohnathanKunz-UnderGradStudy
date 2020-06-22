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

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        print("SHOULDNTBEHERE placeEntities room")
        pass

    def entityCollisionCheck(self):
        print("SHOULDNTBEHERE entityCollisionCheck room")
        pass

    def doorwayCollisionCheck(self):
        print("SHOULDNTBEHERE doorWayCollisionCheck room")
        pass


