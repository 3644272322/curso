import pygame as pg
#crear una plantilla enemiga
class Turrent(pg.sprit.Sprite):
    def __init__ (self,pos,image):
        pg.sprit.Sprite.__init__(self)
        self.image = image     
        self.rect = self.image.get_rect()
        self.rect.center =  pos