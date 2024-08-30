import numpy
import math
from draw import *

#define ponto final e inicial do robo.
x_ini = 0
y_ini = 0

x_final = 9
y_final = 9


class A:
  
    def __init__(self):
        self.open = []
        self.closed = []
        self.position = []
        self.goal = []
        self.path = []
        self.mapa = []
        self.g = 0
    

    def inicio(self):
        #mapa
        #editar essa matriz para alterar os obstaculos
        self.mapa = numpy.array([
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],   
        [1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        
        self.start = [x_ini, y_ini]
        self.goal = [x_final, y_final]
        #coordenadas das casas visinhas
        self.check = [[0,-1],[1,0],[0,1],[-1,0],[-1,-1],[1,-1],[1,1],[-1,1]]

    #função que verifica se existem casas visinhas a casa atual e adiciona as existentes a uma lista
    def filhos(self):
        filhos = []
        for i in self.check:
            x = self.position[0] + i[0]
            y = self.position[1] + i[1]
            if x>=0 and x<len(self.mapa) and y>=0 and y<len(self.mapa[0]):
                if self.mapa[x][y] != 1:
                    filhos.append([x,y])
        return filhos
    
    #função heuristica
    def heuristica(self, x, y):
        h = math.sqrt((self.goal[0] - x)**2 + (self.goal[1] - y)**2)
        return h

    #função do custo para ir para cada casa adjacente
    def custo(self, x, y, g):
        g = g + math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        return g

    #função soma da heuristica e do custo
    def funcao(self, x, y, g):
        f = self.heuristica(x, y) + self.custo(x, y, g) 
        return f

    #algoritmo A* de busca
    def busca(self):
        self.position = self.start
        self.path.append(self.position)
        
        while self.position != self.goal:
            
            filhos = self.filhos()
            for i in filhos:
                if i not in self.open:
                    self.open.append(i)
        
            casavisitada = 1000
            for pos in self.open:
                
                if self.funcao(pos[0], pos[1], self.g) < casavisitada:
                    casavisitada = self.funcao(pos[0], pos[1], self.g)
                    self.position = pos

            self.path.append(self.position)
            print("path",self.path)

    