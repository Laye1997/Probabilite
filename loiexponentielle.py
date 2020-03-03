# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:24:06 2020

@author: Fatou Badji
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
abs=np.linspace(0,8,200)
plt.plot(abs,expon.pdf(abs,scale=1))
plt.plot(abs,expon.pdf(abs,scale=1/3))
plt.grid()
plt.show()

