# Importa as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Para o MDP, é necessário que a representação de cada estado seja suficiente para que o agente tome suas decisões
# O que deve depender apenas do último estado

# Para isso, é definida uma função de recompensa, para definir quanto voce ganha indo de um estado para outro
# Além disso, é definida uma função de transição, para mudança de estado, indicando qual estado voce esta, e qual a probabilidade de ir para outro
# Essas partes foram definidas na classe GridWorld.

# A política de ações serve para dar uma ação para cada estado que voce esta
# O objetivo é encontrar a politica otima, que é aquela que 
# maximiza uma utilidade (valor) esperada a ser seguida
# Para isso, sao feitas as seguintes definições:

# Define a classe do valor das iterações
class ValueIteration:
    # Inicializa os parametros a partir das funções importadas da classe GridWorld
    def __init__(self, reward_function, transition_model, gamma):
        self.num_states = transition_model.shape[0]
        self.num_actions = transition_model.shape[1]
        self.reward_function = np.nan_to_num(reward_function)
        self.transition_model = transition_model
        self.gamma = gamma
        self.values = np.zeros(self.num_states)
        self.policy = None

    # Método que atualiza os valores dos estados em uma única iteração do algoritmo
    # Ele utiliza a equação de Ballman para atualizar os valores, de forma que a política otima deve ser encontrada em
    # uma das iterações ate a convergencia
    # Ajusta as utilidades até que as mudanças sejam suficientemente pequenas
    def one_iteration(self):
        delta = 0
        for s in range(self.num_states):
            temp = self.values[s]
            v_list = np.zeros(self.num_actions) # Serão armazenados os valores de cada casa
            
            # Para cada ação, ele tenta encontrar o melhor modelo de transição para os próximos estados, dada a ação atual no estado atual
            # Depois ele calcula o valor esperado com base na função de recompensa e a soma ponderada dos valores das utilidades dos proximos estados
            # Tambem é incluido o gama, que é o chamado fator de desconto, serve para resolver o problema de fluxos de recompensa infinitos
            for a in range(self.num_actions):
                p = self.transition_model[s, a]
                v_list[a] = self.reward_function[s] + self.gamma * np.sum(p * self.values)

            # Atualiza para o maior valor encontrado, porque este sera a melhor escolha de valor
            self.values[s] = max(v_list)
            # É essa parte que verifica se o algoritmo esta convergindo ou nao, para monitorar o algoritmo
            delta = max(delta, abs(temp - self.values[s]))
        return delta

    # Essa função deriva a política ótima a partir das utilidades (valores) calculadas
    # Determina a melhor ação a ser tomada em cada estado, escolhendo a ação que maximiza a utilidade esperada
    # Converte as utilidades em uma política que pode ser aplicada ao MDP
    
    # Assim, é chamado após as utilidades terem sido calculadas e convergidas, para gerar a política final com base nesses valores
    def get_policy(self):
        # Inicialmente todas as ações sao -1 pois ainda nao foram determinadas
        pi = np.ones(self.num_states) * -1
        
        # Busca a melhor ação para cada estado
        # Mesma logica do metodo anterior
        #  Serve para calcular as utilidades esperadas das ações com base nas utilidades já calculadas
        for s in range(self.num_states):
            v_list = np.zeros(self.num_actions)
            for a in range(self.num_actions):
                p = self.transition_model[s, a]
                v_list[a] = self.reward_function[s] + self.gamma * np.sum(p * self.values)

            max_index = []
            max_val = np.max(v_list)
            for a in range(self.num_actions):
                if v_list[a] == max_val:
                    max_index.append(a)
            pi[s] = np.random.choice(max_index)
            
        # Retorna um array que representa a política, ou seja, a ação ótima a ser tomada em cada estado
        return pi.astype(int)

    # Treina o modelo de iteração de valores até que as utilidades dos estados converjam e a política ótima seja derivada
    # Assim, é ele que controla o processo de atualização das utilidades dos estados até que elas converjam a um valor estável
    # e então gera a política ótima com base nessas utilidades
    def train(self, tol=1e-3, plot=True):
        # Contador de iterações
        epoch = 0
        # Calcula e atualiza as utilidades dos estados pela primeira vez
        delta = self.one_iteration()
        # Armazena os valores de delta ao longo das iterações
        delta_history = [delta]
        
        # Enquanto a maior mudança nas utilidades for maior que a tolerância, realiza o loop
        # A tolerancia indica o quão pequeno deve ser o valor de delta para considerar que o algoritmo convergiu
        # Vai atualizando o contador de epocas a cada vez que o loop é rodado
        # Recalcula as iterações
        while delta > tol:
            epoch += 1
            delta = self.one_iteration()
            delta_history.append(delta)
            if delta < tol:
                break
            
        # Após a convergência das utilidades, determina a política ótima com base nas utilidades calculadas
        self.policy = self.get_policy()

        # Cria o gráfico mostrando as iterações
        if plot is True:
            fig, ax = plt.subplots(1, 1, figsize=(3, 2), dpi=200)
            ax.plot(np.arange(len(delta_history)) + 1, delta_history, marker='o', markersize=4,
                    alpha=0.7, color='#2ca02c', label=r'$\gamma= $' + f'{self.gamma}')
            ax.set_xlabel('Iteration')
            ax.set_ylabel('Delta')
            ax.legend()
            plt.tight_layout()
            plt.show()







