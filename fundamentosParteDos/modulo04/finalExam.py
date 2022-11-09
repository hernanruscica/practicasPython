"""
class A:
    pass
class B:
    pass
class C(A, B):
    pass
print(issubclass(C, A) and issubclass(C, B))

##################################################

my_string = 'abcdef'
def fun(s):
    del s[2]
    return s
print(fun(my_string))

print(__name__);

##################################################

my_list = [1, 2, 3, 4]
my_list = list(map(lambda x: 2*x, my_list))
print(my_list) #[2, 4, 6, 8]

##################################################

str_1 = 'string'
str_2 = str_1[:]
str_1 += 'o'
print(str_1, str_2)

######################################################

from datetime import datetime
datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%Y/%m/%d %H:%M:%S')) #2019/11/27 11:27:22

######################################################

s =  open("file.txt", "rt")
q = s.readlines()
print(q)

######################################################

v = 1 + 1 // 2 + 1 / 2 + 2
print(v) #3.5

class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()
a = A()
print(a.g()) #TypeError: A.g() takes 0 positional arguments but 1 was given

###########################################################

import os
os.makedirs('pictures/thumbnails')
os.rmdir('pictures')
#OSError: [WinError 145] El directorio no está vacío: 'pictures'

###########################################################


class A:
    A = 1
    def __init__(self, v = 2):
        self.v = v + A.A
        A.A += 1
    def set(self, v):
        self.v += v 
        A.A += 1
        return 
a = A()  #self.v = 3 y A.A = 1
a.set(2) #self.v = 5 y A.A = 2
print(a.v) #5

###########################################################

def fun(par2, par1):
    return par2 + par1
print(fun(par2 = 1, 2))
#SyntaxError: positional argument follows keyword argument

###########################################################

t = (1, )
t = t[0] + t[0]
print(t) #2

###########################################################


def a(x):
    def b():
        return x + x
    return b
x = a('x') #xx
y = a('')  #
print(x() + y()) #xx

###########################################################

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
for x in d.keys(): #keys son 2 y 1
    print(d[x][1], end="") #24
"""

my_list =[[c for c in range(r)] for r in range(3)]
for element in my_list:
    if len(element) < 2:
        print() #dos lineas vacias
