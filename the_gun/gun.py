from tkinter import *
from random import choice, randint

screen_width = 400
screen_height = 300
timer_delay = 100

class Ball:
    initial_number=20
    minim_radius=15
    maxim_radius=40
    available_colors=['green', 'blue', 'red','yellow', '#FF00FF','lightgray']

    def __init__(self):
        """
        Создает шарик в случайном месте
        при этом шарик не выходит за границы холста
        """
        R= randint(Ball.minim_radius, Ball.maxim_radius)
        x= randint(0, screen_width-1-2*R)
        y= randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fillcolor, outline =fillcolor)

        self._Vx = randint(-2, +2)
        self._Vy = randint(-2, +2)


    def fly(self):
        self._x +=self._Vx
        self._y += self._Vy
        #отскок от стены
        if self._x <0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R>= screen_width:
            self._x = screen_width - 2*self._R-1
            self._Vx = -self._Vx
        if self._y <0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y  + 2*self._R >= screen_height - 1:
            self._y = screen_height - 2*self._R- 1
            self._Vy = -self._Vy
        canvas.coords(self._avatar, self._x, self._y, self._x  + 2*self._R, self._y  + 2*self._R )

class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height - 1
        self._lx = 30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x + self._lx,
                                          self._y + self._ly)

    def shoot(self):
        """
        :return  возвращает объект снаряд
        """
        shell = Ball()
        shell._x = self._x + self._lx
        shell._y = self._y + self._ly
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        shell._R = 5
        shell.fly()
        return shell

def init_game():
    """
    Создает необходимое количество объектов-шариков и объект Пушка
    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []

def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root, width = screen_width, height = screen_height )
    scores_text = Entry(root, textvariable = scores_value)
    canvas.grid(row = 1, column = 0, columnspan = 3)
    scores_text.grid(row = 0, column = 2)
    canvas.bind('<Button-1>', click_event_handler)

def timer_event():
    #здесь делаются все периодические расчеты
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()
    canvas.after(timer_delay, timer_event)


def click_event_handler(event):
    global  shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()