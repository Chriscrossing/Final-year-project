#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:59:41 2018

@author: chriscrossing
"""

import Gpib
import Functions
import Variables


print("Program Start")
print("")
print("")

TLS = Gpib.Gpib(0,Variables.TLS.get('adr')) # Tunable laser source
OSA = Gpib.Gpib(0,Variables.OSA.get('adr')) # Spectrum Analyser

#input("Press Enter to initialise...")
#print("")
#print("")

#Functions.Init(TLS,OSA)

while True:
    
    input("Press Enter when ready")
    print("")
    print("")
    print("")
    
    print("CHOOSE AN OPTION")
    print("")
    print("Check OSA state: c")
    print("Stop OSA: stop")
    print("Reinitialise all: r")
    print("")
    print("Single sweep: sgl")
    print("Save OSA data to file: save")
    print("")
    print("exit: q")
    
    choice = input("> ")

    if choice == 'c' : 
        Functions.OSAStat(OSA)
        print("0 = Ready")
        print("1 = Auto Sweeping")
        print("2 = Single Sweeping")
        continue
    elif choice == 'r':  #Works!!!!!
        Functions.Init(TLS,OSA)
        print("Initialising, wait for instrument confirmation")
        print("")
        continue
    elif choice == 'save':
        print("Input Filename")
        Filename = input("> ")
        Functions.save(TLS,OSA,Filename)
        continue
    elif choice == 'stop':
        print("Stopping, wait for instrument confirmation")
        Functions.stop(OSA)
        continue
    elif choice == 'sgl':
        print("Set laser wavelength output (default:0, range 1520-1620nm) :")
        Wavelength = input("> ")
        if Wavelength == '0':
            Wavelength = Variables.TLS.get('Wavelength')
        print("Set laser power (default:0, 0-6.309mW)")
        Power = input("> ")
        if Power == '0':
            Wavelength = Variables.TLS.get('Wavelength')
        Functions.single(TLS,OSA,Wavelength,Power)
    elif choice == 'q':
        break
    
