"""
Mediante los ejemplos de diferentes implementaciones de una pila, 
se explica la diferencia entra el enfoque procedimental y el de orientado a objetos.
clase 3.2.1.2
La pila: el enfoque procedimental.
primero un programa que hace push y pop de una pila, implementada con una lista
"""
stack = []
def push(val):
    stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop()) #1
print(pop()) #2
print(pop()) #3


"""
3.2.1.4 La pila, el enfoque orientado a objetos
"""
class Stack:  # Definiendo la clase de la pila.
    def __init__(self):  # Definiendo la función del constructor.
        
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    def my_len(self):
        return len(self.__stack_list)

stack_object = Stack()  # Instanciando el objeto.
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
print(stack_object.pop()) #1
print(stack_object.pop()) #2

longitud_lista = stack_object.my_len()
print('Longitud de la lista dentro del objeto stack:', longitud_lista) #1

#3.2.1.9 instanciando tres objetos stack (continua el ejemplo anterior)
little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())

#3.2.1.10 agregando una subclase a Stack
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    # 3.2.1.11 Agrego el nuevo comportamiento de push()
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)


#3.2.2.12 Ejemplo completo
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())


#3.2.1.14 Laboratorio 1: Pila Contadora

class Stack:
    def __init__(self):
        self.__stk = []
    def push(self, val):
        self.__stk.append(val)
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        # Llena el constructor con acciones apropiadas.
        Stack.__init__(self)
        self.__counter_push = 0
        self.__counter_pop = 0
    def get_counter(self):
        # Presenta el valor actual del contador al mundo.
        return self.__counter_pop    
    def push(self, val):
        self.__counter_push += 1
    def pop(self):
        # Haz un pop y actualiza el contador.
        self.__counter_pop += 1
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
cantidad_pops = stk.get_counter()
print(cantidad_pops)

# 3.2.1.15 Colas alias FIFO
"""
Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos del final de la lista.
Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala cuando get() intentes operar en una lista vacía.
Completa el código que te proporcionamos en el editor. Ejecútalo
"""

#class ColaError:   #Eligir la clase base para la nueva excepción.
    #  Escribe código aquí.    

#cola
class Queue:
    def __init__(self):
        # Escribe código aquí.
        self.__stack = []

    def put(self, elem):
        # Escribe código aquí.
        self.__stack.insert(0, elem)

    def get(self):
        # Escribe código aquí.
        ultimo = self.__stack[-1]
        del self.__stack[-1]
        return ultimo

cola = Queue()
cola.put(1)
cola.put("perro")
cola.put(False)

try:
    for i in range(4):
        print(cola.get())
except :
    print("Error de Cola")


######################################################################################
#3.3.1.2 POO: Propiedades
#agregando vaiables de instancias.
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

######################################################################################
#3.3.1.3 Variables de clase
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)#{'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2.counter)#{'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3.counter)#{'_ExampleClass__first': 4} 3

######################################################################################
#3.3.1.4 Variables de clase (continuacion)

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter) #{'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2._ExampleClass__counter) #{'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3._ExampleClass__counter) #{'_ExampleClass__first': 4} 3


###########################################################################################
#3.3.1.5 variables de clase (continuacion)
#Diferencias entre los dos dict
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__) #{'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7f5fc056f0e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
example_object = ExampleClass(2)

print(ExampleClass.__dict__) #{'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7f5fc056f0e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
print(example_object.__dict__) # {}


###########################################################################################
#3.3.1.6 variables de clase (continuacion) 
#Accediendo a un atributo de clase que no existe, tira error
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a) #1
print(example_object.b) #Error



############################################################################################
#3.3.1.7 hasattr() y AttributeError
class ExampleClass:
    counter = 0
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b) #1
except AttributeError:
    pass

#prueba de la funcion hasattr()
#recibe nombre de clase u objeto y el atributo a buscar.
print(hasattr(example_object, 'b'))#False
print(hasattr(example_object, 'a'))#True
print(hasattr(ExampleClass, 'counter'))#True

############################################################################################
#3.3.1.8 Mas pruebas de hasattr()
class ExampleClass:
    attr = 1
    a = 1
    def __init__(self):
        self.b = 2

example_object = ExampleClass()

