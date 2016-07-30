from tkinter import *
from random import choice, randint

class Ball:
    ball_initial_number=20
    ball_minim_radius=15
    ball_maxim_radius=40
    ball_available_colors=['green', 'blue', 'red','yellow', '#FF00FF','lightgray']

    def __init__(self):
        """
        Создает шарик в случайном месте
        при этом шарик не выходит за границы холста
        """
        self._R= randint(ball_minim_radius, ball_maxim_radius)
        self._x= randint(0, int(canvas['width'])-1-2*R)
        self._y= randint(0, int(canvas['height'])-1-2*R)
        canvas.create_oval(x, y, x+2*R, y+2*R,width=1, fill=random_color())


def init_game():
    """
    Создает необходимое количество объектов-шариков и объект Пушка
    :return:
    """


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk
    #FIXME



if __name__ == "__main__":
    init_main_window()
    init_game()
    root.mainloop()