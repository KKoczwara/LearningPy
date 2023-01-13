import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_range_start = 0
x_range_end = w
y_range_start = 0
y_range_end = h

def xy_range(range_start, range_end):
    return int((range_start + range_end) /2)

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if 'R' in bomb_dir:
        x_range_start = x0  
    elif 'L' in bomb_dir:
        x_range_end = x0

    if 'U' in bomb_dir:
        y_range_end = y0
    elif 'D' in bomb_dir:
        y_range_start = y0

    x0 = xy_range(x_range_start, x_range_end)
    y0 = xy_range(y_range_start, y_range_end)

    # the location of the next window Batman should jump to.
    print(x0, y0)