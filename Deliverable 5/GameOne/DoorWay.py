import pygame

class DoorWay:
    def __init__(self, ownHitbox, destinationRoom, destinationRoomIndex):
        self.ownHitBox = ownHitbox
        self.destinationRoom = destinationRoom
        self.destinationRoomEntranceIndex = destinationRoomIndex