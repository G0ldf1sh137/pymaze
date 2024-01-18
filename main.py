from graphics import Window, Point, Line, Cell



def main():
    win = Window(800, 600)


    c1 = Cell(100, 100, 200, 200, win)
    c1.has_bottom_wall = False
    c2 = Cell(300, 100, 400, 200, win)
    c2.has_right_wall = False
    c2.has_left_wall = False
    c1.draw()
    c2.draw()


    win.wait_for_close()



if __name__ == "__main__":
    main()