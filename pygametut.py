import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("SimpleRPG")

x = 50
y = 450
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10

clock = pygame.time.Clock()
fps = 30


run = True
while run:
    # pygame.time.delay(int(fps))
    # Set the framerate
    clock.tick(fps)
    data = str(clock.get_fps())[:4]
    pygame.display.set_caption("SimpleRPG -- FPS: "+data)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # This allows control of the rectangle charactor.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= jumpCount ** 2 * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # This updates the background every loop.
    win.fill((0, 0, 0))

    # This is my red rectangle charactor
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    # This updates the game screen every loop.
    pygame.display.update()

pygame.quit()
