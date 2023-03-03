import pygame
pygame.init()

clk = pygame.time.Clock()

size = width, height = 552, 430
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('./templates/control2.png').convert()
#scaled_image = pygame.transform.scale(background_image, (width, int(background_image.get_height() * width / background_image.get_width())))
frameReact = pygame.Rect((0, 0), (width, height))
font = pygame.font.SysFont("Calibri", 24)

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)


while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))  
    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (442, 233))
    if Keys[pygame.K_c]: screen.blit(crosshair, (388, 277))
    if Keys[pygame.K_v]: screen.blit(crosshair, (485, 282))
    if Keys[pygame.K_z]: screen.blit(crosshair, (430, 325))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0
    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                label = font.render("Tecla presionada: X", True, (255, 255, 255))               
            elif event.key == pygame.K_c:
                label = font.render("Tecla presionada: C", True, (255, 255, 255))
            elif event.key == pygame.K_v:
                label = font.render("Tecla presionada: V", True, (255, 255, 255)) 
            elif event.key == pygame.K_z:
                label = font.render("Tecla presionada: Z", True, (255, 255, 255))
            elif event.key == pygame.K_LEFT:
                label = font.render("Tecla presionada: LEFT", True, (255, 255, 255))
            elif event.key == pygame.K_UP:
                label = font.render("Tecla presionada: UP", True, (255, 255, 255))
            elif event.key == pygame.K_RIGHT:
                label = font.render("Tecla presionada: RIGHT", True, (255, 255, 255))
            elif event.key == pygame.K_DOWN:
                label = font.render("Tecla presionada: DOWN", True, (255, 255, 255))  
            screen.blit(label, (20, 70))
            pygame.display.update()
            pygame.time.delay(90)
            #screen.fill((0, 0, 0))              
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*30)+111-5, (y*30)+281-5))
    pygame.display.flip()
    clk.tick(40)