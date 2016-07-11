from turtle import Turtle
t=Turtle()
def init_drawman():
    global t, x_current, y_current
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)

def test_drawman():
    """Тестирование работы чертежника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(1, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    global t, x_current, y_current
    x_current += dx
    y_current += dy
    t.goto(x_current, y_current)

def to_point(x, y):
    global t, x_current, y_current
    x_current = x
    y_current = y
    t.goto(x_current, y_current)

init_drawman()
if __name__ == ' _main_ ':
    import time
    test_drawman()
    time.sleep(10)