import pygame as pg
import random
import time
pg.init()

class Bola:
    def __init__(self, padre, x, y, vx, vy, color, radio):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.padre = padre

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1
        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.padre, self.color,(self.x, self.y), self.radio)

class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        #self.bola = Bola(self.pantalla, ancho//2, alto//2, (255,255,0))
        self.bolas = []
        for n in range(random.randint(5, 15)):
            self.bolas.append(Bola(self.pantalla, random.randint(20, ancho-20), random.randint(20, alto-20), 
            random.randint(1, 5), random.randint(1, 5),
            (random.randint (0,255),random.randint(0, 255), random.randint(0,255)),
            random.randint(5,20)))
        
    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True 
            
            for numero in range(len(self.bolas)):
                self.bolas[numero].mover()
                self.pantalla.fill((255, 0, 0))
                for numero in range(len(self.bolas)):
                    self.bolas[numero].dibujar()


            pg.display.flip()

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()

    pg.quit()