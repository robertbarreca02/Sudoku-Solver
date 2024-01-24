import sys
import pygame as pg
import numpy as np
import requests

pg.init()
screen_size = 750, 750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 80)

# fetch board from api(only generates one solution 9x9 sudoku boards)
url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"
req = requests.get(url)
response = req.json()
board = np.array(response.get("newboard").get("grids")[0].get("value"))


def draw_board():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)

    for i in range(80, 720, 80):
        line_width = 3 if i % 240 > 3 else 10
        pg.draw.line(
            screen,
            pg.Color("black"),
            pg.Vector2((i) + 15, 15),
            pg.Vector2((i) + 15, 725),
            line_width,
        )
        pg.draw.line(
            screen,
            pg.Color("black"),
            pg.Vector2(15, (i) + 15),
            pg.Vector2(725, (i) + 15),
            line_width,
        )
        i += 80


def draw_nums():
    for row in range(9):
        for col in range(9):
            curr_num = board[row][col]
            if curr_num == 0:
                continue
            num_text = font.render(str(curr_num), True, pg.Color("black"))
            screen.blit(num_text, pg.Vector2((col * 80) + 40, (row * 80) + 35))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    draw_board()
    draw_nums()
    pg.display.flip()
