from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=0)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("User exited...")

    def close(self):
        self.__running = False




class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"



class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack()




class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            Line(
                Point(self._x1, self._y1), Point(self._x1, self._y2)
            ).draw(self._win.canvas)

        if self.has_right_wall:
            Line(
                Point(self._x2, self._y1), Point(self._x2, self._y2)
            ).draw(self._win.canvas)

        if self.has_top_wall:
            Line(
                Point(self._x1, self._y1), Point(self._x2, self._y1)
            ).draw(self._win.canvas)

        if self.has_bottom_wall:
            Line(
                Point(self._x1, self._y2), Point(self._x2, self._y2)
            ).draw(self._win.canvas)