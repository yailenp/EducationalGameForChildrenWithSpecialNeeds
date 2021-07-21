import pygame
import medium.m_game_config as gc
import pygame, os, sys, random
from pygame.locals import *
from pygame import display, event, image, transform
from time import sleep

#center matrix selection of the mouse
def find_index_from_xy(x, y):
    row = (y - gc.T_B_MARG) // (gc.IMAGE_SIZE)
    col = (x - gc.R_L_MARG) // gc.IMAGE_SIZE 
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index  

#creates a dictionary (list) of the name of the assets in form name:0
medium_count = {a:0 for a in gc.ASSET_FILES}

#counts how many times an asset occurs in the list to ensure it only occurs once
def available_medium():
    return [medium for medium, count in medium_count.items() if count < 2]

#the class randomely chooses a card from the available def and draws it/locates it
class Medium:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_medium())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((16,78,139))
        medium_count[self.name] += 1
        
def med_level():
    
    pygame.init()

    #used to reinitialize the level after it is played multiple times
    global medium_count
    medium_count = {a:0 for a in gc.ASSET_FILES}

    running = True
    
    #Window size
    screen = display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT))
    
    matched = image.load('medium/m_other_assets/matched.png')
    
    #initialized variable for number of guess
    global medguess
    global mg
    medguess = 0

    #initialized variable for number of matches
    global medmatches
    global mm
    medmatches = 0
    
    tiles = [Medium(i) for i in range(0, gc.NUM_TILES_TOTAL)]
    current_images_displayed = []


    while (running):
            
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()

            #find mouse selection of card
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col, index = find_index_from_xy(mouse_x, mouse_y)
                if index not in current_images_displayed:
                    if len(current_images_displayed) > 1:
                        current_images_displayed = current_images_displayed[1:] + [index]
                    else:
                        current_images_displayed.append(index)

        # Display medium level images
        screen.fill((227,227,227))

        total_skipped = 0

        for i, tile in enumerate(tiles):
            current_image = tile.image if i in current_images_displayed else tile.box
            if not tile.skip:
                screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.R_L_MARG, tile.row * gc.IMAGE_SIZE + gc.T_B_MARG))
            else:
                total_skipped += 1


        display.flip()

        # Check for matches between the tiles
        if len(current_images_displayed) == 2:
            idx1, idx2 = current_images_displayed
            if tiles[idx1].name == tiles[idx2].name:
                tiles[idx1].skip = True
                tiles[idx2].skip = True
                # display matched message and add 1 to the number of matches
                sleep(0.2)
                screen.blit(matched, (0 , 0))
                display.flip()
                sleep(0.5)
                current_images_displayed = []
                medmatches += 1
            #add 1 to the number of guesses made by player
            if tiles[idx1].name != tiles[idx2].name:
                display.flip()
                sleep(0.8)
                current_images_displayed = []
                medguess += 1


        if total_skipped == len(tiles):

            pygame.display.update()
            mg = medguess
            mm = medmatches
            
            #to delete the list of cards name and reinitialize every time
            del medium_count

            running=False
            
    return

            

