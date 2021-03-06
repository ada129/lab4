import random
import string
from PIL import Image, ImageDraw
#25.1
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
#25.2
import random

st1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
st2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
st3 = ['2', '3', '4', '5', '6', '7', '8', '9']
st4 = st1 + st2 + st3
 
 
def generate_password(m):
    pas = []
    pas.append(random.choice(st1))
    pas.append(random.choice(st2))
    pas.append(random.choice(st3))
    for i in range(0, m - 3):
        pas.append(random.choice(st4))
    random.shuffle(pas)
    return ''.join(pas)
 
 
def main(n, m):
    list_passw = set()
    while len(list_passw) < n:
        list_passw.add(generate_password(m))
    return list_passw
print("Случайный пароль из 7 символов:", generate_password(7))  
print("10 случайных паролей длиной 15 символов:")  
print(*main(10, 15), sep="\n")
#25.3
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
 #25.4
import random, string
 
 
def generate_password(m):
  x = random.randint(1, m-2)
  y = random.randint(1, m - x - 1)
  z = m - x - y
  
  l = []
  
  i = 0
  while i < x:
    n = random.choice(string.digits)
    if n != '1' and n != '0':
      l.append(n)
      i += 1
  
  i = 0
  while i < y:
    u = random.choice(string.ascii_uppercase)
    if u != 'I' and u != 'O':
      l.append(u)
      i += 1
  
  i = 0
  while i < z:
    w = random.choice(string.ascii_lowercase)
    if w != 'l' and w != 'o':
      l.append(w)
      i += 1
      
  random.shuffle(l)
  return ''.join(l)
 
def main(n, m):
  list_of_passwords = []
  for i in range(n):
    list_of_passwords.append(generate_password(m))
  return list_of_passwords
  
print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
            
#26.1

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
#26.2
def board(num, s):
    ni = Image.new("RGB", (num * s, num * s), (256, 256, 256))
    draw = ImageDraw.Draw(ni)
    b = (0, 0, 0)
    for i in range(num):
        for j in range(num):
            if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                draw.rectangle([j * s, i * s, j * s + s - 1, i * s + s - 1], b)
    ni.save('res.png', 'PNG')

#26.3
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
#27.1
im = Image.open("lena.pgm")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")
#27.2
def negative(source, res):
 
    source = Image.open(source)
 
    result = Image.new('RGB', source.size)
 
    for x in range(source.size[0]):
 
        for y in range(source.size[1]):
 
            r, g, b = source.getpixel((x, y))
 
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
 
    result.save(res, "JPEG")
