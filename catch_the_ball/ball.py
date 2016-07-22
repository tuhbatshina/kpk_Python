import tkinter
from random import choice, randint
ball_initial_number=100
ball_minim_radius=15
ball_maxim_radius=30
ball_available_colors=['green', 'blue', 'red','yellow', '#FF00FF','lightgray']

def click_ball(event):
    """Обработчик событий мышки для игрового холста
    :param event: событие  с координатами клика
    По клику мышкой нужно удалять объект, на который мышка указывает
    А также засчитывать в очки пользователя
    """
    obj=canvas.find_closest(event.x, event.y)
    #print(canvas.coords(obj)) Вывод координат описанного вокруг круга  прямоугольника
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <=x2 and y1 <=event.y <= y2:
        canvas.delete(obj)
        create_random_ball()
        # FIXME: нужно учесть объект в очках

def move_all_balls(event):
    """
    передвигает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    Создает шарик в случайном месте
    при этом шарик не выходит за границы холста
    """
    R= randint(ball_minim_radius, ball_maxim_radius)
    x= randint(0, int(canvas['width'])-1-2*R)
    y= randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R,width=1, fill=random_color())

def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
    создает необходимое количество мячиков
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root = tkinter.Tk()

    canvas=tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>",click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите играть еще")