

#Otro ejemplo, definiendo mi variable global desde afuera de la funcion
global mi_variable_global
mi_variable_global = 22

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)
    #print(mi_variable_global)
    mi_variable_global = 33


var = 1
my_function()
print(var)
print(mi_variable_global)

