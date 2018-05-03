
import pygame, random, copy, closemenu
from pygame.locals import *

cBack = pygame.image.load('minijeu/Blackjack/cartes/cardback.png')
diamondA = pygame.image.load('minijeu/Blackjack/cartes/ad.png')
clubA = pygame.image.load('minijeu/Blackjack/cartes/ac.png')
heartA = pygame.image.load('minijeu/Blackjack/cartes/ah.png')
spadeA = pygame.image.load('minijeu/Blackjack/cartes/as.png')
diamond2 = pygame.image.load('minijeu/Blackjack/cartes/2d.png')
club2 = pygame.image.load('minijeu/Blackjack/cartes/2c.png')
heart2 = pygame.image.load('minijeu/Blackjack/cartes/2h.png')
spade2 = pygame.image.load('minijeu/Blackjack/cartes/2s.png')
diamond3 = pygame.image.load('minijeu/Blackjack/cartes/3d.png')
club3 = pygame.image.load('minijeu/Blackjack/cartes/3c.png')
heart3 = pygame.image.load('minijeu/Blackjack/cartes/3h.png')
spade3 = pygame.image.load('minijeu/Blackjack/cartes/3s.png')
diamond4 = pygame.image.load('minijeu/Blackjack/cartes/4d.png')
club4 = pygame.image.load('minijeu/Blackjack/cartes/4c.png')
heart4 = pygame.image.load('minijeu/Blackjack/cartes/4h.png')
spade4 = pygame.image.load('minijeu/Blackjack/cartes/4s.png')
diamond5 = pygame.image.load('minijeu/Blackjack/cartes/5d.png')
club5 = pygame.image.load('minijeu/Blackjack/cartes/5c.png')
heart5 = pygame.image.load('minijeu/Blackjack/cartes/5h.png')
spade5 = pygame.image.load('minijeu/Blackjack/cartes/5s.png')
diamond6 = pygame.image.load('minijeu/Blackjack/cartes/6d.png')
club6 = pygame.image.load('minijeu/Blackjack/cartes/6c.png')
heart6 = pygame.image.load('minijeu/Blackjack/cartes/6h.png')
spade6 = pygame.image.load('minijeu/Blackjack/cartes/6s.png')
diamond7 = pygame.image.load('minijeu/Blackjack/cartes/7d.png')
club7 = pygame.image.load('minijeu/Blackjack/cartes/7c.png')
heart7 = pygame.image.load('minijeu/Blackjack/cartes/7h.png')
spade7 = pygame.image.load('minijeu/Blackjack/cartes/7s.png')
diamond8 = pygame.image.load('minijeu/Blackjack/cartes/8d.png')
club8 = pygame.image.load('minijeu/Blackjack/cartes/8c.png')
heart8 = pygame.image.load('minijeu/Blackjack/cartes/8h.png')
spade8 = pygame.image.load('minijeu/Blackjack/cartes/8s.png')
diamond9 = pygame.image.load('minijeu/Blackjack/cartes/9d.png')
club9 = pygame.image.load('minijeu/Blackjack/cartes/9c.png')
heart9 = pygame.image.load('minijeu/Blackjack/cartes/9h.png')
spade9 = pygame.image.load('minijeu/Blackjack/cartes/9s.png')
diamond10 = pygame.image.load('minijeu/Blackjack/cartes/10d.png')
club10 = pygame.image.load('minijeu/Blackjack/cartes/10c.png')
heart10 = pygame.image.load('minijeu/Blackjack/cartes/10h.png')
spade10 = pygame.image.load('minijeu/Blackjack/cartes/10s.png')
diamondJ = pygame.image.load('minijeu/Blackjack/cartes/jd.png')
clubJ = pygame.image.load('minijeu/Blackjack/cartes/jc.png')
heartJ = pygame.image.load('minijeu/Blackjack/cartes/jh.png')
spadeJ = pygame.image.load('minijeu/Blackjack/cartes/js.png')
diamondQ = pygame.image.load('minijeu/Blackjack/cartes/qd.png')
clubQ = pygame.image.load('minijeu/Blackjack/cartes/qc.png')
heartQ = pygame.image.load('minijeu/Blackjack/cartes/qh.png')
spadeQ = pygame.image.load('minijeu/Blackjack/cartes/qs.png')
diamondK = pygame.image.load('minijeu/Blackjack/cartes/kd.png')
clubK = pygame.image.load('minijeu/Blackjack/cartes/kc.png')
heartK = pygame.image.load('minijeu/Blackjack/cartes/kh.png')
spadeK = pygame.image.load('minijeu/Blackjack/cartes/ks.png')

black = (0, 0, 0)
white = (255, 255, 255)
gris = (192, 192, 192)

cartes = [diamondA, clubA, heartA, spadeA,
         diamond2, club2, heart2, spade2,
         diamond3, club3, heart3, spade3,
         diamond4, club4, heart4, spade4,
         diamond5, club5, heart5, spade5,
         diamond6, club6, heart6, spade6,
         diamond7, club7, heart7, spade7,
         diamond8, club8, heart8, spade8,
         diamond9, club9, heart9, spade9,
         diamond10, club10, heart10, spade10,
         diamondJ, clubJ, heartJ, spadeJ,
         diamondQ, clubQ, heartQ, spadeQ,
         diamondK, clubK, heartK, spadeK]
