import random
import string
from PIL import Image, ImageDraw

def passgen(n, nums):
    numeric = ([random.randint(-10, 10) for i in range(n)])
    numeric = str(numeric)
    numeric = numeric.replace('[', ' ')
    numeric = numeric.replace(']', ' ')
    numeric = numeric.replace(',', '')
    l = ''.join(random.choice(string.ascii_letters) for i in range(n))
    p = ''.join(random.choice(string.punctuation) for i in range(n))
    prom = numeric + l + p
    res = ''.join(random.sample(prom, len(prom)))
    # print(res)
    if nums == 1:
        res = numeric
        print(res)
        print('первая степень')
        return res

    elif nums == 2:
        prom = l + numeric
        res = ''.join(random.sample(prom, len(prom)))
        print(res)
        print('втораая степень')
        return res
    elif nums == 3:
        prom = numeric + l + p
        res = ''.join(random.sample(prom, len(prom)))
        print('третья  степень')
        print(res)

    else:
        print('wrong number')


if __name__ == '__main__':
    q = int(input("сколко паролей нужно?"))
    for i in range(q):
        n = 12
        nums = 3
        passgen(n, nums)
#
import random
from itertools import count
import numpy as np


class Monte_Karlo():
    stop_count = 100000000

    def calc(self, points_am=10000, seed=0):
        try:
            points_am = int(points_am)
        except:
            err = "error converting value of points_am to int type"
            raise ValueError(err)
            return

        random.seed(seed)
        in_circle = 0
        i = points_am if points_am <= Monte_Karlo.stop_count else Monte_Karlo.stop_count
        while i >= 0:
            x = random.random()
            y = random.random()
            if x ** 2 + y ** 2 <= 1:
                in_circle += 1
            i -= 1
        pi = 4 * in_circle / points_am
        print('pi = {:.8f}. Total points = {} points within = {}'.format(pi, points_am, in_circle))

    def calc_compare(self, start=10000, mul=10, stop=5):
        try:
            start = int(start)
            mul = int(mul)
            stop = int(stop)
        except:
            err = "error converting value of points_am to int type"
            raise ValueError(err)
            return

        counts = count(1)
        for iter in counts:
            if iter > stop:
                break
            print('iter: {}'.format(iter))
            self.calc(start * mul ** iter)

        #########################################################################################################################

    def calc_with_np(self, points_am=10000, seed=0):
        try:
            points_am = int(points_am)
        except:
            err = "error converting value of points_am to int type"
            raise ValueError(err)
            return

        points_am = points_am if points_am <= Monte_Karlo.stop_count else Monte_Karlo.stop_count
        np.random.seed(seed)
        x_arr = np.random.random(points_am)
        y_arr = np.random.random(points_am)
        sq = np.add(x_arr ** 2, y_arr ** 2)
        in_circle = sq[sq <= 1]
        pi = 4 * in_circle.shape[0] / points_am
        print('pi = {:.8f}. Total points = {} points within = {}'.format(pi, points_am, in_circle.shape[0]))

    def calc_compare_with_np(self, start=10000, mul=10, stop=5):
        try:
            start = int(start)
            mul = int(mul)
            stop = int(stop)
        except:
            err = "error converting value of points_am to int type"
            raise ValueError(err)
            return

        counts = count(1)
        for iter in counts:
            if iter > stop:
                break
            print('iter: {}'.format(iter))
            self.calc_with_np(start * mul ** iter)
#

def gradient(color):
    color = color.upper()
    im = Image.new("RGB", (512, 200), (0, 0, 0))
    pixels = im.load()
    r = 0
    g = 0
    b = 0
    if color == 'R':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                r += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'G':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                g += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'B':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                b += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    im.save('res.png')
#
def board(num, s):
    ni = Image.new("RGB", (num * s, num * s), (256, 256, 256))
    draw = ImageDraw.Draw(ni)
    b = (0, 0, 0)
    for i in range(num):
        for j in range(num):
            if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                draw.rectangle([j * s, i * s, j * s + s - 1, i * s + s - 1], b)
    ni.save('res.png', 'PNG')

#
def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = im.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                pixels2[i, j] = r, g, b
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
    res.save("res.jpg")
#
im = Image.open("lena.pgm")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")