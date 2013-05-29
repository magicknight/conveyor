import pygame
import os

from gui_common import Rectangle

class SpriteSheet(object):
    ''' Used to load a set of sprites from a sprite sheet.
    '''
    def __init__(self, key, filename, sheet_size=(30,30), tile_size=(10,10)):
        self.key = key
        self.width, self.height = sheet_size
        self.tile_width, self.tile_height = tile_size
        self.filename = filename
        self._sheet = pygame.image.load(self.filename).convert_alpha()
        self._load_images()


    def _load_images(self):
        ''' Loads sprites into a list from left to right then top to bottom.'''
        tiles_across = int(self.width / self.tile_width)
        tiles_down = int(self.height / self.tile_height)
        rects = []
        for y in range(tiles_down):
            for x in range(tiles_across):
                rects.append(Rectangle(x*self.tile_width, y*self.tile_height, self.tile_width, self.tile_height))
                
        self._sprites = self._images_at(rects)
    
    def _image_at(self, rectangle):
        '''Loads image from x,y,x+offset,y+offset'''
        return self._sheet.subsurface(rectangle)
    
    def _images_at(self, rects):
        '''Loads multiple images, supply a list of coordinates''' 
        return [self._image_at(rect) for rect in rects]

    def __getitem__(self, index):
        return self._sprites[index]

    
