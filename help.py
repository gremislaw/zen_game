import pygame as pg

def get_size():
    pg.init()
    SIZE = pg.display.Info()
    return SIZE


SIZE = get_size()


def img_convert(*imgs):
    sp = []
    for img in imgs:
        img = pg.transform.scale(img, (SIZE.current_w * 0.03, SIZE.current_h * 0.08))
        sp.append(img)
    return sp


def img_convert_slash(*imgs):
    sp = []
    for img in imgs:
        img = pg.transform.scale(img, (SIZE.current_w * 0.045, SIZE.current_h * 0.08))
        sp.append(img)
    return sp


def demon1_convert(*imgs):
    sp = []
    for img in imgs:
        img = pg.transform.scale(img, (SIZE.current_w * 0.015, SIZE.current_h * 0.09))
        sp.append(img)
    return sp


def demon1_died_convert(*imgs):
    sp = []
    for img in imgs:
        img = pg.transform.scale(img, (SIZE.current_w * 0.045, SIZE.current_h * 0.09))
        sp.append(img)
    return sp
