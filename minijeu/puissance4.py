# coding: utf8
import time
import sys
import pygame, closemenu
import json
from pygame.locals import *
from random import randint




def menu(fenetre):  # choice beetween replay or go start
    time.sleep(1.5)
    menu = pygame.image.load("puissance4/menu.png").convert()
    fenetre.blit(menu, (230, 200))
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 200 < event.pos[1] < 239:
                        if 364 < event.pos[0] < 498:
                            puissance4(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_KP1:
                    puissance4(fenetre)


def puissance4(fenetre):
    n = 0  # number of pion on tray
    fenetre.blit(pygame.image.load("puissance4/tray.png").convert(), (0, 0))
    pygame.display.flip()
    background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]  # 0=no pions, 1=red pions, 2=yellow pions
    full = 0  # 0=column is not full, 1=column is full
    w = 0  # 0=no winner
    player = randint(1, 2)  # player who begining (yellow(jaune)=1 red(rouge)=2)
    tyellow = pygame.image.load("puissance4/tyellow.png").convert()
    tred = pygame.image.load("puissance4/tred.png").convert()
    while True:
        while True:
            if n > 41:  # tray is full
                fenetre.blit(pygame.image.load("puissance4/equality.png").convert(), (245, 100))
                pygame.display.flip()
                menu(fenetre)
            if player == 1:  # display the player who play
                fenetre.blit(tyellow, (500, 550))
                pygame.display.flip()
            else:
                fenetre.blit(tred, (500, 550))
                pygame.display.flip()
            col = selectcol()  # player select a column
            for k in range(6):  # search if the player can select the column
                if background[col][k] == 0:
                    background[col][k] = player
                    tray(k, col, player, fenetre)
                    break
                if k == 5:
                    full = 1
            if full == 0:
                break
            full = 0
        n += 1  # pion is place
        if player == 1:
            player = 2
        else:
            player = 1
        if n > 6:
            w = winner(background, fenetre)
            return


def selectcol():  # player select a column for place his pion
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                closemenu.closemenu(fenetre)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 10 < event.pos[1] < 525:
                        if 31 < event.pos[0] < 103:
                            return 0
                        if 118 < event.pos[0] < 187:
                            return 1
                        if 202 < event.pos[0] < 272:
                            return 2
                        if 287 < event.pos[0] < 357:
                            return 3
                        if 373 < event.pos[0] < 443:
                            return 4
                        if 457 < event.pos[0] < 527:
                            return 5
                        if 542 < event.pos[0] < 612:
                            return 6
            if event.type == KEYDOWN:
                if event.key == K_KP1:
                    return 0
                if event.key == K_KP2:
                    return 1
                if event.key == K_KP3:
                    return 2
                if event.key == K_KP4:
                    return 3
                if event.key == K_KP5:
                    return 4
                if event.key == K_KP6:
                    return 5
                if event.key == K_KP7:
                    return 6


def winner(b, fenetre):  # return the player winner or 0
    if line(b)[0] == 1:
        result(line(b)[1], line(b)[2], line(b)[3], line(b)[4], line(b)[5], line(b)[6], line(b)[7], line(b)[8],
               line(b)[9], fenetre)
        return 1
    if column(b)[0] == 1:
        result(column(b)[1], column(b)[2], column(b)[3], column(b)[4], column(b)[5], column(b)[6], column(b)[7],
               column(b)[8], column(b)[9], fenetre)
        return 1
    if diaglltr(b)[0] == 1:
        result(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6],
               diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9], fenetre)
        return 1
    if diagtllr(b)[0] == 1:
        result(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6],
               diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9], fenetre)
        return 1
    if line(b)[0] == 2:
        result(line(b)[1], line(b)[2], line(b)[3], line(b)[4], line(b)[5], line(b)[6], line(b)[7], line(b)[8],
               line(b)[9], fenetre)
        return 2
    if column(b)[0] == 2:
        result(column(b)[1], column(b)[2], column(b)[3], column(b)[4], column(b)[5], column(b)[6], column(b)[7],
               column(b)[8], column(b)[9], fenetre)
        return 2
    if diaglltr(b)[0] == 2:
        result(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6],
               diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9], fenetre)
        return 2
    if diagtllr(b)[0] == 2:
        result(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6],
               diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9], fenetre)
        return 2
    return 0


