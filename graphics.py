from __future__ import annotations

from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(
            self, 
            x: int | float,
            y: int | float,
        ) -> Point:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Point, p2: Point) -> Line:
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"(({self.p1.x},{self.p1.y})-({self.p2.x},{self.p2.y}))"
    
    def __repr__(self) -> str:
        return f"Line(Point{self.p1}, Point{self.p2})"
    
    def draw(self, canvas: Canvas, fill_color="black") -> None:
        """
        Takes a Canvas object and optional fill color,
        draw this line on the canvas from
        """
        canvas.create_line(
            self.p1.x, self.p1.y, 
            self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack()


class Window:
    def __init__(self, width, height) -> Window:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=0)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line: Line, fill_color="black") -> None:
        """
        Takes a Line object and optional fill_color and draw the line to the
        Window's canvas
        """
        line.draw(self.__canvas, fill_color=fill_color)
    
    def wait_for_close(self) -> None:
        """
        Initializes self.__running to True, continue to redraw the window
        until the window is closed
        """
        self.__running = True
        while self.__running:
            self.redraw()
        print("User exited...")
    
    def close(self) -> None:
        """
        Used as a callback function to self.__root.protocol to set
        self.__running = False to stop application from redrawing
        """
        self.__running = False


class Cell:
    def __init__(
            self, 
            x1: int, 
            y1: int, 
            x2: int, 
            y2: int, 
            win: Window=None
        ) -> Cell:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # make x1/y1 top left and x2/y2 bottom right corner from provided coords
        self._x1 = min(x1, x2)
        self._y1 = min(y1, y2)
        self._x2 = max(x1, x2)
        self._y2 = max(y1, y2)
        self._win = win

    def __repr__(self) -> str:
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"
    
    def __str__(self) -> str:
        return f"(({self._x1},{self._y1})[]({self._x2},{self._y2}))"
    
    def draw(self) -> None:
        """
        Draws each cell wall as black if the wall exists, or white 
        (background color) if the wall does not exist
        """
        if self.has_left_wall:
            self._win.draw_line(self.left_wall)
        else:
            self._win.draw_line(self.left_wall, 'white')
        if self.has_right_wall:
            self._win.draw_line(self.right_wall)
        else:
            self._win.draw_line(self.right_wall, 'white')
        if self.has_top_wall:
            self._win.draw_line(self.top_wall)
        else:
            self._win.draw_line(self.top_wall, 'white')
        if self.has_bottom_wall:
            self._win.draw_line(self.bottom_wall)
        else:
            self._win.draw_line(self.bottom_wall, 'white')
    
    @property
    def width(self) -> int | float:
        """width of the cell"""
        return self._x2 - self._x1
    
    @property
    def height(self) -> int | float:
        """height of the cell"""
        return self._y2 - self._y1
    
    @property
    def center(self) -> Point:
        """"center point of the cell"""
        return Point(
            self._x1 + (self.width / 2), 
            self._y1 + (self.height / 2)
        )
    
    @property
    def top(self) -> int | float:

        return self._y1
    
    @property
    def bottom(self) -> int | float:
        return self._y2
    
    @property
    def left(self) -> int | float:
        return self._x1
    
    @property
    def right(self) -> int | float:
        return self._x2
    
    @property
    def top_left(self) -> Point:
        """Point at the top left corner"""
        return Point(self._x1, self._y1)
    
    @property
    def top_right(self) -> Point:
        """Point at the top right corner"""
        return Point(self._x2, self._y1)
    
    @property
    def bottom_left(self) -> Point:
        """Point at the bottom left corner"""
        return Point(self._x1, self._y2)
    
    @property
    def bottom_right(self) -> Point:
        """Point at the bottom right corner"""
        return Point(self._x2, self._y2)
    
    @property
    def top_wall(self) -> Line:
        """Line on the top of the cell"""
        return Line(self.top_left, self.top_right)
    
    @property
    def bottom_wall(self) -> Line:
        """Line on the bottom of the cell"""
        return Line(self.bottom_left, self.bottom_right)
    
    @property
    def left_wall(self) -> Line:
        """Line on the left side of the cell"""
        return Line(self.top_left, self.bottom_left)
    
    @property
    def right_wall(self) -> Line:
        """Line on the right side of cell"""
        return Line(self.top_right, self.bottom_right)
    
    def draw_move(self, to_cell: Cell, undo=False):
        """
        Draws a Line from the center of the current cell, to the center of
        to_cell. Default line color to red if undo is False, line color is
        gray if undo-ing move
        """
        if not undo:
            fill = "red"
        else:
            fill = "gray"
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, fill_color=fill)
