#!/usr/bin/python

import subprocess
import argparse
import os
from pathlib import Path

#Introduction to the program. First function to run. Used to gather the users' options
def launchScreen():
    print ("Forensic Toolkit")

def generatingSnapshots():
    print ("Generating snapshots....")


def vmwareCLIargparse():
    parser = argparse.ArgumentParser(description="VMWare CLI required arguements")
    parser.add_argument("filepath", help="Enter file path of .VMX")
    args = parser.parse_args()
    
    return Path(args.filepath)

#Pushes directory on CMD to point where vmrun executable is
def cd():
    vmPath = "C:\Program Files (x86)\\VMware\\VMware Workstation\\"
    os.chdir(vmPath)

#Launching the virtual machine via VMWare CLI
def executingVM(filepath):
    cd()
    print ("Launching Virtual Machine....")
    print (filepath)
    subprocess.call(["vmrun", "start", "\"" + filepath + "\""], shell="True")
    
#def generatingSnapshot():
#   print ("Launching Virtual Machine....")
#  subprocess.call("vmrun snapshot", shell="True")
#def stoppingVM():
#   print ("Launching Virtual Machine....")
#   subprocess.call("vmrun stop", shell="True")

launchScreen()
filepath = vmwareCLIargparse()
executingVM(filepath)

#executingVM()
