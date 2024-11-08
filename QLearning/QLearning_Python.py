# Q_Learning no mundo de grades
# O agente recebe recompensas pelas ações executadas
# O mundo pode ser descrito por estados, e 
# em cada um deles o agente pode tomar uma ação

# PAra rand()
import random

# Para sleep()
import time

#DEFINIÇÕES

# taxa de aprendizado = 20%
Alpha = 0.2 
# fator de desconto = 90%    
Gamma = 0.9
# porcentagem de exploração = 20%     
Epsilon = 0.2   

# quantidade de estados, ações e experimentos
# 4 ações (cima, baixo, esquerda, direita)
A = 4
# 3 colunas livres e 2 paredes
COL = 5
# 3 linhas livre e duas paredes
LIN = 5
# define quantide de estados S
S = COL*LIN
# define quantidade de episódios
EPISODIOS = 50

# define a representação no mapa/mundo
LIVRE = 0
OBSTACULO = 1
SAIDA = 2

# /////////////////////////////////
#  DECLARAÇÕES GLOBAIS
# /////////////////////////////////

# matriz Q: valor estado-ação;
Q = [[0.0 for _ in range(A)] for _ in range(S)]
# posicao na grade (x, y)
x = 0
y = 0
# auxiliar de recompensa
rew = 0

