# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:36:38 2019

@author: Trevor
"""

import base64 
import sys
 
with open("E:/Programs/Python/images/t.png", "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
    #print(string)
    print(len(string))
    print(sys.getsizeof(string))