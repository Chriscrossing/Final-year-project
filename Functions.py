#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:30:24 2018

@author: chriscrossing
"""
import re
import numpy as np


def OSAStat(OSA): #Checks what state the OSA is in, currently crashes the osa when its running.
    OSA.write("SWEEP?");
    print("Value: " + str(re.sub("\D", "", OSA.read(10).decode('UTF-8'))))
    return 

def Init(TLS,OSA):
    OSA.write("INIT");
    TLS.write("INIT");
    return

def stop(OSA):
    OSA.write("STP")
    return

def single(TLS,OSA,Wavelength,Power):
    Wavelength = "TWL%f" %'{0:.3f}'.format(float(Wavelength))
    TLS.write(Wavelength)
    Power = "TPMW%f" %Power,
    TLS.write(Power) 
    TLS.write("L1") # Turns on laser
    OSA.write("AUTO") # Auto scanning
    input("Press Enter when ready")
    OSA.write("STP") #stops sweeping
    TLS.write("L0") #laser off
    return

def save(TLS,OSA,Filename):                               
    OSA.write("WDATA R1-R20001");           #Command to retrive data.
    Raw_Lam1 = OSA.read(18000);             #command to read data.
    Raw_Lam2 = Raw_Lam1.decode('UTF-8');    #data is decoded as a string.
    Raw_Lam3 = Raw_Lam2.split(',');         #converted to a list.
    Lambda = np.double(Raw_Lam3[2:-1]);        #converted to a numpy array.
    OSA.write("LDATA R1-R20001");           #same again....
    Raw_int1 = OSA.read(18000);
    Raw_int2 = Raw_int1.decode('UTF-8');
    Raw_int3 = Raw_int2.split(',');    
    Intensity = np.double(Raw_int3[2:-1]);
    Intensity = Intensity[0:np.size(Lambda)];
    np.savetxt("data/" + Filename + ".txt", (Intensity, Lambda), delimiter=',');
    print("text file saved in data folder")
    return
