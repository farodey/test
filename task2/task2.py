import sys
from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def areaTriangle(a, b, c):
    p = (a + b + c) / 2
    return sqrt((p * (p - a) * (p - b) * (p - c)))


def inApex(quad, x, y):
    for i in quad:
        if i[0] == x and i[1] == y:
            return True
    return False


def inSide(quad, x, y):
    if distance(x, y, quad[0][0], quad[0][1]) + distance(x, y, quad[1][0], quad[1][1]) == distance(quad[0][0], quad[0][1], quad[1][0], quad[1][1]):
        return True
    if distance(x, y, quad[1][0], quad[1][1]) + distance(x, y, quad[2][0], quad[2][1]) == distance(quad[1][0], quad[1][1], quad[2][0], quad[2][1]):
        return True
    if distance(x, y, quad[2][0], quad[2][1]) + distance(x, y, quad[3][0], quad[3][1]) == distance(quad[2][0], quad[2][1], quad[3][0], quad[3][1]):
        return True
    if distance(x, y, quad[3][0], quad[3][1]) + distance(x, y, quad[0][0], quad[0][1]) == distance(quad[3][0], quad[3][1], quad[0][0], quad[0][1]):
        return True
    return False


def inQuad(quad, x, y):
    s1 = areaTriangle(distance(x, y, quad[0][0], quad[0][1]),
                      distance(quad[0][0], quad[0][1], quad[1][0], quad[1][1]),
                      distance(quad[1][0], quad[1][1], x, y))
    s2 = areaTriangle(distance(x, y, quad[1][0], quad[1][1]),
                      distance(quad[1][0], quad[1][1], quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], x, y))
    s3 = areaTriangle(distance(x, y, quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], quad[0][0], quad[0][1]),
                      distance(quad[0][0], quad[0][1], x, y))

    s4 = areaTriangle(distance(x, y, quad[0][0], quad[0][1]),
                      distance(quad[0][0], quad[0][1], quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], x, y))
    s5 = areaTriangle(distance(x, y, quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], quad[3][0], quad[3][1]),
                      distance(quad[3][0], quad[3][1], x, y))
    s6 = areaTriangle(distance(x, y, quad[3][0], quad[3][1]),
                      distance(quad[3][0], quad[3][1], quad[0][0], quad[0][1]),
                      distance(quad[0][0], quad[0][1], x, y))

    t1 = areaTriangle(distance(quad[0][0], quad[0][1], quad[1][0], quad[1][1]),
                      distance(quad[1][0], quad[1][1], quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], quad[0][0], quad[0][1]))
    t2 = areaTriangle(distance(quad[0][0], quad[0][1], quad[2][0], quad[2][1]),
                      distance(quad[2][0], quad[2][1], quad[3][0], quad[3][1]),
                      distance(quad[3][0], quad[3][1], quad[0][0], quad[0][1]))

    sumAreaTriangle1 = s1 + s2 + s3
    sumAreaTriangle2 = s4 + s5 + s6


    if round(sumAreaTriangle1, 4) == round(t1, 4):
        return True
    if round(sumAreaTriangle2, 4) == round(t2, 4):
        return True
    return False


quad = []
point_list = []

with open(sys.argv[1]) as file:
    for line in file:
        x, y = line.split()
        quad.append([float(x), float(y)])
with open(sys.argv[2]) as file:
    for line in file:
        x, y = line.split()
        point_list.append([float(x), float(y)])


for point in point_list:
    if inApex(quad, point[0], point[1]):
        print(0)
    elif inSide(quad, point[0], point[1]):
        print(1)
    elif inQuad(quad, point[0], point[1]):
        print(2)
    else:
        print(3)

