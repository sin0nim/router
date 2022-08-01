import turtle


class Level0:
    counter = 0

    def __init__(self, num_lines, num_columns, size):
        self.pen_list = []
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.step = size

        screen_size = ((self.num_columns + 2) * self.step * 6, (self.num_lines + 4) * self.step)
        turtle.Screen().colormode(255)
        turtle.Screen().setup(screen_size[0], screen_size[1])
        self.headx, self.heady = -(screen_size[0] - 8 * self.step) / 2, (screen_size[1] - self.step) / 2

        for i in range(self.num_lines):
            item = turtle.Turtle()
            item.hideturtle()
            item.speed(0)
            item.pensize(2)
            item.color(127, 127, 127)
            self.pen_list.append((item, 0))

    @classmethod
    def move_pens(cls, pen_list, dist, angle):
        for pen_item in pen_list:
            pen_item[0].forward(dist)
            pen_item[0].right(angle)

    @classmethod
    def shift_pens(cls, pen_list, x, y, dy):
        xx, yy = x, y
        for item in pen_list:
            item[0].pu()
            item[0].goto(xx, yy)
            item[0].pd()
            yy = yy - dy

    @classmethod
    def draw_column(cls, pen_list, step):
        for _ in range(2):
            Level0.move_pens(pen_list, 2 * step, 90)
            Level0.move_pens(pen_list, step / 6, -90)
            Level0.move_pens(pen_list, step, 180)
            Level0.move_pens(pen_list, step, -90)
            Level0.move_pens(pen_list, step / 3, -90)
            Level0.move_pens(pen_list, step, 180)
            Level0.move_pens(pen_list, step, -90)
            Level0.move_pens(pen_list, step / 3, -90)
            Level0.move_pens(pen_list, step, 180)
            Level0.move_pens(pen_list, step, -90)
            Level0.move_pens(pen_list, step / 6, 90)
            for _ in range(4):
                Level0.move_pens(pen_list, step, 90)

    def draw_crystal(self):
        Level0.shift_pens(self.pen_list, self.headx, self.heady, self.step)

        for column in range(self.num_columns):
            Level0.draw_column(self.pen_list, self.step)
            self.headx += 6 * self.step
            Level0.shift_pens(self.pen_list, self.headx, self.heady, self.step)

        turtle.done()
