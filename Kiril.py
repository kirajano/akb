# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:46:09 2021

@author: Kiril Kasjanov
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv("./train.csv")
store = pd.read_csv("./store.csv")


train.head(10)