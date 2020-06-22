import pygame
from Room import Room
from RoomObjectWrapper import RoomObjectWrapper

from Characters import MainCharacter
from Rooms.RoomZero import Room0


class Controller:
    def __init__(self):
        pygame.init()
        self.windowWidth = 500
        self.windowHeight = 500
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Game One")

        self.rooms = [Room0()]
        self.flags = []
        self.currentRoomIndex = 0

        mainCharChar = MainCharacter.MainCharacter()
        self.mainCharacter = RoomObjectWrapper(mainCharChar, 0, 0)
        
        self.bufferLowerX = 200
        self.bufferUpperX = 300
        self.bufferLowerY = 200
        self.bufferUpperY = 300

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

            if(self.mode==0):
                curRoom = self.rooms[self.currentRoomIndex]

                x = self.mainCharacter.roomXPos
                y = self.mainCharacter.roomYPos
                charCentered = (x > self.bufferLowerX) and (x < self.bufferUpperX) and (y > self.bufferLowerY) and (y < self.bufferUpperY)

                keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_LEFT]:

                    if((curRoom.baseX) <= -self.velocity and charCentered ):
                        curRoom.baseX += self.velocity
                    elif(self.mainCharacter.roomXPos >= self.velocity):
                        self.mainCharacter.roomXPos -= self.velocity

                if keyPressed[pygame.K_RIGHT]:

                    if ((curRoom.baseX + curRoom.width - self.windowWidth) >= self.velocity  and charCentered ):
                        curRoom.baseX -= self.velocity
                    elif (self.mainCharacter.roomXPos <= self.windowWidth - self.velocity):
                        self.mainCharacter.roomXPos += self.velocity

                if keyPressed[pygame.K_UP]:
                    if ((curRoom.baseY) <= -self.velocity  and charCentered):
                        curRoom.baseY += self.velocity
                    elif (self.mainCharacter.roomYPos >= self.velocity):
                        self.mainCharacter.roomYPos -= self.velocity

                if keyPressed[pygame.K_DOWN]:
                    if ((curRoom.baseY + curRoom.height - self.windowHeight) >= self.velocity  and charCentered):
                        curRoom.baseY -= self.velocity
                    elif (self.mainCharacter.roomYPos <= self.windowHeight - self.velocity):
                        self.mainCharacter.roomYPos += self.velocity

                self.updateScreen()
        pygame.quit()

    def updateScreen(self):
        if(self.mode==0):
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
        pass

    def changeToBattleRoom(self, enemy, conditions):
        pass
