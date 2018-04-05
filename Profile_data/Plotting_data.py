#!/usr/bin/env python3
# -*- coding: utf-8 -*-"""

"""
Created on Thu Feb  1 10:30:24 2018

author: chriscrossing
""" 
import numpy as np
import Functions
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#Filename = "1cm taper (taper1 profile).txt"
Filename = "1cm taper (taper2 profile).txt"

LocT = np.loadtxt(Filename,usecols=(0),skiprows=(1))
DiamT = np.loadtxt(Filename,usecols=(1),skiprows=(1))
LocS = np.loadtxt(Filename,usecols=(2),skiprows=(1))
DiamS = np.loadtxt(Filename,usecols=(3),skiprows=(1))

#Plotting the graph
f, ax = plt.subplots(1,figsize=(17,6))

#Figure Formatting
plt.xlabel('Wavelength / nm', fontsize=30);
plt.ylabel('Losses / dBm', fontsize=30);
#plt.ylim([0,np.max(y_err)+np.max(Losses)])
#plt.xlim([float(Swp_Start),float(Swp_End)])
plt.title('Cake', fontsize=20);
#plt.tight_layout()

#Plot the Losses of the fiber device
#ax.scatter(Lambda, Losses,marker='x')

#Now a linear fit.
#ax.plot(Lambda, np.polyval(p,Lambda),color='green',linewidth=2)

#And now the two upper and lower errors.
ax.plot(LocT,DiamT,':',color='red',linewidth=3)
ax.plot(LocS,DiamS,':',color='red',linewidth=3)

#Below is for the Key.
#Red_Patch = mpatches.Patch(color='red', label='Error')
#Blue_Patch = mpatches.Patch( label='Data Points')
#Green_Patch = mpatches.Patch(color='green', label='Linear fit')
#plt.legend(handles=[Blue_Patch,Green_Patch,Red_Patch],fontsize=20)

plt.show()