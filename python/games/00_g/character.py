import pygame as pg 

#crear una plantilla enemigos
class Character (pg.sprite.Sprite):
    def __init__(self,pos,image) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=pos

    def move_left(self,new_pos): # method izquierda
       self.rect.x -= new_pos

    def move_rigth(self,new_pos): # method derecha
        self.rect.x += new_pos

    def move_up(self,new_pos):
        self.rect.y -= new_pos
    
    
    def move_down(self,new_pos):
        self.rect.y += new_pos