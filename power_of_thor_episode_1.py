# https://www.codingame.com/training/easy/power-of-thor-episode-1


import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    direction = ""

    if light_y > initial_ty:
        direction += "S"
        initial_ty += 1
    elif light_y < initial_ty:
        direction += "N"
        initial_ty -= 1

    if light_x > initial_tx:
        direction += "E"
        initial_tx += 1
    elif light_x < initial_tx:
        direction += "W"
        initial_tx -= 1

    print(direction)
