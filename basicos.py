#EL COMENTARIO 
print("hola mundo")
print("adios mundo")

#operadores aritméticos
5+1
print(5+1)
print(5-1)
print(5*2)
print(5/2)
#precendecia de operadores
print(5+8*(3+2))

#tipos de datos
print(type(2))
print(type(2.2))
print(type("texto"))
print(type('texto'))
print(type("2"))

#variables
mensaje = "Esto es un asalto" #tipo implicito
print(mensaje)
mensaje = "Mensaje alterado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

mis3animales = "perico, gallo, chivo"
print(mis3animales)
tresáñimales = "perico, gallo, chivo"
print(tresáñimales)

txt1 = "Mi txt"
txt2 = "Mi segundo txt"
print(txt1 + txt2)

#transforman str() int() float()
edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de dato de edad es: " + str(type(edad)))

import math
#morado= funciones #amarillo= valores
grados = 45.0
radianes = (grados * math.pi)/ 180
seno = math.sin(radianes)
print("seno de 45° : " + str(seno))

def saludar(nombre): 
    print("Hola" + nombre)
    print("bb")
    print("cómo has estado?")

def despedir():
    print("ah bueno")
    print("te me cuidas xD")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("se acabo la funcion")
saludar(" ana")
despedir()

frase = concatenar("Siempre te voy", " a querer") 
print(frase)