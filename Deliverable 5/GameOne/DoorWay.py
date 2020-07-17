import pygame
from RoomObjectWrapper import RoomObjectWrapper
import math

class DoorWay:
    def __init__(self, object, destinationRoom, destinationRoomIndex, x, y, cameraLocationX=0, cameraLocationY=0):

        objectWrapper = RoomObjectWrapper(object, x, y)

        self.x = x
        self.y = y
        # x, y
        # negative for if up or left
        # else positive
        vector = [0, 0]

        facing = object.facing
        if(facing=="U"):
            vector = [0, -1]
        elif(facing=="D"):
            vector = [0, 1]
        elif(facing=="L"):
            vector = [-1, 0]
        else:
            vector = [1, 0]

        self.cameraLocationX = x - (math.pow(vector[1], 2)* 250) - (math.pow(vector[0],2)*200)
        self.cameraLocationY = y - (math.pow(vector[0], 2)* 250) - (math.pow(vector[1],2)*200 )

        self.putPlayerX = x + (vector[0]*objectWrapper.object.HitBox.width)
        self.putPlayerY = y + (vector[1]*objectWrapper.object.HitBox.height)

        self.roomObjectWrapper = objectWrapper
        self.destinationRoom = destinationRoom
        self.destinationRoomEntranceIndex = destinationRoomIndex