carteA = [diamondA, clubA, heartA, spadeA]
carte2 = [diamond2, club2, heart2, spade2]
carte3 = [diamond3, club3, heart3, spade3]
carte4 = [diamond4, club4, heart4, spade4]
carte5 = [diamond5, club5, heart5, spade5]
carte6 = [diamond6, club6, heart6, spade6]
carte7 = [diamond7, club7, heart7, spade7]
carte8 = [diamond8, club8, heart8, spade8]
carte9 = [diamond9, club9, heart9, spade9]
carte10 = [diamond10, club10, heart10, spade10,
          diamondJ, clubJ, heartJ, spadeJ,
          diamondQ, clubQ, heartQ, spadeQ,
          diamondK, clubK, heartK, spadeK]


def getAmt(carte):
    if carte in carteA:
        return 11
    elif carte in carte2:
        return 2
    elif carte in carte3:
        return 3
    elif carte in carte4:
        return 4
    elif carte in carte5:
        return 5
    elif carte in carte6:
        return 6
    elif carte in carte7:
        return 7
    elif carte in carte8:
        return 8
    elif carte in carte9:
        return 9
    elif carte in carte10:
        return 10
    else:
        exit()


def genCarte(cList, xList):
    cA = 0
    carte = random.choice(cList)
    cList.remove(carte)
    xList.append(carte)
    if carte in carteA:
        cA = 1
    return carte, cA


def initGame(cList, uList, dList):
    userA = 0
    dealA = 0
    carte1, cA = genCarte(cList, uList)
    userA += cA
    carte2, cA = genCarte(cList, dList)
    dealA += cA
    carte3, cA = genCarte(cList, uList)
    userA += cA
    carte4, cA = genCarte(cList, dList)
    dealA += cA
    return getAmt(carte1) + getAmt(carte3), userA, getAmt(carte2) + getAmt(carte4), dealA


def blackjack(fenetre):
    ccartes = copy.copy(cartes)
    stand = False
    userCarte = []
    dealCarte = []
    winNum = 0
    loseNum = 0

    fenetre = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Piocher', 1, black)
    standTxt = font.render('Rester', 1, black)
    restartTxt = font.render('Rejouer', 1, black)
    quitTxt = font.render('Quitter', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGame(ccartes, userCarte, dealCarte)

    background = pygame.Surface(fenetre.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    hitB = pygame.draw.rect(background, gris, (10, 445, 75, 25))
    standB = pygame.draw.rect(background, gris, (95, 445, 75, 25))
    ratioB = pygame.draw.rect(background, gris, (555, 420, 75, 50))
    nbrorfi = open("save1/invent/cpic", "r")
    nbror = int(nbrorfi.read())
    nbrorfi.close()

    while 1:
        if (userSum >= 21 and userA == 0) or len(userCarte) == 5:
            gameover = True
        else:
            gameover=False
        if len(userCarte) == 2 and userSum == 21:
            gameover = True
        elif len(dealCarte) == 2 and dealSum == 21:
            gameover = True

        winTxt = font.render('Gagné: %i' % winNum, 1, black)
        loseTxt = font.render('Perdu: %i' % loseNum, 1, black)


        for event in pygame.event.get():
            if event.type == QUIT:
                nbrorfi = open("save1/invent/cpic", "w")
                nbrorfi.write(str(nbror))
                nbrorfi.close()
                closemenu.closemenu(fenetre)
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(
                    pygame.mouse.get_pos()):
                carte, cA = genCarte(ccartes, userCarte)
                userA += cA
                userSum += getAmt(carte)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    carte, cA = genCarte(ccartes, dealCarte)
                    dealA += cA
                    dealSum += getAmt(carte)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()) and nbror>=10:
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCarte) == 5:
                    winNum += 1
                    nbror += 10
                elif 21 >= userSum > dealSum or dealSum > 21:
                    winNum += 1
                    nbror+=10
                else:
                    loseNum += 1
                    nbror-=10
                gameover = False
                stand = False
                userCarte = []
                dealCarte = []
                ccartes = copy.copy(cartes)
                userSum, userA, dealSum, dealA = initGame(ccartes, userCarte, dealCarte)
                restartB = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and quitB.collidepoint(pygame.mouse.get_pos()):
                nbrorfi = open("save1/invent/cpic", "w")
                nbrorfi.write(str(nbror))
                nbrorfi.close()
                return
        print(nbror)
        fenetre.blit(background, (0, 0))
        fenetre.blit(hitTxt, (39, 448))
        fenetre.blit(standTxt, (116, 448))
        fenetre.blit(winTxt, (565, 423))
        fenetre.blit(loseTxt, (565, 448))
        fenetre.blit(font.render("Vous avez "+str(nbror)+" or", True, gris), (565,473))
        for carte in dealCarte:
            x = 10 + dealCarte.index(carte) * 110
            fenetre.blit(carte, (x, 10))
        fenetre.blit(cBack, (120, 10))

        for carte in userCarte:
            x = 10 + userCarte.index(carte) * 110
            fenetre.blit(carte, (x, 295))

        if gameover or stand:
            if nbror>=10:
                fenetre.blit(gameoverTxt, (270, 200))
                restartB = pygame.draw.rect(background, gris, (270, 225, 75, 25))
                quitB = pygame.draw.rect(background, gris, (270, 255, 75, 25))
                fenetre.blit(restartTxt, (287, 228))
                fenetre.blit(quitTxt, (287, 258))
                fenetre.blit(dealCarte[1], (120, 10))
            else:
                fenetre.blit(gameoverTxt, (270, 200))
                quitB = pygame.draw.rect(background, gris, (270, 255, 75, 25))
                fenetre.blit(quitTxt, (287, 258))
                fenetre.blit(dealCarte[1], (120, 10))


        pygame.display.flip()

