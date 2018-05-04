from random import *
import sys
from minijeu.tetris.Shapes import Shape
from minijeu.tetris.Area import Area
from minijeu.tetris.Display import Hud
from minijeu.tetris.Menu import Menu
from minijeu.tetris.Gameover import Gameover
from minijeu.tetris.Bot import Bot
import pygame
from pygame.locals import *
import menu.closemenu as closemenu

# checks the user input and implements proper tests and movements in correspondance
# with the user's input
def check_input(shape,area, surface):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                shape.rotate(area.matrix())
            if event.key == pygame.K_DOWN:
                shape.test_y(area.matrix())
                if shape.collision != 1:
                    shape.move_down(area.matrix())
            if event.key == pygame.K_LEFT:
                shape.move_left(area.matrix())
            if event.key == pygame.K_RIGHT:
                shape.move_right(area.matrix())
            if event.key == pygame.K_SPACE:
                shape.test_y(area.matrix())
                while shape.collision != 1:
                    shape.move_down(area.matrix())
                    shape.draw_shape(area.matrix(), surface)
                    area.draw(shape, area.matrix(), surface)
    return area


# updates the menu surface based on user inputs
def menu_input(menu, surface):
    while not menu.gameStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closemenu.closemenu(fenetre)

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_RETURN:
                    menu.gameStart = 1


def tetris(fenetre):
    pygame.mixer.music.load("son/Sound/tetris.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    bot = Bot()
    fond = pygame.image.load("minijeu/tetris/fond.png").convert_alpha()
    fenetre.blit(fond,(0,20))
    # initializes the surface, window name and the key repeater
    # if the key is held the key is repeated
    size = width, height = 300, 440

    pygame.key.set_repeat(75)

    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                closemenu.closemenu(fenetre)
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        # build a matrix for from the width and height
        surface=pygame.Surface((300,440))
        area = Area(width - 100, height)

        # initializes the shape queue (first number is current shape, second is upcoming)
        # randomizes the shape color
        shape_queue = []
        for i in range(5):
            shape_queue.append(randint(0, 6))
        shape_color = (randint(1, 255), randint(1, 255), randint(1, 255))

        # creates a new shape: 0 is the shape id
        shape = Shape(shape_color, shape_queue[0])

        # init Heads up Display
        hud = Hud(width, height)
        gameOver = Gameover(width, height, area.score)

        # redraws the surface with the black background hud and menu

        surface.fill((0, 0, 0))
        hud.draw(surface)
        menu = Menu(width, height)
        menu.draw_menu(surface)
        menu.update_menu(surface)
        fenetre.blit(surface, (250, 90))
        pygame.display.flip()

        # moves the selector box around the menu
        menu_input(menu, surface)

        # initializes the ticker and starts moving the blocks after ~1s elapsed.
        init = 1000
        start_time = pygame.time.get_ticks()

        # Single Player Looop
        while menu.singlePlayer and shape.game_state:
            check_input(shape, area, surface)
            time = pygame.time.get_ticks() - start_time

            # deactivate shape if state become one, pop shape off the queue and
            # add a new shape to the list and
            if shape.state == 1:
                next_shape.deactivate()
                shape_queue.pop(0)
                shape_queue.append(randint(0, 6))
                shape = Shape(shape_color, shape_queue[0], 0, 5, 0)
                shape_color = (randint(1, 255), randint(1, 255), randint(1, 255))

            # Delay (increase to increase the shape drop delay)
            if init < time:
                shape.move_down(area.matrix())
                init += 300

            # redraws the surface to update everything
            fenetre.blit(surface, (250, 90))
            surface.fill((0, 0, 0))
            shape.draw_shape(area.matrix(), surface)
            area.draw(shape, area.matrix(), surface)
            area.print_game_info(surface)
            next_shape = Shape(shape_color, shape_queue[1], 0, 12, 0)
            next_shape.update_shape(area.matrix())
            area.draw_next_shape(next_shape, surface)
            hud.draw(surface)
            pygame.display.flip()

        while not menu.info and not gameOver.pressContinue:
            highscorefi = open("minijeu/tetris/highscore", "r")
            highscore = int(highscorefi.read())
            highscorefi.close()
            if highscore<area.score:
                highscorefi = open("minijeu/tetris/highscore", "w")
                highscorefi.write(str(area.score))
                highscorefi.close()
            surface.fill((255,255,255))
            gameOver.draw_Gameover(surface)
            gameOver.press_continue(surface)
            fenetre.blit(surface, (250, 90))
            pygame.display.flip()

            # waits for a keystroke to move to main menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closemenu.closemenu(fenetre)

                if event.type == pygame.KEYDOWN:
                    gameOver.pressContinue = 1
                    if event.key==K_ESCAPE:
                        return

        # resets the game variables.
        menu.reset_game()
