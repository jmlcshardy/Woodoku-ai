import pygame
from random import choice, randint
from math import floor

pygame.init()

board = [[0 for j in range(9)] for i in range(9)]

current_tile = 0

screen = pygame.display.set_mode((900, 650))
tile_size = 70

score = 0

font = pygame.font.SysFont('arial', 30)


class Tile:
    def __init__(self, tile_list):
        self.tile = tile_list
        self.size = len(self.tile)
        self.sideTile = 150/self.size

    def draw_board(self, row, col, piece):
        global board, score
        try:
            backup_board = [row[:] for row in board]
            potential_score = 0
            for i in range(self.size):
                for j in range(self.size):
                    if self.tile[j][i] == 1:
                        if board[row + i][col + j] == 1:
                            raise Exception("filled")
                        else:
                            board[row + i][col + j] = 1
                            potential_score += 1
            tiles[tiles.index(piece)] = na
            for i in range(9):
                total = 0
                for j in range(9):
                    if board[i][j] == 1:
                        total += 1
                if total == 9:
                    potential_score *= 2
                    for j in range(9):
                        board[i][j] = 0
            for i in range(9):
                total = 0
                for j in range(9):
                    if board[j][i] == 1:
                        total += 1
                if total == 9:
                    potential_score *= 2
                    for j in range(9):
                        board[j][i] = 0

            for num in range(9):
                row = (floor(num / 3 - .1)) * 3
                col = (num % 3 - 1) * 3
                total = 0
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == 1:
                            total += 1
                if total == 9:
                    potential_score *= 2
                    for i in range(row, row + 3):
                        for j in range(col, col + 3):
                            board[i][j] = 0

            score += potential_score
        except:
            board = backup_board

    def draw_side(self, x, y):
        for i in range(self.size):
            for j in range(self.size):
                if self.tile[j][i] == 1:
                    pygame.draw.rect(screen, (207, 161, 94), (x + i * self.sideTile, y + j * self.sideTile, self.sideTile - 2, self.sideTile - 2))
                else:
                    pygame.draw.rect(screen, (150, 82, 36), (x + i * self.sideTile, y + j * self.sideTile, self.sideTile - 2, self.sideTile - 2))


na = Tile(
     [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]])

tinyL = Tile(
    [[1, 0],
     [1, 1]])

shortL = Tile(
    [[1, 0, 0],
     [1, 0, 0],
     [1, 1, 0]])

longL = Tile(
    [[1, 0, 0],
     [1, 0, 0],
     [1, 1, 1]])

EEE = Tile(
    [[1, 1, 0],
     [1, 0, 0],
     [1, 1, 0]])

one = Tile(
    [[1]])

two = Tile(
    [[1, 1],
     [0, 0]])

square = Tile(
    [[1, 1],
     [1, 1]])

smallT = Tile(
    [[1, 0, 0],
     [1, 1, 0],
     [1, 0, 0]])

bigT = Tile(
    [[1, 0, 0],
     [1, 1, 1],
     [1, 0, 0]])

smallDiag = Tile(
    [[1, 0],
     [0, 1]])

mediumDiag = Tile(
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]])

bigDiag = Tile(
   [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]])

z = Tile(
    [[1, 0, 0],
     [1, 1, 0],
     [0, 1, 0]])

long = Tile(
    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]])

longer = Tile(
   [[1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]])

longest = Tile(
   [[1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])

plus = Tile([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]])

all_tiles = [tinyL, shortL, longL, EEE, one, two, square, smallT, bigT, smallDiag, mediumDiag, bigDiag, z, long, longer, longest, plus]
tiles = [na, na, na, na]


def rotate(tile, rot):
    if rot == 1:
        new_list = []
        for i in range(tile.size):
            row = []
            for j in range(tile.size):
                row.append(tile.tile[j][i])
            new_list.append(row)
    if rot == 2:
        new_list = []
        for i in range(tile.size):
            row = []
            for j in range(tile.size):
                row.append(tile.tile[i][j])
            new_list.insert(0, row)
    if rot == 3:
        new_list = []
        for i in range(tile.size):
            row = []
            for j in range(tile.size):
                row.append(tile.tile[j][i])
            row.reverse()
            new_list.append(row)
    else:
        return
    tile.tile = new_list


def main():
    global current_tile, board, tiles
    screen.fill((210, 128, 70))

    showScore = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(showScore, (710, 10))

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                pygame.draw.rect(screen, (90, 35, 2), (i * 70 + 10, j * 70 + 10, 65, 65))
            else:
                pygame.draw.rect(screen, (207, 161, 94), (i * 70 + 10, j * 70 + 10, 65, 65))

    mousePos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    mouse_square = [(mousePos[0] // tile_size), (mousePos[1] // tile_size)]
    if mouse[0] and mousePos[0] < 630:
        tiles[current_tile].draw_board(mouse_square[0], mouse_square[1], tiles[current_tile])

    mouse_hitbox = pygame.Rect((mousePos[0], mousePos[1], 1, 1))

    if tiles[1] != na:
        tiles[1].draw_side(710, 70)
    hitbox1 = pygame.Rect((710, 70, 150, 150))
    if mouse[0] and hitbox1.colliderect(mouse_hitbox):
        current_tile = 1

    if tiles[2] != na:
        tiles[2].draw_side(710, 260)
    hitbox2 = pygame.Rect((710, 260, 150, 150))
    if mouse[0] and hitbox2.colliderect(mouse_hitbox):
        current_tile = 2

    if tiles[3] != na:
        tiles[3].draw_side(710, 450)
    hitbox3 = pygame.Rect((710, 450, 150, 150))
    if mouse[0] and hitbox3.colliderect(mouse_hitbox):
        current_tile = 3

    if tiles[0] == tiles[1] == tiles[2] == tiles[3] == na:
        tiles = [na]
        for i in range(3):
            new_tile = choice(all_tiles)
            rotate(new_tile, randint(1, 4))
            tiles.append(new_tile)
        current_tile = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            quit()

    main()
    pygame.display.update()
