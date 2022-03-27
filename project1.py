import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


face=pygame.Rect(100,200,200,200)
eye1=pygame.Rect(120,240,60,30)
eye2=pygame.Rect(230,240,60,30)
mouth=pygame.Rect(160,320,90,30)
nose=pygame.Rect(200,280,10,20)

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    pygame.draw.rect(screen,(120,120,120),face)  
    pygame.draw.rect(screen,(225,225,0),eye1)  
    pygame.draw.rect(screen,(225,225,0),eye2)  
    pygame.draw.rect(screen,(225,150,150),mouth)  
    pygame.draw.rect(screen,(250,20,20),nose)  

    pygame.display.update()
    clock.tick(30)



