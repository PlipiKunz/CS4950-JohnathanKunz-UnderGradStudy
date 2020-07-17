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

        self.bufferLowerX = 150
        self.bufferUpperX = 350
        self.bufferLowerY = 150
        self.bufferUpperY = 350

        self.velocity = 5
        # mode 0 for noraml, 1 for battle
        self.mode = 0

        self.run = True
        self.changeRoomOn = True
        self.delay = 50

    def main(self):
        self.scanIn()

        while self.run:
            # Make sure to call pygame.event.pump() in every loop or the game gets backed up
            # and wont accept new key presses or other pieces, or at least call it before you need to get
            # key presses

            pygame.event.pump()
            pygame.time.delay(self.delay)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.mode == 0:
                self.mode0Code()

        self.saveState()
        pygame.quit()

    def mode0Code(self):
        curRoom = self.rooms[self.currentRoomIndex]

        pygame.key.set_repeat()

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


        if(keyPressed[pygame.K_SPACE]):
            self.interactHitBox = self.getInteractHitbox()
            curRoom.interact(self)

        self.updateScreen()

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

    def displayTextBox(self, content,  font=0, speeds=0, clrs=0, noise=0,):
        fontSize = 24
        font = pygame.font.Font('freesansbold.ttf', fontSize)

        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)
        dialogYLoc = 350
        dialogXLoc = 50
        dialogWidth = self.windowWidth-2*dialogXLoc
        dialogHeight = 100
        dialogRect = pygame.Rect((dialogXLoc, dialogYLoc), (dialogWidth, dialogHeight))

        loc = -1
        curContent1 = ""
        curContent2 = ""
        curContent3 = ""
        text1 = font.render(curContent1, True, white)
        text2 = font.render(curContent2, True, white)
        text3 = font.render(curContent3, True, white)
        time = 1
        skip = False
        while loc < len(content):
            useWhat = 0
            if(time==1):
                useWhat = text1
            if(time==2):
                useWhat = text2
            if(time==3):
                useWhat = text3
            stillGoing = True
            while useWhat.get_width() < dialogWidth-20 and loc < len(content) and stillGoing:
                pygame.event.pump()
                keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_LSHIFT]:
                    skip = True


                if(not skip):
                    pygame.time.delay(self.delay)
                else:
                    pygame.time.delay(5)

                if(self.distanceToNextSpace(content, loc, font) + useWhat.get_width() < dialogWidth):
                    loc += 1
                    if (loc < len(content)):
                        next = content[loc]

                        if(time==1):
                            curContent1 = curContent1 + next
                        if (time == 2):
                            curContent2 = curContent2 + next
                        if (time == 3):
                            curContent3 = curContent3 + next

                        self.updateScreen()

                        if(time == 1):
                            text1 = font.render(curContent1, True, white)
                        if(time == 2):
                            text2 = font.render(curContent2, True, white)
                        if (time == 3):
                            text3 = font.render(curContent3, True, white)

                        pygame.draw.rect(self.screen, black, dialogRect)

                        self.screen.blit(text1, (dialogXLoc, dialogYLoc + 5))
                        self.screen.blit(text2, (dialogXLoc, dialogYLoc + 5 + fontSize))
                        self.screen.blit(text3, (dialogXLoc, dialogYLoc + 5 + 2 * fontSize))

                        pygame.display.update()
                else:
                    stillGoing = False

                if (time == 1):
                    useWhat = text1
                if (time == 2):
                    useWhat = text2
                if (time == 3):
                    useWhat = text3

            time += 1

            while(loc + 1 < len(content)):
                if(content[loc+1]==" "):
                    loc += 1
                else:
                    break

            if(time==4 and loc < len(content)):
                skip = False
                time=1
                displayMessage = 0
                while (True):
                    pygame.event.pump()
                    pygame.time.delay(self.delay)

                    self.updateScreen()

                    pygame.draw.rect(self.screen, black, dialogRect)

                    self.screen.blit(text1, (dialogXLoc, dialogYLoc + 5))
                    self.screen.blit(text2, (dialogXLoc, dialogYLoc + 5 + fontSize))
                    self.screen.blit(text3, (dialogXLoc, dialogYLoc + 5 + 2 * fontSize))

                    if (displayMessage % 20 < 10):
                        finishedMessage = "NEXT PAGE"
                        finishedMessage = font.render(finishedMessage, True, red, white)
                        self.screen.blit(finishedMessage, (dialogXLoc + dialogWidth - finishedMessage.get_width(), dialogYLoc + dialogHeight - fontSize))
                    displayMessage += 1
                    displayMessage = displayMessage % 20

                    pygame.display.update()

                    keyPressed = pygame.key.get_pressed()
                    if keyPressed[pygame.K_SPACE]:
                        self.changeRoomOn = False
                        pygame.time.delay(self.delay)
                        break

                curContent1 = ""
                curContent2 = ""
                curContent3 = ""
                text1 = font.render(curContent1, True, white)
                text2 = font.render(curContent2, True, white)
                text3 = font.render(curContent3, True, white)

        displayMessage = 0
        while (True):
            pygame.event.pump()
            pygame.time.delay(self.delay)

            self.updateScreen()

            pygame.draw.rect(self.screen, black, dialogRect)

            self.screen.blit(text1, (dialogXLoc, dialogYLoc + 5))
            self.screen.blit(text2, (dialogXLoc, dialogYLoc + 5 + fontSize))
            self.screen.blit(text3, (dialogXLoc, dialogYLoc + 5 + 2 * fontSize))

            if(displayMessage%20 < 10):
                finishedMessage = "END DIALOG"
                finishedMessage = font.render(finishedMessage, True, red, white)
                self.screen.blit(finishedMessage, (dialogXLoc, dialogYLoc + dialogHeight))
            displayMessage += 1
            displayMessage = displayMessage%20

            pygame.display.update()

            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_SPACE]:
                self.changeRoomOn = False
                pygame.time.delay(self.delay)
                break

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

    def distanceToNextSpace(self, string, curIndex, font):
        strLen = len(string)
        stringPortion = ""
        while(True):
            if(curIndex+1 < strLen):
                curIndex += 1
                nextChar = string[curIndex]
                stringPortion += nextChar

                if(nextChar == " "):
                    return font.render(stringPortion,True, (0,0,0)).get_width()
            else:
                return 0
