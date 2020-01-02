#!/usr/bin/python3

import os
k=input("enter the name of file : ")

def touch(k, times=None) :
    fhandle = open(k, 'a')
    try :
        os.utime(k, times)
    finally :
        f.handle.close()



