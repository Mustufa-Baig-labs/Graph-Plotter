import pygame
import math
pygame.init()

size=(1200,600)

win=pygame.display.set_mode(size)

def graph(x,y,precision=0.01,offset=2.5,scale=(1,0.01)):
    x=(x*scale[0])
    y=(y*scale[1])
    
    func=math.tan(math.radians(x))
    
    if func>=y-precision-offset and func<=y+precision-offset:
        return True
    
    return False

run=True

while run:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            run=False

    win.fill((0,0,0))
    for x in range(size[0]):
        for y in range(size[1]):
            if graph(x,y):
                win.set_at((x,size[1]-y),((255,255,255)))
    pygame.display.update()
    #print(".")
    

pygame.quit()
