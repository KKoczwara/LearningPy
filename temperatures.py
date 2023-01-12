# https://www.codingame.com/training/easy/temperatures

import sys
import math

n = int(input())  # the number of temperatures to analyse
MAX_TEMPERATURE = 5526
closest_temp = MAX_TEMPERATURE

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if abs(0 - t) < abs(closest_temp):
        closest_temp = t
    elif t == - closest_temp:
        closest_temp = abs(t)

if n == 0:
    print(0)
else:
    print(closest_temp)