# https://www.codingame.com/training/easy/horse-racing-duals

import sys
import math

n = int(input())
strengths_list = []

for i in range(n):
    pi = int(input())
    strengths_list.append(pi)

strengths_list.sort()

difference = strengths_list[n - 1] - strengths_list[0]

for i in range(n - 1):
    if difference > abs(strengths_list[i] - strengths_list[i + 1]):
        difference = abs(strengths_list[i] - strengths_list[i + 1])

print(difference)