print("No es la primera vez que hago esto pero imaginemos que si")

#Datos simples
"string" #cadena de texto
"""tus datos son:
nombre: Garp
    id:pascdart """
int("40") #enteros
float("48.2") #flotantes
bool("false") #boolean

#Variables
x = "8"
nombre  = "Garp"
numero = 10 + 5
numero += 1 #el valor que ya tiene más lo que este despues del igual
numero -= 1 #el valor que tiene menos lo que esta despues del igual
bienvenida = "Hola " + nombre + " ¿como estas?" #concatenar con +
bienvenida2 = f"Hola {nombre} ¿que tal tu dia?" # concatenar con f-strings

#variables con snake_case
nombre_completo_del_viejo_master = "D Garp"

print(bienvenida)
del bienvenida #operador para borrar datos
print(x)
print(nombre)
print(numero)
print(bienvenida2)

#operadores de pertenencia (in/ not in)
print("Garp" in bienvenida2) #true
print("Garp" not in bienvenida2) #false

##Datos compuestos
lista = ["D Garp", "Enel", True, 1.70] #lista o matriz
tupla = ("D Garp", "Enel", True, 1.70) #inmodificable

#esto es valido
lista[3] = False 

#esto no, ademas aunque sea tupla esta bien escrito en corchetes
#tupla[3] = False 

#creando un conjunto (set)
conjunto = {"D Garp", "Enel", True, 1.70, "Enel"} #no muestra datos duplicados
#no accede a elementos por indice pues posee datos desordenados

#creando un diccionario (dict)
diccionario = {
    "nombre" : "D Garp",
    "persona" : "Enel",
    "esta_emocionado" : True,
    "altura" : 1.71,
    "dato_duplicado" : "Enel"
} # "key" : "value"

print(lista[3])
print(conjunto)
print(diccionario["nombre"])
print(diccionario["altura"] + 2)