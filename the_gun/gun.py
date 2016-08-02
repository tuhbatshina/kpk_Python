from tkinter import *
from random import choice, randint

screen_width = 400
screen_height = 300
timer_delay = 50
gravitational_acceleration = 0
dt = 2
class MovingUnit:
    """
    Абстрактный класс-предок для шариков-мишеней и снарядов
    Имеет атрибуты x, y, Vx, Vy, R, avatar
    а также метод fly - абстрактный, т.е. его нельзя
    реально вызывать
    """
    def __init__(self, x, y, Vx, Vy, R, avatar):
        self._R = R
        self._x = x
        self._y = y
        self._Vx = Vx
        self._Vy = Vy
        self.avatar = avatar
        self._deleted = False
    def fly(self):
        """Абстрактный метод. Нельзя вызывать.
        Требуется реализовывать в классах-потомках
        """
        raise RuntimeError()
    def delete(self):
        """
        Удаляет объект с холста и
        помечает его как удаленный
        """
        if not self._deleted:
            canvas.delete(self.avatar)
            self._deleted = True

    def deleted(self):
        """
        :return: True, если объект уже удален
        """
        return self._deleted



class Shell(MovingUnit):
    """
    Снаряд, вылетающий из пушки.
    Не отражается от стенок, уничтожается за пределами поля.
    Двигается по гравитационной траектории
    """
    radius = 5
    maximal_number = 3
    color = 'black'

    def __init__(self, x, y, Vx, Vy):
        """


        """
        R = Shell.radius
        avatar = canvas.create_oval(x, y, x+2*R, y+2*R,
                                    width=1, fill = Shell.color,
                                    outline = Shell.color)
        super().__init__(x, y, Vx, Vy, R, avatar)


    def fly(self):
        ax = 0
        ay = gravitational_acceleration
        self._x += self._Vx*dt + ax*dt**2/2
        self._y += self._Vy*dt + ay*dt**2/2
        self._Vx += ax*dt
        self._Vy += ay*dt
        canvas.coords(self.avatar, self._x, self._y,
                      self._x + 2*self._R, self._y + 2*self._R)
        #FIXME Не выполнено уничтожение снаряда за границами поля!

class Ball(MovingUnit):
    initial_number = 20
    minim_radius = 15
    maxim_radius = 40
    available_colors = ['green', 'blue', 'red','yellow', '#FF00FF','lightgray']

    def __init__(self):
        """
        Создает шарик в случайном месте
        при этом шарик не выходит за границы холста
        """
        R= randint(Ball.minim_radius, Ball.maxim_radius)
        x= randint(0, screen_width-1-2*R)
        y= randint(0, screen_height-1-2*R)
        Vx = randint(-2, +2)
        Vy = randint(-2, +2)

        fillcolor = choice(Ball.available_colors)
        avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fillcolor, outline =fillcolor)

        super().__init__(x, y, Vx, Vy, R, avatar)



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
        canvas.coords(self.avatar, self._x, self._y, self._x  + 2*self._R, self._y  + 2*self._R )

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
        :return  возвращает объект снаряд класса Shell
        """
        shell = Shell(self._x + self._lx, self._y + self._ly,
                self._lx/10, self._ly/10      )

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

def remove_deleted_units_from_list(units):
    delta = 0
    for i in range(len(units)):
        if units[i].deleted():
            delta += 1
        else:
            units[i - delta] = units[i]
    units[:] = units[: - delta]
    print(len(units))

def distance(unit1, unit2):
    """
    расстояние между поверхностями шариков
    """
    dx = unit1._x - unit2._x
    dy = unit1._y - unit2._y
    L = (dx**2 + dy**2)**0.5
    return L - unit1._R - unit2._R

def timer_event():
    #здесь делаются все периодические расчеты
    # проверять перебором столкновение снаряда и шарика.
    # При столкновении убирать снаряд и шарик из их списков
    # Запомнить эти снаряды и шарики. Потом разом удалить
    # удалить шарик - аватар из списка
    # на событие Move для canvas повесить событие gun._lx и gun_ly
    # и обновление аватара через coords
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()
    print(1)

    for shell in shells_on_fly:
        for ball in balls:
            if distance(ball, shell)<=0:
                #удалить шарик и снаряд
                shell.delete()
                ball.delete()
        remove_deleted_units_from_list(balls)
    remove_deleted_units_from_list(shells_on_fly)
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