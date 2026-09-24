# -*- coding: utf-8 -*-
from math import radians, sqrt, cos

print("This programm finds the 3rd side of a triangle")
c = 0  # we're looking for

print('Enter the 1st side')
a = float(input())  # 1st side
print('Enter the 2nd side')
b = float(input())  # 2nd side
print('Enter the angle in degrees')
adegr = float(input())  # angle
arad = radians(adegr)  # degr into rad
if a > 0:
    if b > 0:
        c = ((a**2) + (b**2)) - 2 * a * b * cos(arad)
        c = sqrt(c)
        print('The 3rd side is ', c)
    else:
      print("Such triangle does not exist. Please, try again by entering values that are above 0")
else:
    print("Such triangle does not exist. Please, try again by entering values that are above 0")