# Mundo de grades:
# livre = 0
# obstaculo = 1
# saida = 2
mapa = [
    [1, 1, 1, 2, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# /////////////////////////////////
#  FUNÇÕES
# /////////////////////////////////

# inicializa função Q com numeros aleatorios 
# entre 0 e 1
def init_q(Q):
    for s in range(len(Q)):
        for a in range(len(Q[s])):
            # Atribui um número aleatório entre 0 e 1
            Q[s][a] = random.uniform(0, 1)
            

# inicio aleatorio do agente no mapa / mundo
def inicio_aleatorio():
    global x, y
    while True:
        y = random.randint(0, LIN - 1)
        x = random.randint(0, COL - 1)
        
        if mapa[y][x] != OBSTACULO and mapa[y][x] != SAIDA:
            break
    # while para testar se o agente não está começando  
    # na saída ou no obstáculo
    # so para de gerar um ponto para inicio quando
    # nao for nem obstaculo nem saida
    

# a partir de x e y cria o estado s
def estado(x, y):
    s = 0
    c = 0
    for j in range(LIN):
        for i in range(COL):
            if (x == i) and (y == j):
                s = c
            c += 1
    return s

# seleciona uma acao: estratégia e-greedy
# dados Q e s
def seleciona_acao(Q, s):
    # Encontra a ação com o valor máximo Q para o estado s
    a_qmax = 0
    for i in range(1, A):
        if Q[s][i] > Q[s][a_qmax]:
            a_qmax = i
    acao = a_qmax

    # e-greedy: 
    # escolhe a ação com Q maximo ou escolhe ação aleatória
    # gera número aleatório

    if random.uniform(0, 1) < Epsilon:
        acao = random.randint(0, A - 1)
    
    return acao

# obtém o próximo estado e verifica se colisões
# utiliza rew para armazenar colisão
def proximo_estado(a):
    global x, y, rew  # garante que estamos modificando a variável global rew
    rew = 0

    # Ações: {0: para baixo, 1: para direita, 2: para cima, 3: para esquerda}
    # para baixo
    if a == 0:  
        if mapa[y + 1][x] != 1:
            y += 1
        else:
            rew = 1
            
    # para direita
    elif a == 1:  
        if mapa[y][x + 1] != 1:
            x += 1
        else:
            rew = 1
            
    # para cima
    elif a == 2:  
        if mapa[y - 1][x] != 1:
            y -= 1
        else:
            rew = 1
            
    # para esquerda
    elif a == 3:  
        if mapa[y][x - 1] != 1:
            x -= 1
        else:
            rew = 1

    return estado(x, y)

# Retorna a recompensa com base no estado atual
# 100 caso encontre o objetivo
# -5 quando colidir
# -1 para cada ação que não resultar no objetivo
def recompensa():
    if mapa[y][x] == SAIDA:
        return 100
    
    else:
        if rew == 1:
            return -5
        
        else:
            return -1

# Atualiza o valor da matriz Q
def atualiza_q(s, a, r, Q, next_s, next_a):
    Q[s][a] += Alpha * (r + Gamma * Q[next_s][next_a] - Q[s][a])

# Desenha a política de ações no terminal
# simula o mundo
def desenha_mapa_politica(espaco, episodio):
    print("\n\n\n ===== Q-LEARNING =====\n")
    print(f"Episódio: {episodio}\n")
    
    for linha in range(LIN):
        for coluna in range(COL):
            if mapa[linha][coluna] == LIVRE:
                esp = estado(coluna, linha)
                
                # Definindo a ação
                if espaco[esp] == 0:
                    print("v", end="")  # seta para baixo
                    
                elif espaco[esp] == 1:
                    print(">", end="")  # seta para direita
                    
                elif espaco[esp] == 2:
                    print("^", end="")  # seta para cima
                    
                elif espaco[esp] == 3:
                    print("<", end="")  # seta para esquerda
                
            elif mapa[linha][coluna] == OBSTACULO:
                print("#", end="")
                
            elif mapa[linha][coluna] == SAIDA:
                print(" ", end="")
                
        print()  # nova linha após cada linha da grade


# ////////////////////////////////
#  CÓDIGO PRINCIPAL (main)
# ////////////////////////////////

def main():
    global x, y
    
    random.seed(time.time()) # para gerar os números aleatórios
    at = 0   # Ação a ser tomada
    s = 0    # Estado atual
    s_proximo = 0   # Próximo estado
    a_proximo = 0   # Próxima ação
    r = 0    # Recompensa
    episodio = 0    # Contador de episódios

    # Inicializa Q com valores aleatórios
    init_q(Q)

    # Imprime a matriz Q inicial para debug
    # linhas são estados, colunas são ações
    print("Tabela Q inicial")
    for s in range(S):
        for a in  range(A):
            print(Q[s][a], end=" ")
        print()  # Pula para a próxima linha após imprimir todas as ações do estado s
    
    # Loop principal de episódios
    # repete EPISODIOS vezes
    for episodio in range(EPISODIOS):
        inicio_aleatorio()  # Inicia o agente em uma posição aleatória
        s = estado(x, y)    # Obtém o estado inicial do agente

        # Loop até encontrar o objetivo
        while mapa[y][x] != SAIDA:
            # Seleciona uma ação com e-greedy
            # a partir de Q e s
            at = seleciona_acao(Q, s)
            # Obtém o próximo estado com a ação escolhida
            s_proximo = proximo_estado(at)
            # Calcula a recompensa recebida
            r = recompensa()
            # Seleciona a próxima ação no novo estado
            a_proximo = seleciona_acao(Q, s_proximo)
            # Atualiza o valor de Q
            atualiza_q(s, at, r, Q, s_proximo, a_proximo)
            # Atualiza o estado atual para o próximo
            s = s_proximo


        # Desenha a política a cada x episódios
        x = 5
        # Inicializa a política com uma lista de zeros de tamanho S
        politica = [0] * S  
        
        if episodio % x == 0:
            for s in range(S):
                a_qmax = 0
                for i in range(1, A):
                    if Q[s][i] > Q[s][a_qmax]:
                        a_qmax = i
                politica[s] = a_qmax
                
            # imprime na tela somente a ação que max Q
            desenha_mapa_politica(politica, episodio)
            # atualiza a cada 1 seg
            time.sleep(1)
    
    # Imprime a matriz Q inicial para debug
    # linhas são estados, colunas são ações
    print("\nTabela Q final")
    for s in range(S):
        for a in  range(A):
            print(Q[s][a], end=" ")
        print()  # Pula para a próxima linha após imprimir todas as ações do estado s
    
# Chamando a função principal
if __name__ == "__main__":
    main()
