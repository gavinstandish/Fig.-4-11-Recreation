# -*- coding: utf-8 -*-
"""
Gavin Standish
"""

import numpy as np
import matplotlib.pyplot as plt

'Creating dimensionless values for minutes, hours, and days.'

O_s = 1
O_0 = 1*10**7.5 # Incase a large integer is to be used instead of built-in 'inf' value. This value seems to result in a more accurate graph to literature values.
# O_0 = float('inf')
xrange = np.linspace(1,70,70)

min = np.linspace(1, 70, 70) * 60
hour = np.linspace(1, 70, 70) * 3600 # Conversions to seconds
day = np.linspace(1, 70, 70) * 86400

Os_min = min / O_s
Os_hour = hour / O_s
Os_day = day / O_s



'Defining fig. 4-32 equation and inputting dimensionless time values previously calculated.'

def Power(O_s, O_0):
    return ((0.1*((O_s+10)**-0.2))-(0.087*((O_s+(2*10**7))**-0.2)))-((0.1*((O_s+O_0+10)**-0.2))-(0.087*((O_s+O_0+(2*10**7))**-0.2)))

min_value = [Power(O_s, O_0) for O_s in Os_min]
hour_value = [Power(O_s, O_0) for O_s in Os_hour]
day_value = [Power(O_s, O_0) for O_s in Os_day]



'Input of information along with certain boundaries for plot using matplotlib.'

plt.plot(xrange, min_value, label='Minutes')
plt.plot(xrange, hour_value, label='Hours')
plt.plot(xrange, day_value, label='Days')

plt.xlim(0,70)
plt.xlabel('Time after shutdown, 0s')
plt.ylim(0.0001, 0.1)
plt.ylabel('Fraction of operating reactor power, Ps/Po')
plt.yticks([0.0001,0.001,0.01,0.1])
plt.yscale('log')

plt.legend()
plt.grid()
plt.show()