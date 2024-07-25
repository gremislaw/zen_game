import pygame as pg
import pygame.gfxdraw as draw
from help import *

SIZE = get_size()

class Button:
    def __init__(self, width, height, x, y, func, screen):
        self.width = width
        self.height = height
        self.chd_clr = (139, 0, 255)
        self.unchd_clr = (30, 0, 60)
        self.sound = pg.mixer.Sound('data/musics/button.mp3')
        self.sound.set_volume(0.1)
        self.func = func
        self.screen = screen
        self.x = int(x)
        self.y = int(y)

    def draw(self, text, pressed, additional_variable=''):
        if self.check_intersect():
            draw.filled_ellipse(self.screen, self.x, self.y, int(self.width), int(self.height), self.chd_clr)
            draw.aaellipse(self.screen, self.x, self.y, int(self.width), int(self.height), pg.Color('yellow'))
            draw.aaellipse(self.screen, self.x, self.y, int(self.width) - 1, int(self.height) - 1, pg.Color('yellow'))
            f = pg.font.SysFont('arial', int(self.height) - int(SIZE.current_h * 0.0005)).render(text, True, pg.Color('yellow'))
            ff = f.get_rect(center=(self.x, self.y))
            self.screen.blit(f, ff)
            if pressed:
                if additional_variable == '':
                    self.func(self.screen)
                else:
                    self.func(self.screen, additional_variable)
                self.sound.play()
        else:
            draw.filled_ellipse(self.screen, self.x, self.y, int(self.width) - 1, int(self.height) - 1, self.unchd_clr)
            draw.aaellipse(self.screen, self.x, self.y, int(self.width), int(self.height), (250, 200, 0))
            draw.aaellipse(self.screen, self.x, self.y, int(self.width) - 1, int(self.height) - 1, (250, 200, 0))
            draw.aaellipse(self.screen, self.x, self.y, int(self.width) - 2, int(self.height) - 2, (250, 200, 0))
            f = pg.font.SysFont('arial', int(self.height) - int(SIZE.current_h * 0.001)).render(text, True, (250, 200, 0))
            ff = f.get_rect(center=(self.x, self.y))
            self.screen.blit(f, ff)

    def check_intersect(self):
        pos = pg.mouse.get_pos()
        if self.x - self.width < pos[0] < self.x + self.width and self.y - int(self.height) < pos[1] < self.y + self.height:
            return True
        else:
            return False