import pygame


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Test Game")

    playX = 50
    playY = 50
    playRecWidth = 40
    playRecHeight = 40
    playVel = 5
    run = True

    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_LEFT]:
            playX -= playVel
        if keyPressed[pygame.K_RIGHT]:
            playX += playVel
        if keyPressed[pygame.K_UP]:
            playY -= playVel
        if keyPressed[pygame.K_DOWN]:
            playY += playVel

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 255, 255), (playX, playY, playRecWidth, playRecHeight))
        pygame.display.update()

    pygame.quit()
