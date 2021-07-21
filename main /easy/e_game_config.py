import os



#Matrix Size for easy level
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 8
MARGIN = 10

IMAGE_SIZE = 315

#Screen Size
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 730

#CENTERING MATRIX
NUM_ROWS = 2
NUM_COLM = 4

T_B_MARG = (SCREEN_HEIGHT - (IMAGE_SIZE * NUM_ROWS) + (MARGIN *2)) // 2
R_L_MARG = (SCREEN_WIDTH - (IMAGE_SIZE * NUM_COLM) + (MARGIN *2))  // 2

ASSET_DIR = 'easy/easy_assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 4