print(hasattr(ExampleClass, 'attr')) #True
print(hasattr(ExampleClass, 'prop')) #False
print(hasattr(example_object, 'b')) #True
print(hasattr(example_object, 'a')) #True
print(hasattr(ExampleClass, 'b')) #False
print(hasattr(ExampleClass, 'a')) #True


########################################################################################
#3.3.1.9 RESUMEN DE SECCIÓN
class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Variable de instancia.
        self.__delta = 3 # Variable de instancia privada.


obj = Sample()
obj.beta = 2  # Otra variable de instancia (que existe solo dentro de la instancia "obj").
print(obj.__dict__) #{'alpha': 1, '_Sample__delta': 3, 'beta': 2}



##########################################################################################
# 3.4.1.2 
#El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.
class Classy:
    varia = 2
    
    def other(self):
        print("otro: metodo dentro de la clase")
        
    def method(self):
        print(self.varia, self.var)
        self.other()

obj = Classy()
obj.var = 3
obj.method()
print(obj.varia)

###########################################################################################
#3.4.1.4 Formas de acceder a los metodos, segun su declaracion.
class Classy:
    def __init__(self, value = None):
        self.var = value        
    def visible(self):
        print("visible")    
    def __hidden(self):
        print("oculto")

obj_1 = Classy("objeto")
obj_2 = Classy()

print(obj_1.var) #
print(obj_2.var) #None

obj_2.visible() #visible

try:
    obj_2.__hidden() #Tira Exception 
except:
    print("fallido") #fallido
    
obj_2._Classy__hidden() #Manera Correcta de llamar al metodo __hidden() y muestra "oculto"


###########################################################################################
#3.4.1.6 - 3.4.1.7
#propiedad __name__ que dvuelve un string con el nombre de la clase con que se instancio el objeto.
class Classy:
    pass

print(Classy.__name__)
obj = Classy()
nombre_clase_obj = type(obj)
print(nombre_clase_obj.__name__)

#ejemplos del metodo __module__()
print(Classy.__module__)
print(obj.__module__)



###########################################################################################
#3.4.1.8
# __bases__ es una funcion que devuelve las superclasses de un objeto
class SuperOne:
    pass
class SuperThree:
    pass
class SuperTwo(SuperThree):
    pass
class Sub(SuperOne, SuperTwo):
    pass
def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

###########################################################################################
#3.4.1.10
"""
incIntsI() toma un objeto de cualquier clase, escanea su contenido para encontrar todos los atributos 
enteros con nombres que comienzan con i, y los incrementa en uno.
"""
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():  #escanea el atributo __dict__, buscando todos los nombres de atributos.
        if name.startswith('i'): # si un nombre comienza con i...
            val = getattr(obj, name) # para obtener su valor actual
            if isinstance(val, int): #comprueba si el valor es de tipo entero
                setattr(obj, name, val + 1) #toma 3 argumentos: un obj, el nombre de la propiedad  y el nuevo valor de la propiedad.


print(obj.__dict__) #{'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
incIntsI(obj)
print(obj.__dict__) #{'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}


##############################################################################################
#LAB 3.4.1.12 La clase Timer
"""

"""
class Timer:
    def __init__(self, horas = 0, minutos = 0, segundos = 0 ):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        
        return formatear_tiempo(self.__horas, self.__minutos, self.__segundos)

    def next_second(self):
        self.__segundos += 1
        if self.__segundos >= 60:
            self.__segundos = 0
            self.__minutos += 1
            
        if self.__minutos >= 60:
            self.__minutos = 0
            self.__horas += 1
        
        if self.__horas >= 24:
            self.__horas = 0
            

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos < 0:
            self.__segundos = 59
            self.__minutos -= 1
            
        if self.__minutos < 0:
            self.__minutos = 59
            self.__horas -= 1
        
        if self.__horas <= 0:
            self.__horas = 23


def formatear_tiempo(h, m, s):
    
    horas_str = str(h)
    minutos_str = str(m)
    segundos_str = str(s)
    
    if h >= 0 and h < 10 :
        horas_str = "0" + horas_str
    
    if m >= 0 and m < 10 :
        minutos_str = "0" + minutos_str
    
    if s >= 0 and s < 10 :
        segundos_str = "0" + segundos_str
    
    return horas_str + ":" + minutos_str + ":" + segundos_str
    
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

