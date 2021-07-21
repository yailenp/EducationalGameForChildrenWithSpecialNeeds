import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import pygame, os, sys

#imported functions
import easy_app as ea
import med_app as ma
import hard_app as ha

def easy():
    ea.easy_level()
    
    
    surface = create_example_window('Educational Card Game', (1350, 730))

    #background and title of the main menu
    etheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    etheme.title_background_color=(69,139,116)
    etheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    etheme.title_font_shadow = True
    etheme.title_font_color = (227,227,230)
    etheme.title_font_size = 90
    etheme.title_offset = (195,0)
    etheme.background_color = (227,227,227)
    #buttons of the menu
    #mytheme.widget_font_color = (0,0,0)
    etheme.widget_border_color = (128,128,128)
    etheme.cursor_color = (0,0,0)
    etheme.selection_color = (69,139,116)
    etheme.widget_font_size= 40
    #menu definition
    menu = pygame_menu.Menu(
        height=730,
        theme=etheme,
        title='Easy Level Completed!',
        width=1350
    )
    #decorator
    decorator = menu.get_decorator()

    #green square horizontal
    decorator.add_rectangle(-710, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, -80, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, 140, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, -190, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, 140, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, -190, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, -300, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, 30, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, -300, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-710, 30, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, -80, 100, 100, (69,139,116), border=0, prev=False)

    E_ScoreM = 'Number of Matches: %d' % int(ea.em)
    menu.add.label(E_ScoreM, max_char=-1,font_size=30,font_color =(69,139,116))

    E_ScoreG = 'Number of Guesses: %d' % int(ea.eg)
    menu.add.label(E_ScoreG, max_char=-1,font_size=30,font_color =(69,139,116))

    menu.add.vertical_margin(35)
    menu.add.button('Play Again',easy,font_color = (69,139,116))
    menu.add.button('Main Menu',main_m,font_color = (0,0,0))
    menu.add.button('Quit', pygame_menu.events.EXIT,font_color =(0,0,0))

    if __name__ == '__main__':
        menu.mainloop(surface)

def medium():
    ma.med_level()

    surface = create_example_window('Educational Card Game', (1350, 730))

    #background and title of the main menu
    etheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    etheme.title_background_color=(16,78,139)
    etheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    etheme.title_font_shadow = True
    etheme.title_font_color = (227,227,230)
    etheme.title_font_size = 90
    etheme.title_offset = (120,0)
    etheme.background_color = (227,227,227)
    #buttons of the menu
    #mytheme.widget_font_color = (0,0,0)
    etheme.widget_border_color = (128,128,128)
    etheme.cursor_color = (0,0,0)
    etheme.selection_color = (16,78,139)
    etheme.widget_font_size= 40
    #menu definition
    menu = pygame_menu.Menu(
        height=730,
        theme=etheme,
        title='Medium Level Completed!',
        width=1350
    )
    
    #decorator
    decorator = menu.get_decorator()

    #green square horizontal
    decorator.add_rectangle(-710, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, -80, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, 140, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, -190, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, 140, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, -190, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, -300, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, 30, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, -300, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-710, 30, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, -80, 100, 100, (16,78,139), border=0, prev=False)
    
    M_ScoreM = 'Number of Matches: %d' % int(ma.mm)
    menu.add.label(M_ScoreM, max_char=-1,font_size=30,font_color =(16,78,139))

    M_ScoreG = 'Number of Guesses: %d' % int(ma.mg)
    menu.add.label(M_ScoreG, max_char=-1,font_size=30,font_color =(16,78,139))

    menu.add.vertical_margin(35)
    menu.add.button('Play Again',medium,font_color = (16,78,139))
    menu.add.button('Main Menu',main_m,font_color = (0,0,0))
    menu.add.button('Quit', pygame_menu.events.EXIT,font_color =(0,0,0))

    if __name__ == '__main__':
        menu.mainloop(surface)

