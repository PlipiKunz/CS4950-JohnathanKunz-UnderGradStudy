import pygame
from Room import Room
from RoomObjectWrapper import RoomObjectWrapper

from Characters import MainCharacter
from HitBox import HitBox
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
        self.currentRoomIndex = 0

        mainCharChar = MainCharacter.MainCharacter()
        self.mainCharacter = RoomObjectWrapper(mainCharChar, 0, 0)
        self.interactHitBox = self.getInteractHitbox()

        self.bufferLowerX = 200
        self.bufferUpperX = 225
        self.bufferLowerY = 200
        self.bufferUpperY = 225

        self.velocity = 5
        # mode 0 for noraml, 1 for battle
        self.mode = 0

        self.run = True
        self.changeRoomOn = True

    def main(self):
        self.scanIn()

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.mode == 0:
                self.mode0Code()

        self.saveState()
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

    def displayTextBox(self, content, spr=0,  speed=0, noise=0, font=0):
        pass

    def changeRoom(self, roomNum, doorwayNum):
        # resets the room just in case
        self.rooms[self.currentRoomIndex].reset()

        self.currentRoomIndex = roomNum
        room = self.rooms[self.currentRoomIndex]

        doorway = room.entrances[doorwayNum]
        room.baseX = -(doorway.cameraLocationX)
        if(room.baseX - self.windowWidth < - room.width):
            room.baseX = -(room.width - self.windowWidth)
        elif(room.baseX >0):
            room.baseX = 0

        room.baseY = -(doorway.cameraLocationY)
        if((room.baseY - self.windowHeight < -room.width)):
            room.baseY = -(room.height - self.windowHeight)
        elif (room.baseY > 0):
            room.baseY = 0

        self.mainCharacter.roomXPos = doorway.putPlayerX + room.baseX
        self.mainCharacter.roomYPos = doorway.putPlayerY + room.baseY

        self.changeRoomOn = False

    def changeToBattleRoom(self, enemy, conditions):
         pass

    def mode0Code(self):
        curRoom = self.rooms[self.currentRoomIndex]

        x = self.mainCharacter.roomXPos
        y = self.mainCharacter.roomYPos
        charCenteredX = (x > self.bufferLowerX) and (x < self.bufferUpperX)
        charCenteredY = (y > self.bufferLowerY) and (y < self.bufferUpperY)

        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_LSHIFT]:
            self.velocity = 10

        distanceCheck = self.velocity * 1.2

        if keyPressed[pygame.K_LEFT]:
            self.changeRoomOn = True
            self.mainCharacter.object.facing = "L"

            self.mainCharacter.changePos(-distanceCheck, 0)
            if(curRoom.entityCollisionCheck(self)):
                if curRoom.baseX <= -self.velocity and charCenteredX:
                    curRoom.moveRoom(self.velocity,0)
                elif self.mainCharacter.roomXPos >= self.velocity:
                    self.mainCharacter.changePos(-self.velocity, 0)
            self.mainCharacter.changePos(distanceCheck, 0)

        if keyPressed[pygame.K_RIGHT]:
            self.changeRoomOn = True
            self.mainCharacter.object.facing = "R"

            self.mainCharacter.changePos(distanceCheck, 0)
            if (curRoom.entityCollisionCheck(self)):
                if (curRoom.baseX + curRoom.width - self.windowWidth) >= self.velocity and charCenteredX:
                    curRoom.moveRoom(-self.velocity,0)
                elif self.mainCharacter.roomXPos <= self.windowWidth - self.velocity - self.mainCharacter.object.getWidth():
                    self.mainCharacter.changePos(self.velocity, 0)
            self.mainCharacter.changePos(-distanceCheck, 0)

        if keyPressed[pygame.K_UP]:
            self.changeRoomOn = True

            self.mainCharacter.object.facing = "U"

            self.mainCharacter.changePos(0, -distanceCheck)
            if (curRoom.entityCollisionCheck(self)):
                if curRoom.baseY <= -self.velocity and charCenteredY:
                    curRoom.moveRoom(0,self.velocity)
                elif self.mainCharacter.roomYPos >= self.velocity:
                    self.mainCharacter.changePos(0, -self.velocity)
            self.mainCharacter.changePos(0, distanceCheck)

        if keyPressed[pygame.K_DOWN]:
            self.changeRoomOn = True
            self.mainCharacter.object.facing = "D"

            self.mainCharacter.changePos(0, distanceCheck)
            if (curRoom.entityCollisionCheck(self)):
                if (curRoom.baseY + curRoom.height - self.windowHeight) >= self.velocity and charCenteredY:
                    curRoom.moveRoom(0,-self.velocity)
                elif self.mainCharacter.roomYPos <= self.windowHeight - self.velocity - self.mainCharacter.object.getHeight():
                    self.mainCharacter.changePos(0, self.velocity)
            self.mainCharacter.changePos(0, - distanceCheck)

        self.velocity = 5

        if(self.changeRoomOn):
            curRoom.doorwayCollisionCheck(self)

        if keyPressed[pygame.K_SPACE]:
            self.interactHitBox = self.getInteractHitbox()
            curRoom.interact(self)

        self.updateScreen()

    def getInteractHitbox(self):
        vector = [0, 0]
        facing = self.mainCharacter.object.facing
        if (facing == "U"):
            vector = [0, -1]
        elif (facing == "D"):
            vector = [0, 1]
        elif (facing == "L"):
            vector = [-1, 0]
        else:
            vector = [1, 0]

        width = 0
        height = 0
        x = 0
        y = 0

        # meaning that it is L or R
        if (vector[0]!=0):
            width = self.mainCharacter.object.getWidth()//4
            height = self.mainCharacter.object.getHeight()

            if(vector[0]<0):
                x = self.mainCharacter.object.HitBox.upperLeft[0] - width
            else:
                x = self.mainCharacter.object.HitBox.upperLeft[0] + self.mainCharacter.object.HitBox.width
            y = self.mainCharacter.object.HitBox.upperLeft[1]

        else:
            width = self.mainCharacter.object.getWidth()
            height = self.mainCharacter.object.getHeight()//4

            if(vector[1]<0):
                y = self.mainCharacter.object.HitBox.upperLeft[1] - height
            else:
                y = self.mainCharacter.object.HitBox.upperLeft[1] + self.mainCharacter.object.HitBox.height
            x = self.mainCharacter.object.HitBox.upperLeft[0]

        return HitBox([x,y],width,height)


