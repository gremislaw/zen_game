import pygame as pg
import pygame.gfxdraw as draw
from help import *

SIZE = get_size()

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chd_clr = (139, 0, 255)
        self.unchd_clr = (30, 0, 60)
        self.sound = pg.mixer.Sound('data/button.mp3')
        self.sound.set_volume(0.3)

    def draw(self, x, y, text, func, screen, pressed):
        x = int(x)
        y = int(y)
        pos = pg.mouse.get_pos()
        if x - self.width // 2 < pos[0] < x + self.width // 2 and y - int(self.height // 2) < pos[1] < y + self.height // 2:
            draw.filled_ellipse(screen, x, y, int(self.width // 1.5), int(self.height // 1.5), self.chd_clr)
            draw.aaellipse(screen, x, y, int(self.width // 1.5), int(self.height // 1.5), pg.Color('yellow'))
            f = pg.font.SysFont('arial', int(self.height) - 5).render(text, True, pg.Color('yellow'))
            ff = f.get_rect(center=(x, y))
            screen.blit(f, ff)
            if pressed:
                func(screen)
                return True
        else:
            draw.filled_ellipse(screen, x, y, int(self.width // 2), int(self.height // 2), self.unchd_clr)
            draw.aaellipse(screen, x, y, int(self.width // 2), int(self.height // 2), pg.Color('orange'))
            f = pg.font.SysFont('arial', int(self.height) - int(SIZE.current_h * 0.019)).render(text, True, pg.Color('orange'))
            ff = f.get_rect(center=(x, y))
            screen.blit(f, ff)