def hard():
    ha.hard_level()

    surface = create_example_window('Educational Card Game', (1350, 730))

    #background and title of the main menu
    etheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    etheme.title_background_color=(205,38,38)
    etheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    etheme.title_font_shadow = True
    etheme.title_font_color = (227,227,230)
    etheme.title_font_size = 90
    etheme.title_offset = (195,0)
    etheme.background_color = (227,227,227)
    #buttons of the menu
    #mytheme.widget_font_color = (0,0,0)
    etheme.widget_border_color = (128,128,128)
    etheme.cursor_color = (0,0,0)
    etheme.selection_color = (205,38,38)
    etheme.widget_font_size= 40
    #menu definition
    menu = pygame_menu.Menu(
        height=730,
        theme=etheme,
        title='Hard Level Completed!',
        width=1350
    )

    #decorator
    decorator = menu.get_decorator()

    #green square horizontal
    decorator.add_rectangle(-710, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, -80, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, 140, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, -190, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, 140, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, -190, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, -300, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, 30, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, -300, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-710, 30, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, -80, 100, 100, (205,38,38), border=0, prev=False)
    
    H_ScoreM = 'Number of Matches: %d' % int(ha.hm)
    menu.add.label(H_ScoreM, max_char=-1,font_size=30,font_color =(205,38,38))

    H_ScoreG = 'Number of Guesses: %d' % int(ha.hg)
    menu.add.label(H_ScoreG, max_char=-1,font_size=30,font_color =(205,38,38))

    menu.add.vertical_margin(35)
    menu.add.button('Play Again',hard,font_color = (205,38,38))
    menu.add.button('Main Menu',main_m,font_color = (0,0,0))
    menu.add.button('Quit', pygame_menu.events.EXIT,font_color =(0,0,0))

    if __name__ == '__main__':
        menu.mainloop(surface)
    
def main_m():

    surface = create_example_window('Educational Card Game', (1350, 730))

    #background and title of the main menu
    mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    mytheme.title_background_color=(16,78,139)
    mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    mytheme.title_font_shadow = True
    mytheme.title_font_color = (227,227,230)
    mytheme.title_font_size = 70
    mytheme.background_color = (227,227,227)

    #buttons of the menu
    #mytheme.widget_font_color = (0,0,0)
    mytheme.widget_border_color = (128,128,128)
    mytheme.cursor_color = (0,0,0)
    mytheme.selection_color = (0,0,0)
    mytheme.widget_font_size= 40


    #menu definition
    menu = pygame_menu.Menu(
        height=730,
        theme=mytheme,
        title='Educational Card Matching Game',
        width=1350
    )


    #decorator
    decorator = menu.get_decorator()
    #squares
    #green
        #green square horizontal
    decorator.add_rectangle(-600, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-270, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(60, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(390, 250, 100, 100, (69,139,116), border=0, prev=False)
        #green square vertical
    decorator.add_rectangle(-600, 250, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(-600, -80, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, 140, 100, 100, (69,139,116), border=0, prev=False)
    decorator.add_rectangle(610, -190, 100, 100, (69,139,116), border=0, prev=False)

    #blue
        #blue square horizontal
    decorator.add_rectangle(-490, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-160, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(170, 250, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(500, 250, 100, 100, (16,78,139), border=0, prev=False)
        #blue square vertical
    decorator.add_rectangle(-600, 140, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(-600, -190, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, 30, 100, 100, (16,78,139), border=0, prev=False)
    decorator.add_rectangle(610, -300, 100, 100, (16,78,139), border=0, prev=False)

    #red
        #red square horizontal
    decorator.add_rectangle(-710, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-380, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(-50, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(280, 250, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, 250, 100, 100, (205,38,38), border=0, prev=False)
        #red square vertical
    decorator.add_rectangle(-600, 30, 100, 100, (205,38,38), border=0, prev=False)
    decorator.add_rectangle(610, -80, 100, 100, (205,38,38), border=0, prev=False)


    menu.add.button('Easy',easy,font_color = (69,139,116))
    menu.add.button('Medium', medium,font_color = (16,78,139))
    menu.add.button('Hard', hard,font_color =(205,38,38))
    menu.add.vertical_margin(35)
    menu.add.button('Quit', pygame_menu.events.EXIT,font_color =(128,128,128))

    if __name__ == '__main__':
        menu.mainloop(surface)

main_m()

