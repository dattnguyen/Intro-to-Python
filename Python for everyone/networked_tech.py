# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:30:28 2019

@author: Dat Nguyen
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect ( ('data.pr4e.org', 80))