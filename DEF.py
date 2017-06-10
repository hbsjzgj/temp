import math
def move(x, y, step, angel=0):
    nx = x + step * math.cos(angel)
    ny = y - step * math.sin(angel)
    return nx, ny

def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2