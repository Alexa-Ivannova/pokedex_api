# Siempre se maneja snake case en la creación de variables y funciones ejp: prueba_snake_case
# VARIABLES EN minusculas 
# CONSTANTE EN MAYUSCULAS

nombre_persona = "nombre"
numero = 23.5 

NOMBRE_PRUEBA = "así"
PRUEBA_DOS = "asa"

# Datos arreglos (array) objetos, tuplas, sets
# TUPLAS: tipos de datos, arreglos, no permite modificar los datos internos, se puede consultar pero NO SE PUEDE MODIFICAR (Casi no se usan)

tupla = ("perro", "gato", "raton")
# print(type(tupla))

#SET: Tipos d eestructuras de datos --> Permite almacenar info como arreglo, pero no permite duplicados, se escribe así:

ejemplo_set = {"perro", "gato", "raton", "perro"}

# DE LOS QUE MÁS SE USAN SON:
# LISTAS:
arreglo = ["nombres", "apellidos", "Telefono", 23]

# DICCIONARIOS: Son los objetos en JS, permiten guardar info con clave:valor

diccionario = {
    "nombre": "valor",
    "numero": 23,
    "arreglo": ["nombre", "apellido"]
}

# VALIDACIONES DE DATOS: Condicionales (if)
# DATOS LOGICOS: se escriben && = and --- || = or  --- ! = not  

# if (1 + 1 == 3) and (2 + 2 == 4):
#     print("verdadero")
# else:
#     print("Falso")

# IF ANIDADOS -- ELSE IF

color = "rojo"
# EJEMPLO: Esto de abajo esta mal a noser q sea la unica forma de dar solución
# if color == "rojo":
#     print("color calido")
#     if color == "azul":
#         print("Color frio")
#         if color == "verde":
#             print("Neutro")

#ELIF:

# if color == "verde":
#     print("Color verde")
# elif color == "negro":
#     print("Color negro")
# elif color == "Rojo":
#     print("color rojo")
# else:
#     print("No existe el color")

# FOR: Solo existe un for :D ... SIRVEN PARA TODOOOOS :D
# for QUE_VAS_A_ITERAR in DONDE_BUSCAR
# animals_list = ["leon","perro", "sapo", "Oso"]

# for animal in animals_list:
    # print(animal)

# crear diccionario, con key perro

# dog = {
#     "raza": "Criollo",
#     "edad": 3,
#     "patas": 4,
#     "nombre": "Toby"
# }

# for key, value in dog.items():
#     print("Aqui", value)

# numero = 10

# for recorrer in range(1, numero +1, 3):
#     print(recorrer)

# WHILE: Condicional de bucle -- Parecido al for, NECESITA CONDICIÓN VERDADERA "fusión for e if", si se cumple la condición siempre que se cumpla la condición

# contador = 1

# while contador < 5:
#     print(contador)
#     contador += 1

# CICLOS FOR Y WHILE, hay 2 condiciones q se usan para continuar o romper ejecución
# BREAK y CONTINUE

# for animal in animals_list:
#     if animal == "perro":
#         break
#     print(animal)

# while contador < 5:
#     print(contador)
#     contador += 1
#     if contador % 2 == 0:
#         break

    # LIST COMPREHENSIONS: Como se comprende la info -- Hacer q una lista extraiga datos escribiendo codigo mas cortico
    # Estrucutura: variable = [RESULTADO_SIEMPRE_ES_ITERAR for ITERAR in DONDE "SI SE NECESITA SE AGREGAN ACA LAS CONDICIONES"]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

multiplicar_por_dos = [numero * 2 for numero in lista_numeros]

# for numero in lista_numeros:
#     print(numero * 2)
# multiplos_de_dos = [numero for numero in lista_numeros if numero % 2 == 0]

# print(multiplos_de_dos)
# for numero in lista_numeros:
#     if numero % 2 == 0:
#         print (numero)
# DIC COMPREHENSIONS: Igual al anterior pero con diccionarios

# COMO EXTRAER DATOS DE LISTAS, DICCIONARIOS, SETS, TUPLAS
# LISTAS: slising lista[indice:] los : significan DESDE X punto hasta el final
# print(lista_numeros[2:4])

dog = {
    "raza": "Criollo",
    "edad": 3,
    "patas": 4,
    "nombre": "Toby"
}

#FORMA 1 Traer data con los corchetes me trae el valor de la llave seleccionada 
# print(dog["raza"])

# FORMA 2 Usando metodo get
# print(dog.get("patas"))

# SET: Son no indexados (NO TIENEN INDICES, solo se extraen for)

# TUPLAS: No son modificables se puede extraer info con for  o indice como una lista

# FUNCION SIN PARAMETROS:

# def saludar():
#     print("Hola mundo")
#     suma = 1 + 1
#     print("aca funcion saludar", suma)
#     return suma

# saludar()

# FUNCION CON PARAMETROS:

# def saludar_dos(nombre):
#     print(f"Hola {nombre}")

# saludar_dos("Alexa")

# cualquiera = saludar()

# print("Desde la variable cualquiera", cualquiera)

poderes = {
    "Charmander": "Fuego",
    "Picachu": "Rayo",
    "Eve": "Ternura"    
}

def ataque(pokemon, poder):
    poderes[pokemon]= poder

    fuego = 30
    rayo = 20
    ternura = 40
    rasguño = 15
    veneno = 20

    if pokemon == "Gengar":
        return veneno * 2
    if pokemon == "Charmander":
        return fuego * 2
    if pokemon == "Picachu":
        return rayo * 2
    if pokemon == "Eve":
        return ternura * 2 
    if pokemon == "Miaw":
        return rasguño* 2
    
    return "No coincide con la busqueda"

ataque_pokemon = ataque("Miaw", "Rasguño")


print(f"Funcion {ataque_pokemon}")
print(f"diccionario {poderes}")
# print(f"El ataque de Miaw es {ataque_pokemon}")

# CLASES: Palabra clave "clas" SE ESCRIBE PASCAL CASE ...Plantilla que define como se comporta un objeto y define como es el objeto... un objeto es una instancia q puede tener atributos (caracteristicas), metodos (Lo que hace) y funciones

class Pokemon:
    def __init__(self, nombre, tipo, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque

    def saludar(self):
        print(f"{self.nombre} te dice holavaya a domir!")
    
    def poder(self):
        return self.ataque * 2

charmander = Pokemon("Charmander", "Fuego", 50)
gengar = Pokemon("Gengar", "Fantasma", 30)

print(f"Instanciar {charmander.nombre}")

ataque_charmie = charmander.poder()
saludo_charmie = charmander.saludar()

# print(ataque_charmie)
print(saludo_charmie)