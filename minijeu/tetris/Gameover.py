from random import *
import pygame


class Gameover:
    """
    Class that is used for the drawing of the gameover
    surface.
    """

    def __init__(self, width, height, score):
        self.width = width
        self.height = height
        self._score = score
        self.pressContinue = 0

    # Draws the Gameover surface and displays the score
    def draw_Gameover(self, surface):
        highscorefi = open("minijeu/tetris/highscore", "r")
        highscore = highscorefi.read()
        highscorefi.close()
        background_color = (255, 255, 255)
        font_color = (0, 0, 0)
        pygame.draw.rect(surface, background_color, (100, 100, self.width - 100, self.height - 100), 0)

        tetris_font = pygame.font.Font("minijeu/tetris/Tetris.TTF", 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("PERDU", 1, font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 150)

        tetris_font = pygame.font.SysFont("monospace", 32)
        tetris_font.set_bold(1)
        label_2 = tetris_font.render("Score:", 1, font_color)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 230)

        score = tetris_font.render("%i" % self._score, 1, font_color)
        score_rect = score.get_rect()
        score_rect.center = (150, 280)

        surface.blit(label_1, label_1_rect)
        surface.blit(label_2, label_2_rect)
        surface.blit(score, score_rect)

    # Prints the continue message
    def press_continue(self, surface):
        tetris_font = pygame.font.SysFont("monospace", 12)
        font_color = (0, 0, 0)

        label_1 = tetris_font.render("Appuyez sur une touche", True, font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 350)

        label_2 = tetris_font.render("Echap pour quitter", True, font_color)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 365)

        surface.blit(label_1, label_1_rect)
        surface.blit(label_2, label_2_rect)
