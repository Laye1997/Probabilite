# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:25:25 2020

@author: Fatou Badji
"""


import numpy as np
import matplotlib.pyplot as plt
def repartuni(x):
#fonction de répartition pour a=-1 et b=2
   if x<-1:
       return(0)
   elif (-1<=x and x<=2):
       return((x+1)/3)
   else:
       return(1)
1
abs=np.linspace(-5,5,200)
y=[repartuni(x) for x in abs]
plt.grid()
plt.plot(abs,y)
plt.show()