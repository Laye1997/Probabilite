# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 21:11:25 2020

@author: Abdul Lahi Jaaw
"""

import  numpy  as  np 
import matplotlib.pyplot as plt
s = np.random.poisson(5, 10000)
count ,  bins ,  ignored  =  plt . hist ( s ,  14 ,  density = True, label = "loi de Poisson" ) 
plt.legend()
plt.grid()
plt.show ()