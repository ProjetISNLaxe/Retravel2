import pygame


with open("option\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()
retravel = pygame.image.load("launcher/retravel_logo.png").convert()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else :
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

map={}
grandemap = pygame.image.load("map/map.png").convert_alpha()
map["capitale"]=pygame.image.load("map/capitale/capitale.png").convert_alpha()
for i in range (785):
    fenetre.fill((0,0,0))
    fenetre.blit(retravel, (800-i,0))
    pygame.display.flip()
map["capitale_obstacle"]=pygame.image.load("map/capitale/capitale_obstacle.png").convert_alpha()

map["mapdepart"]=pygame.image.load("map/mapdepart/mapdepart.png").convert_alpha()
map["mapdepart_obstacle"]=pygame.image.load("map/mapdepart/mapdepart_obstacle.png").convert_alpha()

map["maison_1"]=pygame.image.load("map/maison_1/maison_1.png").convert_alpha()
map["maison_1_obstacle"]=pygame.image.load("map/maison_1/maison_1_obstacle.png").convert_alpha()

map["maison_2"]=pygame.image.load("map/maison_2/maison_2.png").convert_alpha()
map["maison_2_obstacle"]=pygame.image.load("map/maison_2/maison_2_obstacle.png").convert_alpha()

map["auberge_1F"]=pygame.image.load("map/auberge_1F/auberge_1F.png").convert_alpha()
map["auberge_1F_obstacle"]=pygame.image.load("map/auberge_1F/auberge_1F_obstacle.png").convert_alpha()

map["auberge_2F"]=pygame.image.load("map/auberge_2F/auberge_2F.png").convert_alpha()
map["auberge_2F_obstacle"]=pygame.image.load("map/auberge_2F/auberge_2F_obstacle.png").convert_alpha()

map["cheminfjord"]=pygame.image.load("map/cheminfjord/cheminfjord.png").convert_alpha()
map["cheminfjord_obstacle"]=pygame.image.load("map/cheminfjord/cheminfjord_obstacle.png").convert_alpha()

map["chateau_1F"]=pygame.image.load("map/chateau_1F/chateau_1F.png").convert_alpha()
map["chateau_1F_obstacle"]=pygame.image.load("map/chateau_1F/chateau_1F_obstacle.png").convert_alpha()

map["chateau_2F"]=pygame.image.load("map/chateau_2F/chateau_2F.png").convert_alpha()
map["chateau_2F_obstacle"]=pygame.image.load("map/chateau_2F/chateau_2F_obstacle.png").convert_alpha()

map["chateau_3F"]=pygame.image.load("map/chateau_3F/chateau_3F.png").convert_alpha()
map["chateau_3F_obstacle"]=pygame.image.load("map/chateau_3F/chateau_3F_obstacle.png").convert_alpha()