import pygame
from Room import Room
from RoomObjectWrapper import RoomObjectWrapper

import MainCharacter
from RoomZero import Room0


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Game One")

        self.rooms = [Room0()]
        self.flags = []
        self.currentRoomIndex = 0

        mainCharChar = MainCharacter.MainCharacter()
        self.mainCharacter = RoomObjectWrapper(mainCharChar, 0, 0)

        self.charVelocity = 5

        print(self.mainCharacter.object)
        self.run = True

    def main(self):
        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.mainCharacter.roomXPos -= self.charVelocity
            if keyPressed[pygame.K_RIGHT]:
                self.mainCharacter.roomXPos += self.charVelocity
            if keyPressed[pygame.K_UP]:
                self.mainCharacter.roomYPos -= self.charVelocity
            if keyPressed[pygame.K_DOWN]:
                self.mainCharacter.roomYPos += self.charVelocity

            self.updateScreen()
        pygame.quit()

    def updateScreen(self):
        if(self.currentRoomIndex < self.rooms.__len__()):
            roomToCome = self.rooms[self.currentRoomIndex]
            if(isinstance(roomToCome, Room)):
                roomToCome.placeEntities(self)
                self.mainCharacter.draw(self)
            else:
                print("Horrible Awful Crash The Room Wasnt a Room")
                self.run = False

            pygame.display.update()
        else:
            print("Horrible Awful Crash The Room Index Exceeded the Rooms list size")
            self.run = False

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
