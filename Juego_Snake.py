from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

from sqlalchemy import false
import pygame
import random

class cuerpo:
    def __init__(self, ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana
    
    def dibujar:
        pygame.draw.rect(self.ventana, (255, 0, 0), (self.x, self.y, 10, 10))    
    
    def moverse(selt):
        if self.dir == 0:
            self.x += 100
        elif self.dir == 1:
            self.x -= 100
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10
            

class manzanas:
    def __init__(self, ventana):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.ventana = ventana
    
    def dibujar():  
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))    
    
    def nueva manzana(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
       
def refrescar(ventana):
    ventana.fill((0, 0, 0))
    comida.dibujar()
    for i in range(len(serpiente))
    serpiente[1].dibujar()

def seguir_cabeza():
    for i in range(len(serpiente) - 1):
        serpiente[len(serpeinte) -1 -1].x = serpiente[len(serpiente) - 1 - 2].x
        serpiente[len(serpeinte) -1 -1].y = serpiente[len(serpiente) - 1 - 2].y    

def main ():
    global serpiente, comidade
    ventana = pygame.display.set_mode((400, 400))
    ventana.fill((0, 0, 0))
    comida = manzanas(ventana)
    serpiente = [cuerpo(ventana)]
    run = True
    while run:
        for even in pygame.event.get():
            if event.type == pygame.quit:
                run = false
            if event.type == pygame.KEYDOWN
                if event.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                if event.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                if event.key == pygame.K_DOWN:
                    serpiente[0].dir = 2
                if event.key == pygame.K_UP:
                    serpiente[0].dir = 3
                
        serpiente[0].moverse()
        refrescar(ventana)
        pygame.display.update()
        pygame.time.delay(100)
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))
        seguir_cabeza()
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        elif serpiente[0].x < 0:
            serpiente[0].x = 390
        if serpiente[0].y >= 400:
            serpiente[0].y = 0
        elif serpiente[0].y < 0:
            serpiente[0].y = 390

if   __name__ == "__main__":
    main()
    pygame.quit()
                