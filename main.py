import math
import pygame
from settings import *
from player import Player
from drawing import Drawing
from map import world_map



pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.mini_map(player)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick()