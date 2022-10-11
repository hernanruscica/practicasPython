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

