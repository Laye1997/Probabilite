# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:35:01 2020

@author: Fatou Badji
"""

from scipy.stats import norm
norm.rvs()
import matplotlib.pyplot as plt
import numpy as np
abs=np.linspace(-5,5,200)
plt.plot(abs,norm.cdf(abs))
plt.grid()
plt.show()