#!insert the current directory path to python path
import sys
import os

cwd = os.getcwd() #get current working directory

sys.path.append(cwd)
#print(sys.path)

#test the module: generate_list
from generate_list import printIt

for x in range(0,999):
    #running until error occurs
    printIt()
