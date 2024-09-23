from sklearn import linear_model
import matplotlib.pyplot as plt

# Este código tem como objetivo fazer previsões de qual seria a nota de um aluno, dada a quantidade de livros que ele leu e qual sua frequencia ao longo do semestre
# Isto é feito por meio do método dos mínimos quadrados, usando regressão linear a partir de um conjunto de dados fornecido com as relações entre livros, frequencia e nota dos alunos

# informações de cada aluno
#livros lidos
livros = [0, 1, 0, 2, 4, 4, 1, 4, 3, 0, 2, 1, 4, 1, 0, 1, 3, 0, 1, 4, 4, 0, 2, 3, 1, 0, 3, 3, 2, 2, 3, 2, 2, 3, 4, 4, 3, 1, 2, 0]

#frequecia nas aulas
frequencia = [9, 15, 10, 16, 10, 20, 11, 20, 15, 15, 8, 13, 18, 10, 8, 10, 16, 11, 19, 12, 11, 19, 15, 15, 20, 6, 15, 19, 14, 13, 17, 20, 11, 20, 20, 20, 9, 8, 16, 10]

#vetor que junta livros e frquencia
entrada = [[0, 9], [1, 15], [0, 10], [2, 16], [4, 10], [4, 20], [1, 11], [4, 20], [3, 15], [0, 15],
            [2, 8], [1, 13], [4, 18], [1, 10], [0, 8], [1, 10], [3, 16], [0, 11], [1, 19], [4, 12],
            [4, 11], [0, 19], [2, 15], [3, 15], [1, 20], [0, 6], [3, 15], [3, 19], [2, 14], [2, 13], 
            [3, 17], [2, 20], [2, 11], [3, 20], [4, 20], [4, 20], [3, 9], [1, 8], [2, 16], [0, 10]]

#notas
notas = [45, 57, 45, 51, 65, 88, 44, 87, 89, 59, 66, 65, 56, 47, 66, 41, 56, 37, 45, 58, 47, 64, 97, 55, 51, 61, 69, 79, 71, 62, 87, 54, 43, 92, 83, 94, 60, 56, 88, 62]


# cria um grafico 3D sem a previsão
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plota os pontos
ax.scatter(livros, frequencia, notas)


# Adiciona rótulos aos eixos
#figura sem previsao
ax.set_xlabel('Livros')
ax.set_ylabel('Aulas')
ax.set_zlabel('Notas')


# comandos para importar e realizar a regressão linear
regressao = linear_model.LinearRegression()
regressao.fit(entrada, notas)

a = regressao.coef_ # "a" é o coeficiente angular para a equação da reta
b = regressao.intercept_ # "b" é o coeficiente linear para a equação da reta
print("Coef Angular:", a, "Coef Linear:", b)


# realiza a previsao de nota dos alunos de acordo com as entradas de livros e frequencias
previsao = regressao.predict([[2, 11],[0, 5],[4, 10],[2, 10],[4, 15]])
print("Previsao: ", previsao)

# calcula a precisao das previsoes
precisao = regressao.score(entrada, notas)
print("Precisão: ", precisao)


# Mostra o gráfico
plt.show()
input()