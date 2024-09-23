import skfuzzy
from skfuzzy import control
import numpy as np
import matplotlib.pyplot as plt

comida = control.Antecedent(np.arange(0, 10.1, 0.1), 'comida')
servico = control.Antecedent(np.arange(0, 10.1, 0.1), 'servico')
gorjeta = control.Consequent(np.arange(5, 25.1, 0.1), 'gorjeta')


comida['ruim'] = skfuzzy.zmf(comida.universe, 0, 5)
comida['boa'] = skfuzzy.gaussmf(comida.universe, 5, 1)
comida['otima'] = skfuzzy.smf(comida.universe, 5, 10)

servico['ruim'] = skfuzzy.zmf(servico.universe, 0, 5)
servico['bom'] = skfuzzy.gaussmf(servico.universe, 5, 1)
servico['otimo'] = skfuzzy.smf(servico.universe, 5, 10)

gorjeta['pouca'] = skfuzzy.trimf(gorjeta.universe, [5, 5, 15])
gorjeta['media'] = skfuzzy.trimf(gorjeta.universe, [5, 15, 25])
gorjeta['muita'] = skfuzzy.trimf(gorjeta.universe, [15, 25, 25])



comida['boa'].view()
servico.view()
gorjeta.view()
plt.show()


regra1 = control.Rule(servico['ruim'] | comida['ruim'], gorjeta['pouca'])
regra2 = control.Rule(comida['boa'], gorjeta['media'])
regra3 = control.Rule(comida['otima'] | servico['bom'], gorjeta['muita'])

regras = control.ControlSystem([regra1, regra2, regra3])

resultado = control.ControlSystemSimulation(regras)

resultado.input['comida'] = 3
resultado.input['servico'] = 7

resultado.compute()

print(resultado.output['gorjeta'])
gorjeta.view(sim=resultado)