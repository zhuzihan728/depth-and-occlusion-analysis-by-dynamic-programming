from PIL import Image, ImageDraw
import numpy as np


def getwidth(im):
    return im.width


def getheight(im):
    return im.height


class matrix():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = np.empty((col, row))

    def get_value(self, row, col):
        return self.value[col, row]

    def add(self, value, row, col):
        self.value[col, row] = value

    def get_size(self):
        return (self.row, self.col)


def get_pixel(path):
    im = Image.open(path)
    grey_im = im.convert('L')
    mat = matrix(getwidth(im), getheight(im))
    for j in range(getheight(im)):
        for i in range(getwidth(im)):
            mat.add(grey_im.getpixel((i, j)), i, j)
    return mat


l1 = get_pixel('/Users/doudou/Desktop/algorithm/cwk2/randomDot1.png')
l2 = get_pixel('/Users/doudou/Desktop/algorithm/cwk2/randomDot2.png')

print(l1.value)


def cost_of_matching(im1, im2, i, j, col):
    z1 = im1.get_value(i, col)
    z2 = im2.get_value(j, col)
    z = (z1 + z2) / 2
    w = (z - z1) * (z - z2) / 16
    return abs(w)


def cost_matrix(im1, im2, col):
    a = im1.get_size()[0]
    mat = matrix(a + 1, a + 1)
    mat1 = matrix(a + 1, a + 1)
    for i in range(1, a + 1):
        mat.add(i * 3.8, i, 0)
    for i in range(1, a + 1):
        mat.add(i * 3.8, 0, i)
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            l = []
            a1 = mat.get_value(i - 1, j - 1) + cost_of_matching(im1, im2, i - 1, j - 1, col)
            b = mat.get_value(i, j - 1) + 3.8
            c = mat.get_value(i - 1, j) + 3.8
            l.append(a1)
            l.append(c)
            l.append(b)
            m = min(l)
            mat.add(m, i, j)
            mat1.add(l.index(m) + 1, i, j)

    return mat1


def match(mat):
    pairs = []
    leng = mat.get_size()[0]
    a = b = leng - 1
    while (a != 0 and b != 0):
        path = mat.get_value(a, b)
        if path == 1:
            pairs.append((a, b))
            a -= 1
            b -= 1
        elif path == 2:
            a -= 1
        elif path == 3:
            b -= 1

    row = []
    a = 0
    b = 0
    pairs.reverse()
    while (a < leng):
        if b >= len(pairs):
            row.append(-1)
            a += 1
        elif (a != pairs[b][0]):
            row.append(-1)
            a += 1
        else:
            row.append(abs(pairs[b][0] - pairs[b][1]))
            a += 1
            b += 1

    return row


def point_value(im1, im2):
    points = []
    for i in range(im1.get_size()[1]):
        points.append(match(cost_matrix(im1, im2, i)))

    return points


point = point_value(l1, l2)
a = []
for i in range(len(point)):
    a.append(max(point[i]))

x = 255 / (max(a))

im = Image.open('/Users/doudou/Desktop/algorithm/cwk2/view2.png')
for i in range(l1.get_size()[0]):
    for j in range(l1.get_size()[1]):
        a = point[j][i]

        if (a == -1):
            im.putpixel((i, j), 0)
        else:
            a = int(a * x + 40)
            im.putpixel((i, j), a+128)

im.save('l_dot5.png')
