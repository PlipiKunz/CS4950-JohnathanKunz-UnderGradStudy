from Room import Room


class Room0(Room):
    def __init__(self):
        super().__init__(0,0,0,0)

    def specialOccuranceCheck(self, controller):
        print("SHOULDNTBEHERE specialOccuranceCheck room")
        pass

    def placeEntities(self, controller):
        controller.screen.fill((0,255,0))

    def entityCollisionCheck(self):
        print("SHOULDNTBEHERE entityCollisionCheck room")
        pass

    def doorwayCollisionCheck(self):
        print("SHOULDNTBEHERE doorWayCollisionCheck room")
        pass
