#!/usr/bin/env python3

import os.path

filename =  input("Enter a file name\n")

if os.path.exists(filename):
    print(filename)
else:
    print("file not exixts")
    

