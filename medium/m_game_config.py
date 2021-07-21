import os
import pygame


IMAGE_SIZE = 170

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 730

#Matrix size for medium level
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 10

#CENTERING MATRIX
NUM_ROWS = 4
NUM_COLM = 4

T_B_MARG = (SCREEN_HEIGHT - (IMAGE_SIZE * NUM_ROWS) + (MARGIN *2)) // 2
R_L_MARG = (SCREEN_WIDTH - (IMAGE_SIZE * NUM_COLM) + (MARGIN *2))  // 2

ASSET_DIR = 'medium/med_assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 8


        
        
    
