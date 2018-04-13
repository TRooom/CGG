import math
import tkinter
import sys

WIDTH = 1000
HEIGHT = 500

LEFT = 0.1
RIGHT = 10


def get_points():
    f = "1 / (x)"
    x = LEFT
    dx = (RIGHT - LEFT) / WIDTH
    xlist = []
    ylist = []
    for _ in range(WIDTH):
        y = eval(f.replace("x", str(x)))
        xlist.append(x)
        ylist.append(y)
        x = x + dx
    return xlist, ylist


def scale(points, top, bottom):
    pmax = -1 * sys.maxsize
    pmin = sys.maxsize
    for p in points:
        if p > pmax:
            pmax = p
        if p < pmin:
            pmin = p
    offset = bottom - pmin
    sprain = abs((top - bottom) / (pmax - pmin))
    return list(map(lambda x: int((x + offset) * sprain), points))


def fill(points):
    for i in range(len(points) - 1):
        prev = points[i]
        next = points[i + 1]
        current = prev[1]
        dy = 1 if prev[1] < next[1] else -1
        while prev[1] != next[1]:
            current = current + dy
            points.append((prev[0], current))


data = get_points()
ylist = scale(data[1], HEIGHT, 0)
points = [(i, ylist[i]) for i in range(WIDTH)]
fill(points)

root = tkinter.Tk()

canv = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
for x, y in points:
    canv.create_oval(x, HEIGHT - y, x, HEIGHT - y, fill="black")

canv.pack()
root.mainloop()
