from Drawman import *
from time import sleep

def f(x):
    return x*x

drawman_scale = 20
x = -5.
to_point(x, f(x))
pen_down()
while x < 5:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(20)
