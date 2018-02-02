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
    print("Check OSA state: check")
    print("Stop OSA: stop")
    print("Reinitialise all: reset")
    print("")
    print("Single wavelength measurement: single")
    print("Sweeping wavelength measurement: sweep")
    print("Save OSA data to file: save")
    print("")
    print("exit: q")
    
    choice = input("> ")

    if choice == 'check' : 
        Functions.OSAStat(OSA)
        print("0 = Ready")
        print("1 = Auto Sweeping")
        print("2 = Single Sweeping")
        continue
    elif choice == 'reset':  #Works!!!!!
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
    elif choice == 'single':
        print("Set laser wavelength output (default:0, range 1520-1620nm) :")
        Wavelength = input("> ")
        if Wavelength == '0':
            Wavelength = Variables.TLS.get('Wavelength')
        print("Set laser power (default:0, 0-6.309mW)")
        Power = input("> ")
        if Power == '0':
            Wavelength = Variables.TLS.get('Wavelength')
        Functions.single(TLS,OSA,Wavelength,Power)
    elif choice == 'sweep':
        print("Laser power (range 0-6.309mW:")
        Power = input("> ")
        #Must input a if statement here for default settings
        print("Sweep start wavelength (range 1520-1620nm): ")
        Swp_start = input("> ")
        print("Sweep end wavelength (range 1520-1620nm):")
        Swp_end = input("> ")
        print("Number of samples (datapoints):")
        Samples = input("> ")
        print("Number of repeats (these are averaged):")
        Ave_rpts = input("> ")
        swp_init(TLS,OSA,Power,Swp_Start,Swp_End,Samples,Ave_rpts)
        input("Press enter to start")
        swp_start(TLS,OSA)
        continue


    elif choice == 'q':
        break
    
