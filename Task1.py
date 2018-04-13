import math
import tkinter
import sys

WIDTH = 1000
HEIGHT = 500

LEFT = -10
RIGHT = 10
Y = None
X = None


def get_points():
    global Y
    f = "(x) ** 3"
    x = LEFT
    dx = (RIGHT - LEFT) / WIDTH
    xlist = []
    ylist = []
    for i in range(WIDTH):
        y = eval(f.replace("x", str(x)))
        xlist.append(x)
        ylist.append(y)
        x = x + dx
        if abs(x) < dx:
            Y = i
    return xlist, ylist


def scale(ypoints, top, bottom):
    global X
    pmax = -1 * sys.maxsize
    pmin = sys.maxsize
    for p in ypoints:
        if p > pmax:
            pmax = p
        if p < pmin:
            pmin = p
    offset = bottom - pmin
    sprain = abs((top - bottom) / (pmax - pmin))
    if pmax > 0 and pmin < 0:
        X = offset * sprain
    return list(map(lambda x: int((x + offset) * sprain), ypoints))


def fill(points):
    for i in range(len(points) - 1):
        prev = points[i]
        next = points[i + 1]
        current = prev[1]
        dy = 1 if prev[1] < next[1] else -1
        while current != next[1]:
            current = current + dy
            points.append((prev[0], current))


def invert(point):
    return [(x, HEIGHT - y) for x, y in points]


data = get_points()
ylist = scale(data[1], HEIGHT, 0)
points = [(i, ylist[i]) for i in range(WIDTH)]
fill(points)
points = invert(points)

root = tkinter.Tk()

canv = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
for x, y in points:
    canv.create_line(x, y, x, y, fill="black")
if Y is not None:
    canv.create_line(Y, 0, Y, HEIGHT)
if X is not None:
    canv.create_line(0, X, WIDTH, X)
canv.pack()
root.mainloop()
