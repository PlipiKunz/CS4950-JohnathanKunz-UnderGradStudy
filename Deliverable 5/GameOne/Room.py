import pygame

class Room:
    def __init__(self, roomSprite, roomNumber, entrances, entities):
        self.roomSprite = roomSprite
        self.roomNumber = roomNumber
        self.entrances = entrances
        self.entities = entities

        self.baseX = 0
        self.baseY = 0



