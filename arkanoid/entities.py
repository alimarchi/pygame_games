import pygame as pg

class Vigneta:
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 0
        self.vy = 0

    @property
    def xcentro(self):
            return self.x + self.ancho // 2 

    @property
    def ycentro(self):
            return self.y + self.alto // 2

    def dibujar(self):
        pass

    def mover(self):
        pass

    def intersecta(self, otro) -> bool:

        if self.ancho > otro.ancho:
            menor_ancho = otro
            mayor_ancho = self

        else:
            menor_ancho = self
            mayor_ancho = otro

        if self.alto > otro.alto:
            menor_alto = otro
            mayor_alto = self

        else:
            menor_alto = self
            mayor_alto = otro

        return (menor_ancho.x in range(mayor_ancho.x, mayor_ancho.x + mayor_ancho.ancho) or \
                menor_ancho.x + menor_ancho.ancho in range(mayor_ancho.x, mayor_ancho.x + mayor_ancho.ancho)) and \
                (menor_alto.y in range(mayor_alto.y, mayor_alto.y + mayor_alto.alto) or \
                menor_alto.y + menor_alto.alto in range(mayor_alto.y, mayor_alto.y + mayor_alto.alto))

class Ladrillo(Vigneta):
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def comprobarToque(self, bola):
        if self.intersecta(bola):
            bola.vy *= -1
            return True
        
        return False
    
class Raqueta(Vigneta):
    def __init__(self, padre, x, y, color =(255, 255, 0)):
        self.images = []
        for i in range(3):
            self.images.append(pg.image.load(f"./resources/images/electric0{i}.png"))
        self.imagen_activa = 0
        self.frecuencia_cambio = 5
        self.contador_frames = 0
        self.imagen = self.images[self.imagen_activa]
        self.rect = self.imagen.get_rect()
        super().__init__(padre, x, y, self.rect.width, self.rect.height, color)
        self.vx = 5

    def dibujar(self):
        self.padre.blit(self.images[self.imagen_activa], (self.x, self.y))

        self.contador_frames += 1
        if self.contador_frames == self.frecuencia_cambio:
            self.imagen_activa += 1
            if self.imagen_activa >= len(self.images):
                self.imagen_activa = 0
            
            self.contador_frames = 0
        
        #self.imagen_activa = (self.imagen_activa +1) % len(self.images)
        #pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.x -= self.vx 
        if teclas[pg.K_RIGHT]:
            self.x += self.vx

        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho

class Bola(Vigneta):
    def __init__(self, padre, x, y, color=(255,255,255), radio =10):
        super().__init__(padre, x - radio, y - radio, 2 * radio, 2* radio, color)
        self.radio = radio
        self.vx = 3
        self.vy = 3
        self.x_ini = x
        self.y_ini = y
        self.esta_viva = True

    def reset(self):
        self.x = self.x_ini
        self.y = self.y_ini
        self.esta_viva = True

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= self.padre.get_width() - self.ancho:
            self.vx *= -1
        
        if self.y <= 0:
            self.vy *= -1 
    
        if self.y >= self.padre.get_height() - self.alto:
            self.esta_viva = False

    def dibujar(self):
        pg.draw.circle(self.padre, self.color,(self.xcentro, self.ycentro), self.radio)

    def compruebaChoque(self, otro):
        if self.intersecta(otro):
            self.vy *= -1


