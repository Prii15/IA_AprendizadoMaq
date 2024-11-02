# Código principal
import numpy as np

# Importando os códigos que serao utilizados
from GridWorld import GridWorld
from ValueIteration import ValueIteration

# A variavel problema inicializa a classe GridWOrld, definida no outro arquivo
# Para isso, é usado um dos mapas da pasta GridMaps, definidos em forma de matriz
# O parametro reward define as recompensas de cada casa que o robo pode andar
# Nessa classe são definidas as funções de recompensa e trasnição de estados, a partir dos parametros
# São essas funções que tornam possivel fazer a iteração de valores
# Parametros utilizados a partir do aprezentado no github do desenvolvedor do codigo
problem = GridWorld('MDP_(markov)\GridMaps\world00.csv', reward={0: -0.04, 1: 1.0, 2: -1.0, 3: np.NaN}, random_rate=0.2)


# A variavel solver inicializa a classe ValueIteration, definida no outro arquivo
# São passadas as funções de recompensa e transição de estados
solver = ValueIteration(problem.reward_function, problem.transition_model, gamma=0.9)

# Executa o algoritmo de Iteração de Valores para calcular a política ótima e o valor de cada estado
solver.train()

# Plota os gráficos da policy, que sao as ações que o agente deve tomar, e dos valores de cada estado
problem.visualize_value_policy(policy=solver.policy, values=solver.values)
# Faz uma simulação para avaliar a solver policy, testando-a repetidas vezes (no caso, 1000)
problem.random_start_policy(policy=solver.policy, start_pos=(2, 0), n=1000)

# O processo de decisão de markov (MDP) serve para a tomada de decisões sequenciais 
# Assim, utiliza-se a matematica para modelar as ações com base nao apenas no ambiente, mas tambem nas ações ja tomadas anteriormente 

# A partir da simulação, é possível concluir que nossa solver policy foi eficiente, com o robo sendo capaz de chegar ate o quadrate de destino quase sempre
# Apesar disso, vale ressaltar que apesar de esse metodo ser muito util, na vida real nem sempre da para implementa-lo
# Isso porque é necessário ter a reward e a transition function (função de recompensa e de transição), o que normalmente nao temos
# Dessa forma, fica inviavel inplementar esse metodo em situações em que voce nao entende o funcionamento do mapa, ou seja, possui essas funções
