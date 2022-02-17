import pygame as pg
pg.init()

class Bola:
    def __init__(self, x, y, color=(255,255,255), radio =10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio

class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(ancho//2, alto//2, (255,255,0))

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True 


            self.pantalla.fill((255, 0, 0))
            pg.draw.circle(self.pantalla, self.bola.color, 
                        (self.bola.x, self.bola.y), self.bola.radio)

            pg.display.flip()

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()

    pg.quit()