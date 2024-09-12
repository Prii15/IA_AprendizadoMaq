import skfuzzy
from skfuzzy import control
import numpy as np
import matplotlib.pyplot as plt

#Input parameters
#Type of clothes (TC)
#Amount of clothes (AC)
#Amount of dirtiness (AD)

#Output parameters
#Wash time (Wash)
#Rinse time (Rinse)
#Spin time (Spin)

tc = control.Antecedent(np.arange(0, 100, 1), 'tc')
ac = control.Antecedent(np.arange(0, 10, 1), 'ac')
ad = control.Antecedent(np.arange(0, 100, 1), 'ad')

wash = control.Consequent(np.arange(0, 50, 1), 'wash')
rinse = control.Consequent(np.arange(0, 60, 1), 'rinse')
spin = control.Consequent(np.arange(0, 180, 1), 'spin')

# (TC) thin ,thick, and jeans are [-50 0 50], [20 50 80] and [50 100 150]
# (AC) little, normal, and large are [ -5 0 5], [2 5 8], and [5 10 15] 
# (AD) small [-50 0 50], normal [20 50 80], and large [50 100 150]

tc['thin'] = skfuzzy.trimf(tc.universe, [-50, 0, 50])
tc['thick'] = skfuzzy.trimf(tc.universe, [20, 50, 80])
tc['jeans'] = skfuzzy.trimf(tc.universe, [50, 100, 150])

ac['pouca'] = skfuzzy.trimf(ac.universe, [-5, 0, 5])
ac['media'] = skfuzzy.trimf(ac.universe, [2, 5, 8])
ac['muita'] = skfuzzy.trimf(ac.universe, [5, 10, 15])

ad['pouca'] = skfuzzy.trimf(ad.universe, [-50, 0, 50])
ad['media'] = skfuzzy.trimf(ad.universe, [20, 50, 80])
ad['muita'] = skfuzzy.trimf(ad.universe, [50, 100, 150])

# Rinse time very small, small, normal, long, and very long are [-12.5 0 12.5], [0 12.5 25],
# [15 25 35], [25 35 45], [40 60 80].

# washing time small, normal and large are [-20 0 20],[10 25 40] and [35 50 50]

# f Spin time very small, small, normal, large and
# very large [0 0 40], [30 52.5 75], [50 75 100], [75 107.5 140], [120 180 480] 

rinse['verysmall'] = skfuzzy.trimf(rinse.universe, [-12.5, 0, 12.5])
rinse['small'] = skfuzzy.trimf(rinse.universe, [0, 12.5, 25])
rinse['normal'] = skfuzzy.trimf(rinse.universe, [15, 25, 35])
rinse['long'] = skfuzzy.trimf(rinse.universe, [25, 35, 45])
rinse['verylong'] = skfuzzy.trimf(rinse.universe, [40, 60, 80])

wash['small'] = skfuzzy.trimf(wash.universe, [-20, 0, 20])
wash['normal'] = skfuzzy.trimf(wash.universe, [10, 25, 40])
wash['large'] = skfuzzy.trimf(wash.universe, [35, 50, 50])

spin['verysmall'] = skfuzzy.trimf(spin.universe, [0, 0, 40])
spin['small'] = skfuzzy.trimf(spin.universe, [30, 52.5, 75])
spin['normal'] = skfuzzy.trimf(spin.universe, [50, 75, 100])
spin['large'] = skfuzzy.trimf(spin.universe, [75, 107.5, 140])
spin['verylarge'] = skfuzzy.trimf(spin.universe, [120, 180, 180])

tc.view()
ac.view()
ad.view()
rinse.view()
wash.view()
spin.view()
plt.show()

input()

regra1 = control.Rule(ac['large'] & ad['large'], rinse['long'])
regra2 = control.Rule(ac['little'] & ad['small'], rinse['verysmall'])
regra3 = control.Rule(ac['normal'] & ad['normal'], rinse['normal'])
regra4 = control.Rule(ac['normal'] & ad['small'], rinse['small'])
regra5 = control.Rule(ac['large'] & ad['normal'], rinse['long'])
regra6 = control.Rule(ac['normal'] & ad['large'], rinse['verylong'])
regra7 = control.Rule(ac['large'] & ad['small'], rinse['long'])
regra8 = control.Rule(ac['little'] & ad['large'], rinse['long'])

regra9 = control.Rule(ac['little'] & ad['small'], wash['small'])
regra10 = control.Rule(ac['normal'] & ad['small'], wash['small'])
regra11 = control.Rule(ac['large'] & ad['small'], wash['normal'])
regra12 = control.Rule(ac['little'] & ad['normal'], wash['small'])
regra13 = control.Rule(ac['normal'] & ad['normal'], wash['normal'])
regra14 = control.Rule(ac['large'] & ad['normal'], wash['large'])
regra15 = control.Rule(ac['little'] & ad['large'], wash['normal'])
regra16 = control.Rule(ac['normal'] & ad['large'], wash['large'])
regra17 = control.Rule(ac['large'] & ad['large'], wash['large'])

regra18 = control.Rule(tc['thin'] & ac['little'], spin['verysmall'])
regra19 = control.Rule(tc['jean'] & ac['large'], spin['verylarge'])
regra20 = control.Rule(tc['thin'] & ac['normal'], spin['small'])
regra21 = control.Rule(tc['thick'] & ac['normal'], spin['large'])
regra22 = control.Rule(tc['thick'] & ac['little'], spin['normal'])
regra23 = control.Rule(tc['thick'] & ac['large'], spin['large'])
regra24 = control.Rule(tc['thin'] & ac['large'], spin['normal'])
regra25 = control.Rule(tc['jean'] & ac['normal'], spin['large'])
regra26 = control.Rule(tc['jean'] & ac['little'], spin['normal'])


regras = control.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18, regra19, regra20, regra21, regra22, regra23, regra24, regra25, regra26])

resultado = control.ControlSystemSimulation(regras)

