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
    Wavelength = "TWL" + str(Wavelength)
    TLS.write(Wavelength)
    Power = "TPMW" + str(Power)
    TLS.write(Power) 
    TLS.write("L1") # Turns on laser
    OSA.write("AUTO") # Auto scanning
    input("Press Enter when finished")
    OSA.write("STP") #stops sweeping
    TLS.write("L0") #laser off
    return

def swp_init(TLS,OSA,Power,Swp_Start,Swp_End,Samples,Ave_rpts):
    TLS.write(Power); 
    TLS.write("TSTPWL" + str(Swp_End));
    TLS.write("TSTAWL" + str(Swp_Start));
    #TLS.write(Swp_Step);
    #TLS.write(Swp_Time);
    #TLS.write(Stp_Time);
    #OSA.write(Resolution);
    OSA.write("TLSADR" + str(Variables.TLS.get('adr')));
    OSA.write("TLSSYNC1");
    OSA.write("ATREF1");
    OSA.write("STAW" + str(Swp_Start));
    OSA.write("STPWL" + str(Swp_End));
    OSA.write(Ave_rpts);
    OSA.write(Samples);
    OSA.write("SHI2");
    return 

def swp_start(TLS,OSA):
    TLS.write("L1");
    OSA.write("SGL");
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
