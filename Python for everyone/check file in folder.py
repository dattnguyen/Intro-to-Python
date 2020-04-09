# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:04:13 2019

@author: Dat Nguyen
"""

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))