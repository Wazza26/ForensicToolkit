#!/usr/bin/python

import subprocess
import argparse
import os

#Introduction to the program. First function to run. Used to gather the users' options
def launchScreen():
    print ("Forensic Toolkit")

def generatingSnapshots():
    print ("Generating snapshots....")


def vmwareCLIargparse():
    parser = argparse.ArgumentParser(description="VMWare CLI required arguements")
    parser.add_argument("filepath", help="Enter file path of .VMX")
    args = parser.parse_args()
    return args.filepath

#Pushes directory on CMD to point where vmrun executable is
def pushd():
    previous_dir = os.getcwd()
    vmPath = "C:\Program Files (x86)\\VMware\\VMware Workstation\\"
    os.chdir(vmPath)

#Launching the virtual machine via VMWare CLI
def executingVM(filepath):
    pushd()
    print ("Launching Virtual Machine....")
    print (filepath)
    subprocess.call("vmrun start", shell="True", args=["\"" + filepath + "\""])
    
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
