# -*- coding: utf-8 -*-
"""rmse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YaCBgMI91EVbNBXYddztaRf0ZAML6k98
"""

import numpy as np

def rmse(y_t, y_h):
  mse = np.power(y_t - y_h, 2).mean()
  return np.sqrt(mse)

y_t_1 = np.array([10, 13, 22, 52])
y_t_2 = np.array([10, 10, 20, 30])
y_h = np.array([10, 10, 20, 30])

print(f'Case 1: {rmse(y_t_1, y_h)}')
print(f'Case 2: {rmse(y_t_2, y_h)}')

from sklearn.metrics import mean_squared_error as lib_mse

print(f'Case 1: {rmse(y_t_1, y_h)}')
print(f'Case 2: {rmse(y_t_2, y_h)}')

print(f'Case 1: {np.sqrt(lib_mse(y_t_1, y_h))}')
print(f'Case 2: {np.sqrt(lib_mse(y_t_2, y_h))}')

