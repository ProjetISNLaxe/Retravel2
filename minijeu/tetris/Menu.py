from random import *
import pygame


class Menu:
    """
    Class to draw the menu and keep it updated

    Gives information to the main file for which
    surface to display and which game to play.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.demo = 0
        self.singlePlayer = 1
        self.info = 0
        self.gameStart = 0
        self.infoDone = 0

    # draws the menu surface with the title and names
    def draw_menu(self, surface):

        background_color = (255, 255, 255)
        font_color = (0, 0, 0)

        pygame.draw.rect(surface, background_color, (50, 50, self.width - 100, self.height - 100), 0)

        tetris_font = pygame.font.Font("minijeu/tetris/Tetris.TTF", 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("TETRIS", 1, font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 100)

        tetris_font = pygame.font.SysFont("monospace", 10)

        surface.blit(label_1, label_1_rect)


    # displays the info page once it is selected
    # has instructions for how to play the game
    # as well as the scoring system

    # updates the menu to display the current users selection
    def update_menu(self, surface):

        tetris_font = pygame.font.Font("minijeu/tetris/Tetris.TTF", 16)
        tetris_font.set_bold(0)

        singlePlayerBG = (255 * (1 - self.singlePlayer), 255 * (1 - self.singlePlayer), 255 * (1 - self.singlePlayer))
        demoBG = (255 * (1 - self.demo), 255 * (1 - self.demo), 255 * (1 - self.demo))
        infoBG = (255 * (1 - self.info), 255 * (1 - self.info), 255 * (1 - self.info))

        singlePlayerFont = (255 * self.singlePlayer, 255 * self.singlePlayer, 255 * self.singlePlayer)
        demoFont = (255 * self.demo, 255 * self.demo, 255 * self.demo)
        infoFont = (255 * self.info, 255 * self.info, 255 * self.info)

        pygame.draw.rect(surface, singlePlayerBG, (90, 180, 120, 20), 0)
        label_2 = tetris_font.render("Jouer", True, singlePlayerFont)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 190)
        surface.blit(label_2, label_2_rect)


    # function to switch the current selection on the menu surface


    # function to reset game initialization variables
    def reset_game(self):
        self.demo = 0
        self.singlePlayer = 1
        self.info = 0
        self.gameStart = 0
        self.infoDone = 0
