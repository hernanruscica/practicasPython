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

###########################################################

my_list =[[c for c in range(r)] for r in range(3)]
for element in my_list:
    if len(element) < 2:
        print() #dos lineas vacias

######################################################
x, y, z = 3, 2, 1          
z, y, x = x, y, z
print(x, y, z) #1 2 3
######################################################
try:
    1 / 0
except ZeroDivisionError as division_por_cero:
    print(division_por_cero.args) #('division by zero',)
######################################################

#// Realiza la división con resultado de número entero. Por ejemplo: 18 // 5 = 3
x = 16
while x > 0 :
    print('*', end='')
    x //= 2 
# x = 16 *
# x =  8 **
# x =  4 ***
# x =  2 ****
# x =  1 *****
# x =  0 *****
######################################################
t = (1, 2, 3, 4)
t = t[-2:-1] #3
t = t[-1] #3 
print(t) #3

###################################################### 

def fun(d, k, v):
    d[k] = v #objeto my_dictionary['1'] = 'v'
my_dictionary = {}
print(fun(my_dictionary, '1', 'v')) #none

######################################################
def fun(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s
for x in fun(3):
    print(x, end='')
######################################################
def fun(a, b, c = 0):
    print(a,b, c) #0 0 0
fun(a=0, b=0, c=0) 
######################################################
print("a", "b", "c", sep="'") #a'b'c
######################################################
i = 4 
while i > 0:
    i -= 2 
    print("*")
    if i == 2:
        break
else:
    print("*")
######################################################
print(len((1,)))
x
class A:
    def __init__(self, v):
        self._a = v + 1
a = A(0)
print(a._a) #1
######################################################
x = "\"
print(len(x))
######################################################
my_string_1 = 'Bond'
my_string_2 = 'James Bond'
print(my_string_1.isalpha(), my_string_2.isalpha()) #True False
######################################################
class clase:
    _a = 1    
    def __init__(self, a):
        self._a = a    
    def fun(self):
        return self._a
miobjeto = clase()
mivariable =  miobjeto.fun()
print(mivariable)
######################################################
d = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0
for y in range(len(d)): 
    x = d[x] 
print(x) #0
######################################################
print(len([i for i in range(0, -2)])) #0
######################################################
y = input()
x = input()
print(x + y) #21
######################################################
try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
#####################################################
class A:
    A = 1
    def __init__(self):
        self.a = 0
print(hasattr(A, 'A')) #True
#####################################################
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x = X()
z = Z()
print(isinstance(x, Z), isinstance(z, X)) # False True
#####################################################
x = """
"""
print(len(x)) #1
#####################################################
def fun(x):
    return 1 if x % 2 != 0 else 2
print(fun(fun(1)))
#####################################################
class Class:
    def __init__(self):
        pass
object = Class()
print(object)
#####################################################

a = True
b = False
a = a or b
b = a and b
a = a or b
print(a, b) #True False

from datetime import timedelta
delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta) #14 days, 11:00:00

d = {'one': 1, 'three': 3, 'two': 2}
for k in sorted(d.values()):
    print(k, end='') #123


import calendar
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ") #6 0 1 2 3 4 5 

z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)

try:
    raise Exception
except BaseException:
    print("a", end='')
else:
    print("b", end='')
finally:
    print("c")
  """  
class A:
    def __init__(self, name):
        self.name = name
a = A("class")
print(a)