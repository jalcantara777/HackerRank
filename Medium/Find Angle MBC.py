## Find Angle MBC
import math

y=int(input())  ## AB
x=int(input()) ## BC

phi=math.atan(y/x)
phi=math.degrees(phi)
phi=str(int(round(phi,0)))
print(phi+chr(176))