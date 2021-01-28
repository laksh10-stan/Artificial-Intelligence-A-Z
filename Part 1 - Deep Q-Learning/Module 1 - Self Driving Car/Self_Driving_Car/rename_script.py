# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:57:56 2020

@author: laksh
"""

import os
for filename in os.listdir('F:\Icons\starwars'):
    os.rename(os.path.join('F:\Icons\starwars', filename),
              os.path.join('F:\Icons\starwars', filename.replace('peace','Wars')))
    

    