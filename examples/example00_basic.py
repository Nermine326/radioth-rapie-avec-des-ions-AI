
"""
Simple example of how to do arithmetic on Cube objects in PyTRiP.
"""
import pytrip as pt

# sum two dose cubes, write result:
print("Two half boxes: out.dos")
d1 = pt.DosCube()
d2 = pt.DosCube()
d1.read("box052000.dos")
d2.read("box053000.dos")
d = (d1 + d2)
d.write("out.dos")

# print minium and maximum value found in cubes
print(d1.cube.min(), d1.cube.max())
print(d2.cube.min(), d2.cube.max())

# calculate new dose average LET cube
l1 = pt.LETCube()
l2 = pt.LETCube()
l1.read("box052000.dosemlet.dos")
l2.read("box053000.dosemlet.dos")

let = ((d1 * l1) + (d2 * l2)) / (d1 + d2)
let.write("out.dosemlet.dos")
