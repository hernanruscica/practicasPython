
#4.5.1.2 Creando funciones con dos parámetros

#dos funciones para las conversiones
def pies_pulgadas_a_metros(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def libras_a_kilos(lb):
    return lb * 0.45359237

#calcula el indice de masa corporal. valores en kilos y metros
def imc(peso, altura):
    #condiciones con la \ hago que la linea continue en el reglon de abajo
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    return peso / altura ** 2

def pedir_datos(sistema_medida):
    datos = []    
    if sistema_de_medida == 1 :        
        datos.append(float(input("Ingrese su peso en Kilogramos: ")))
        datos.append(float(input("Ingrese su altura en metros: ")))
    if sistema_de_medida == 2 :
        peso_libras = float(input("Ingrese su peso en Libras: "))
        altura_pies = float(input("Ingrese su altura en pies y pulgadas\n1ro, los pies: "))
        altura_pulgadas = float(input("Ingrese su altura en pies y pulgadas\n2do, las pulgadas: "))
        datos.append(libras_a_kilos(peso_libras))
        datos.append(pies_pulgadas_a_metros(altura_pies, altura_pulgadas))
    return datos
    

#ingreso de datos y pregunta si los datos estan en sistema ingles o sistema metrico?
sistema_de_medida = int(input("Los datos estan en: \n 1. Sistema metrico.\n2. Sistema ingles.\n"))
#llamo a la funcion que pide datos
datos_sistema_metrico = pedir_datos(sistema_de_medida)
peso = datos_sistema_metrico[0]
altura = datos_sistema_metrico[1]
mi_imc = imc(peso, altura)
print("Su I.M.C. es : ", mi_imc)
