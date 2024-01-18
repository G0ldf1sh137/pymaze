from __future__ import annotations

from tkinter import Tk, BOTH, Canvas


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

    def __str__(self):
        return f"(({self.p1.x},{self.p1.y})-({self.p2.x},{self.p2.y}))"
    
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, 
            self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack()


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=0)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color=fill_color)
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("User exited...")
    
    def close(self):
        self.__running = False


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
            self._win.draw_line(self.left_wall)
        if self.has_right_wall:
            self._win.draw_line(self.right_wall)
        if self.has_top_wall:
            self._win.draw_line(self.top_wall)
        if self.has_bottom_wall:
            self._win.draw_line(self.bottom_wall)
    
    @property
    def width(self) -> int:
        return self._x2 - self._x1
    
    @property
    def height(self) -> int:
        return self._y2 - self._y1
    
    @property
    def center(self) -> Point:
        return Point(
            self._x1 + (self.width / 2), 
            self._y1 + (self.height / 2)
        )
    
    @property
    def top(self) -> int:
        return self._y1
    
    @property
    def bottom(self) -> int:
        return self._y2
    
    @property
    def left(self) -> int:
        return self._x1
    
    @property
    def right(self) -> int:
        return self._x2
    
    @property
    def top_left(self) -> Point:
        return Point(self._x1, self._y1)
    
    @property
    def top_right(self) -> Point:
        return Point(self._x2, self._y1)
    
    @property
    def bottom_left(self) -> Point:
        return Point(self._x1, self._y2)
    
    @property
    def bottom_right(self) -> Point:
        return Point(self._x2, self._y2)
    
    @property
    def top_wall(self) -> Line:
        return Line(self.top_left, self.top_right)
    
    @property
    def bottom_wall(self) -> Line:
        return Line(self.bottom_left, self.bottom_right)
    
    @property
    def left_wall(self) -> Line:
        return Line(self.top_left, self.bottom_left)
    
    @property
    def right_wall(self) -> Line:
        return Line(self.top_right, self.bottom_right)
    
    def draw_move(self, to_cell: Cell, undo=False):
        if not undo:
            fill = "red"
        else:
            fill = "gray"
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, fill_color=fill)
