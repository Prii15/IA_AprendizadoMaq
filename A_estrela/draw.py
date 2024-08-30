"""
Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

cell_size = 30


def desenha_mundo(map):
    x_size = len(map)
    y_size = len(map[0])
    screen = turtle.Screen()
    screen.screensize(500, 500)
    for i in range(x_size):
        for j in range(y_size):
            t.speed(10000)
            t.color('green')
            t.penup()
            t.setposition((j * cell_size)-150, (-i * cell_size)+150)
            t.pendown()
            if map[i][j] == 1: t.begin_fill()
            t.forward(cell_size)
            t.left(90)
            t.forward(cell_size)
            t.left(90)
            t.forward(cell_size)
            t.left(90)
            t.forward(cell_size)
            t.left(90)
            if map[i][j] == 1: t.end_fill()


def desenha_destino(destino):
    x = destino[0]
    y = destino[1]

    t.speed(10000)
    t.color('blue')
    t.penup()
    t.setposition((y * cell_size)-150, (-x * cell_size)+150)
    t.pendown()
    t.begin_fill()
    t.forward(cell_size)
    t.left(90)
    t.forward(cell_size)
    t.left(90)
    t.forward(cell_size)
    t.left(90)
    t.forward(cell_size)
    t.left(90)
    t.end_fill()


def posiciona_tartaruga(inicio):
    x = inicio[0]
    y = inicio[1]

    t.shape("turtle")
    t.speed(10)
    t.color('red')
    t.penup()
    t.setposition(((y + 0.5) * cell_size)-150, ((x + 0.5) * cell_size)+150)
    t.pendown()

def move_tartaruga(lista):
    for pos in lista:
        y = pos[0]
        x = pos[1]
        t.setposition(((x + 0.5) * cell_size)-150, ((-y + 0.5) * cell_size)+150)