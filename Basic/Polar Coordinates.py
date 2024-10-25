import cmath
import re
z=input()
patron = r'([+-]?\d+)\s*([+-]\s*\d+)i'
match = re.match(patron, z.replace(" ", ""))
x = int(match.group(1))
y = int(match.group(2).replace(" ", ""))
r=(x**2+y**2)**(1/2)
phi=cmath.phase(complex(x,y))
print(r)
print(phi)