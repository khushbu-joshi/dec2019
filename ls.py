#!/usr/bin/python3
import os

x=input("enter the name of the directory : ")
dirlist=os.listdir(x)

#for structured pattern of list
from pprint import  pprint
pprint(dirlist)


'''
#for unstructured pattern of data
print(dirlist)
'''
