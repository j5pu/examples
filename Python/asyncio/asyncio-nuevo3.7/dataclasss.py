from dataclasses import dataclass
'''
dataclasses
The new dataclass() decorator provides a way to declare data classes.
A data class describes its attributes using class variable annotations.
Its constructor and other magic methods, such as __repr__(), __eq__(), and __hash__() are generated automatically.

Example:
'''
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)
print(p)   # produces "Point(x=1.5, y=2.5, z=0.0)"