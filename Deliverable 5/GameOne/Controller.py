import pygame
from Room import Room
from RoomObjectWrapper import RoomObjectWrapper

from Characters import MainCharacter
from Rooms.RoomZero import Room0
from Rooms.RoomOne import  RoomOne


class Controller:
    def __init__(self):
        pygame.init()
        self.windowWidth = 500
        self.windowHeight = 500
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Game One")

        self.rooms = [Room0(), RoomOne()]
        self.flags = []
        self.currentRoomIndex = 1

        mainCharChar = MainCharacter.MainCharacter()
        self.mainCharacter = RoomObjectWrapper(mainCharChar, 0, 0)

        self.bufferLowerX = 200
        self.bufferUpperX = 225
        self.bufferLowerY = 200
        self.bufferUpperY = 225

        self.velocity = 5
        # mode 0 for noraml, 1 for battle
        self.mode = 0

        self.run = True

    def main(self):
        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.mode == 0:
                self.mode0Code()

        pygame.quit()

    def updateScreen(self):
        if self.mode == 0:
            curRoom = self.rooms[self.currentRoomIndex]
            curRoom.placeEntities(self)

            self.mainCharacter.draw(self)
            pygame.display.update()

    def scanIn(self):
        pass

    def saveState(self):
        pass

    def displayTextBox(self, spr, content, speed, noise, font):
        pass

    def changeRoom(self, roomNum, doorwayNum):
        # resets the rooms x and y just in case
        self.rooms[self.currentRoomIndex].baseX = 0
        self.rooms[self.currentRoomIndex].baseY = 0

        self.currentRoomIndex = roomNum
        room = self.rooms[self.currentRoomIndex]

        room.baseX = -room.entrances[doorwayNum].ownHitbox.lowerRight[0]
        room.baseY = -room.entrances[doorwayNum].ownHitbox.upperLeft[1]

    def changeToBattleRoom(self, enemy, conditions):
        pass


    def mode0Code(self):
        curRoom = self.rooms[self.currentRoomIndex]

        x = self.mainCharacter.roomXPos
        y = self.mainCharacter.roomYPos
        charCenteredX = (x > self.bufferLowerX) and (x < self.bufferUpperX)
        charCenteredY = (y > self.bufferLowerY) and (y < self.bufferUpperY)

        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_SPACE]:
            self.velocity = 10

        if keyPressed[pygame.K_BACKSLASH]:
            curRoom.reset()
            self.currentRoomIndex = (self.currentRoomIndex + 1) % self.rooms.__len__()
            print(self.currentRoomIndex)

        distanceCheck = self.velocity * 2

        if keyPressed[pygame.K_LEFT]:
            self.mainCharacter.object.facing = "L"

            self.mainCharacter.changePos(-distanceCheck, 0)
            if(curRoom.entityCollisionCheck(self)):
                if curRoom.baseX <= -self.velocity and charCenteredX:
                    curRoom.moveRoom(self.velocity,0)
                elif self.mainCharacter.roomXPos >= self.velocity:
                    self.mainCharacter.changePos(-self.velocity, 0)
            self.mainCharacter.changePos(distanceCheck, 0)

        if keyPressed[pygame.K_RIGHT]:
            self.mainCharacter.object.facing = "R"

            self.mainCharacter.changePos(distanceCheck, 0)
            if (curRoom.entityCollisionCheck(self)):
                if (curRoom.baseX + curRoom.width - self.windowWidth) >= self.velocity and charCenteredX:
                    curRoom.moveRoom(-self.velocity,0)
                elif self.mainCharacter.roomXPos <= self.windowWidth - self.velocity - self.mainCharacter.object.getWidth():
                    self.mainCharacter.changePos(self.velocity, 0)
            self.mainCharacter.changePos(-distanceCheck, 0)

        if keyPressed[pygame.K_UP]:
            self.mainCharacter.object.facing = "U"

            self.mainCharacter.changePos(0, -distanceCheck)
            if (curRoom.entityCollisionCheck(self)):
                if curRoom.baseY <= -self.velocity and charCenteredY:
                    curRoom.moveRoom(0,self.velocity)
                elif self.mainCharacter.roomYPos >= self.velocity:
                    self.mainCharacter.changePos(0, -self.velocity)
            self.mainCharacter.changePos(0, distanceCheck)

        if keyPressed[pygame.K_DOWN]:
            self.mainCharacter.object.facing = "D"

            self.mainCharacter.changePos(0, distanceCheck)
            if (curRoom.entityCollisionCheck(self)):
                if (curRoom.baseY + curRoom.height - self.windowHeight) >= self.velocity and charCenteredY:
                    curRoom.moveRoom(0,-self.velocity)
                elif self.mainCharacter.roomYPos <= self.windowHeight - self.velocity - self.mainCharacter.object.getHeight():
                    self.mainCharacter.changePos(0, self.velocity)
            self.mainCharacter.changePos(0, - distanceCheck)

        self.velocity = 5
        curRoom.doorwayCollisionCheck(self)
        self.updateScreen()
