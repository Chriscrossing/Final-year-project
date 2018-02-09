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

#TLS = Gpib.Gpib(0,Variables.TLS.get('adr')) # Tunable laser source
#OSA = Gpib.Gpib(0,Variables.OSA.get('adr')) # Spectrum Analyser

#input("Press Enter to initialise...")
#print("")
#print("")

#Functions.Init(TLS,OSA)

while True:

    TLS_default = Functions.load_obj('TLS')
    OSA_default = Functions.load_obj('OSA')
    Common_default = Functions.load_obj('Common')
    
    print(Common_default)

    print("")
    print("")
    print("")
    input("Press Enter when instruments are ready")
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
    print("View/edit sweep defaults: edit")
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
        print("Set laser wavelength output (range 1520-1620nm) :")
        print("(Leave blank for default)")
        Wavelength = input("> ")
        if Wavelength == '':
            Wavelength = TLS_default.get('Wavelength')
        print("Set laser power (0-6.309mW)")
        print("(Leave blank for default)")
        Power = input("> ")
        if Power == '':
            Wavelength = TLS_default.get('Power')
        Functions.single(TLS,OSA,Wavelength,Power)
        print("Save settings as default?")
        print("(y/n)")
        default = input("> ")
        if default == "y":
            newTLS = {
                'Wavelength': Wavelength,
                'Power': Power
                }
            newOSA = {}
            newcommon = {}
            Functions.savedefault(TLS_default,OSA_default,Common_default,newcommon,newTLS,newOSA)
        continue
    
    
    elif choice == 'sweep':
        print("")
        print("")
        print("Input settings for a wavelength sweep")
        print("Leave blank for default settings")
        print("")
        print("")
        print("Laser power (range 0-6.309mW:")
        Power = input("> ")
        if Power == '':
            Power = TLS_default.get('Power')
        print("Sweep start wavelength (range 1520-1620nm): ")
        Swp_Start = input("> ")
        if Swp_Start == '':
            Swp_Start = Common_default.get('Swp_Start')
        print("Sweep end wavelength (range 1520-1620nm):")
        Swp_End = input("> ")
        if Swp_End == '':
            Swp_End = Common_default.get('Swp_End')
        print("Number of samples (datapoints):")
        Samples = input("> ")
        if Samples == '':
            Samples = OSA_default.get('Samples')
        print("Number of repeats per sample (these are averaged):")
        Ave_rpts = input("> ")
        if Ave_rpts == '':
            Ave_rpts = OSA_default.get('Ave_rpts')
        print("Wavelength step width:")
        Swp_Step = input("> ")
        if Swp_Step == '':
            Swp_Step = TLS_default.get('Swp_Step')
        print("Time for Sweep:")
        Swp_Time = input('> ')
        if Swp_Time == '':
            Swp_Time = TLS_default.get('Swp_Time')
        print("Time for each step:")
        Stp_Time = input('> ')
        if Stp_Time == '':
            Stp_Time = TLS_default.get('Stp_Time')
        print("OSA Resolution:")
        Resolution = input('> ')
        if Resolution == '':
            Resolution = OSA_default.get('Resoloution')
        #Functions.swp_init(TLS,OSA,Variables,Power,Swp_Start,Swp_End,Samples,Ave_rpts)
        
        print("Save settings as default?")
        print("(y/n)")
        default = input("> ")
        if default == "y":
            newTLS = {
                'Power': Power,
                'Samples': Samples,
                'Swp_Step': Swp_Step,
                'Swp_Time': Swp_Time,
                'Stp_Time': Stp_Time
                }
            newOSA = {
                'Ave_rpts': Ave_rpts,
                'Resolution': Resolution
                }
            newcommon = {
                'Swp_start': Swp_Start,
                'Swp_End': Swp_End
                }
            Functions.savedefault(TLS_default,OSA_default,Common_default,newcommon,newTLS,newOSA)
        

        input("Press enter to start sweep")
        #Functions.swp_start(TLS,OSA)

        continue


    elif choice == 'q':

        break
    