def line(b):  # watch if we have 4 pion aligned in line
    for l in range(6):
        for k in range(4):
            if b[k][l] == b[k + 1][l] == b[k + 2][l] == b[k + 3][l] == 1:
                return [1, b, k, l, k + 1, l, k + 2, l, k + 3, l]
            if b[k][l] == b[k + 1][l] == b[k + 2][l] == b[k + 3][l] == 2:
                return [2, b, k, l, k + 1, l, k + 2, l, k + 3, l]
    return [0]


def column(b):  # watch if we have 4 pion aligned in column
    for k in range(7):
        for l in range(3):
            if b[k][l] == b[k][l + 1] == b[k][l + 2] == b[k][l + 3] == 1:
                return [1, b, k, l, k, l + 1, k, l + 2, k, l + 3]
            if b[k][l] == b[k][l + 1] == b[k][l + 2] == b[k][l + 3] == 2:
                return [2, b, k, l, k, l + 1, k, l + 2, k, l + 3]
    return [0]


def diaglltr(b):  # watch if we have 4 pion aligned in diagonal (downleft-upright)
    for k in range(4):
        for l in range(3):
            if b[k][l] == b[k + 1][l + 1] == b[k + 2][l + 2] == b[k + 3][l + 3] == 1:
                return [1, b, k, l, k + 1, l + 1, k + 2, l + 2, k + 3, l + 3]
            if b[k][l] == b[k + 1][l + 1] == b[k + 2][l + 2] == b[k + 3][l + 3] == 2:
                return [2, b, k, l, k + 1, l + 1, k + 2, l + 2, k + 3, l + 3]
    return [0]


def diagtllr(b):  # watch if we have 4 pion aligned in diagonal (upleft-downright)
    for k in range(4):
        for l in range(3):
            if b[k][5 - l] == b[k + 1][4 - l] == b[k + 2][3 - l] == b[k + 3][2 - l] == 1:
                return [1, b, k, 5 - l, k + 1, 4 - l, k + 2, 3 - l, k + 3, 2 - l]
            if b[k][5 - l] == b[k + 1][4 - l] == b[k + 2][3 - l] == b[k + 3][2 - l] == 2:
                return [2, b, k, 5 - l, k + 1, 4 - l, k + 2, 3 - l, k + 3, 2 - l]
    return [0]


def tray(coord1, coord2, color, fenetre):  # display pion
    pioncollin = [coord1, coord2]  # pion coordinate
    c = [440 + pioncollin[0] * -85, 28 + pioncollin[1] * 85]  # center of the first pion in down-left
    if color == 1:
        piony = pygame.image.load("puissance4/piony.png").convert()
        fenetre.blit(piony, (c[1], c[0]))
    else:
        pionr = pygame.image.load("puissance4/pionr.png").convert()
        fenetre.blit(pionr, (c[1], c[0]))
    pygame.display.flip()


def result(b, k1, c1, k2, c2, k3, c3, k4, c4, fenetre):  # display 4 pion which player can win
    tkey=pygame.key.get_pressed()
    while not tkey[K_ESCAPE]:
        clock=pygame.time.Clock()
        tkey=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type== QUIT:
                closemenu.closemenu(fenetre)
        fenetre.blit(pygame.image.load("puissance4/tray.png").convert(), (0, 0))
        c = b[k1][c1]
        tray(c1, k1, c,fenetre)
        tray(c2, k2, c, fenetre)
        tray(c3, k3, c, fenetre)
        tray(c4, k4, c, fenetre)
        if b[k1][c1] == 1:
            fenetre.blit(pygame.image.load("puissance4/wyellow.png").convert(), (80, 525))
        else:
            fenetre.blit(pygame.image.load("puissance4/wred.png").convert(), (80, 525))
        clock.tick(60)
        pygame.display.flip()
    return
