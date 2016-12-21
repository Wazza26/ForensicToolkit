#!/usr/bin/python

import subprocess
import argparse


#Introduction to the program. First function to run. Used to gather the users' options
def intro():
    print ("Forensic Toolkit")
    print ("v1.0 - 2016")

    scanOption = input("Please choose from the following options: ")

    print ("Option X selected")

#Function to generate snapshots throughout the analysis. 
#Snapshot 1: Taken after the malware has been placed onto the virtual machine but not executed
#Snapshot 2: Taken once the malware has been executed
#Snapshot 3: Taken after the malware has run (ie after a period of 'X' minutes)
def generatingSnapshots():
    print ("Generating snapshots....")


def vmwareCLIargparse():
    parser = argparse.ArgumentParser(description="VMWare CLI")
    parser.add_argument("-s", "start", required=True, help="Starts the Virtual Machine") 
    my_args = parser.parse_args()
    return argparse.prompttolaunchVM(my_args)

#Launching the virtual machine via VMWare CLI
def executingVM():
    print ("Launching Virtual Machine....")
       
    
    #vmrun start "C:\Users\jwasley\Documents\Virtual Machines\Windows 10 x64\Windows 10 x64.vmx"

intro()
#executingVM()