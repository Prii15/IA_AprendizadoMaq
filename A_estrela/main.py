from A_estrela import *
from draw import *


def main():
  # inicializa o A*
  a_star = A()
  a_star.inicio()

  desenha_mundo(a_star.mapa)
  desenha_destino(a_star.goal)
  posiciona_tartaruga(a_star.start)

  #executa algoritmo de busca A*
  a_star.busca()

  move_tartaruga(a_star.path)
  print(a_star.path)


if __name__ == "__main__":
    main()
    input()