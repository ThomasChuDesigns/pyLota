import pygame as pg
import ui

class BouncyText(ui.StringRenderer):
    critical = pg.Color(236,208,120)

    def __init__(self, host, value, position, size = 32, state = pg.Color(192,41,66), back = pg.Color(84,36,55)):
        super().__init__()
        self.size = size
        self.host = host
        self.value = value
        self.position = list(position)
        self.position[0] -= self.getStringSize(value,size)[0] // 2

        self.fg = state
        self.bg = back

        self.alive = True
        self.lifeTime = 500

    def update(self,dt):
        if self.alive:
            self.lifeTime -= dt
            if self.lifeTime <= 0:
                self.alive = False

            self.position[1] -= 0.05*dt
        else:
            self.host.statQueue.remove(self)

    def draw(self,surface,camera):
        ox = self.position[0] + 3
        if self.alive:
            self.drawString(surface,self.value,camera.applyOnPosition([ox,self.position[1]]),self.size,self.bg)
            self.drawString(surface,self.value,camera.applyOnPosition([self.position[0],self.position[1]]),self.size,self.fg)







