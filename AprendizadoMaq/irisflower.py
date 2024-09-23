# KNN Regressão

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Este código tem como objetivo classificar o conjunto de dados de flores de íris através do método KNN

# importação dos dados das flores
# iris_X sao informações das flores, e iris_y sao as especies
iris_X, iris_y = load_iris(return_X_y=True)

# é necessario transformar os dados das especies das flores em um array, para relacionar os nomes com números
iris_y_np = np.array(iris_y)
especies = np.empty(iris_y_np.shape, dtype='U10')

# correspondencia das especieis com numeros
especies[iris_y_np == 0] = "setosa"
especies[iris_y_np == 1] = "versicolor"
especies[iris_y_np == 2] = "virginica"

# cria a classificação para o KNN com 5 vizinhos
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(iris_X, especies)

# realiza a previsao qual especie a flor é de acordo com suas caracteristicas, mostrando a probabilidade de ser daquela especie
print("Previsao da espécie da flor: ", str(knn.predict([[4.9, 3.0, 1.4, 0.2]])))
print("Probabilidade de ser dessa espécie: ", knn.predict_proba([[4.9, 3.0, 1.4, 0.2]]))

print("Previsao da espécie da flor: ", str(knn.predict([[6.9, 3.1, 4.9, 1.5]])))
print("Probabilidade de ser dessa espécie: ", knn.predict_proba([[6.9, 3.1, 4.9, 1.5]]))

print("Previsao da espécie da flor: ", str(knn.predict([[7.3, 2.9, 6.3, 1.8]])))
print("Probabilidade de ser dessa espécie: ", knn.predict_proba([[7.3, 2.9, 6.3, 1.8]]))

# calcula a precisao das previsoes
precisao = knn.score(iris_X, especies)
print("Precisão: ", precisao)

# monta o gráfico
# em azul a distribuição da especie setosa
for i in range(50):
    plt.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], color="blue")
    
# em vermelho a distribuição da especie vesicolor
for i in range(50, 100):
    plt.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], color="red")
    
# em verde a distribuição da especie virginica
for i in range(100, 150):
    plt.scatter(iris_X[i][0], iris_X[i][1], iris_X[i][2], color="green")


# Mostra o gráfico
plt.show()
input()

