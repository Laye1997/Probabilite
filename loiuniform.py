# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:27:07 2020

@author: Fatou Badji
"""


from random import random
def uniforme(a,b):
    return(a+(b-a)*random())

import numpy as np
import matplotlib.pyplot as plt
def densuni(x):
#densité pour a=-1 et b=2
   if (-1<=x and x<=2):
       return(1/3)
   else:
       return(0)
abs=np.linspace(-5,5,200)
y=[densuni(x) for x in abs] #à cause des inégalités dans densuni on construit les ordonnées à la main
plt.grid()
plt.plot(abs,y)
plt.show()

