'''
Se solicita crear un programa que permita ejecutar mediante una función, este deberá preguntar al usuario si quiere ejecutar el programa.
La función debe de tener una arrays esta tendrá los nombres de los integrantes del grupo, mediante un for recorrerá los índices del arrays 
para luego mostrarlo como un menú estos datos se mostrarán uno de bajo del otro.

Luego se solicita que pida al usuario ingresar texto desde el teclado este dato a ingresar deberá ser el nombre de uno de los integrantes 
del grupo si el usuario se equivoca N número de veces indicárselo al usuario y lo devolverá a un paso previo. 
Según el nombre ingresado mostrar los datos siguientes:
Nombres
Apellidos
Sexo
Edad
Departamento
Municipio
Dirección
Luego indicar que, si desea consultar otro dato de los integrantes, si su respuesta es no finalizar programa.'''

#Inicio del programa

print("========================================================")
print("================ Bienvenido al programa ================")
print("========================================================\n")

#Datos que vamos a utilizar para efectuar el programa

integrantes = ["Antony Tobías", "Andrea Nuñez", "Geovanny Gómez", "Kevin Francisco", "Mauricio Romero"]
antony = '''Nombres: Antony Eleazar
Apellidos: Tobías Beltrán
sexo: Masculino
Edad: 17 años
Departamento: Chalatenango
Municipio: Chalatenango
Direccion: Colonia Fátima'''

andrea ='''Nombres: Andrea Alexandra
Apellidos: Nuñez Morán
sexo: Femenino
Edad: 17 años
Departamento: Chalatenango
Municipio: Chalatenango
Direccion: Barrio San Antonio'''

geovanny ='''Nombres: Franklin Geavanny
Apellidos: Gómez
sexo: Masculino
Edad: 17 años
Departamento: Chalatenango
Municipio: Chalatenango
Direccion: Colonia Fátima'''

kevin = '''Nombres: Kevin
Apellidos: Francisco
sexo: Masculino
Edad: 17 años
Departamento: Chalatenango
Municipio: Chalatenango
Direccion: Cerca del Destacamiento Militar 1'''

mauricio = '''Nombres: Mauricio Imanol
Apellidos: García Romero
sexo: Masculino
Edad: 17 años
Departamento: Chalatenango
Municipio: Chalatenango
Direccion: Cantón San José'''


#Empieza el nucleo del programa donde le preguntamos al usuario que si lo quiere usar

start = input("¿Quieres usar el programa, si/no? ")

#si lo quiere usar y escribe si pasara por el IF y le mostrará al usuario la lista de los integrantes

if start.lower() == "si" or start.lower() == "sí":
    print("Lista de integrantes")

#la lista se recorrerá en un FOR que además ennumerará a los integrantes

    for i in range(len(integrantes)):
        print(f"{i+1}. {integrantes[i]}")
        
#construimos la estructura while qu usaremos cuando el usuario se equivoque o quiera usar de nuevo el programa
    while True:
        nombre = input("\n¿De qué integrante de nuestro grupo quieres saber sus datos? ") #preguntamos a quien de los integrantes quiere poner

#Hacemos la estructura IF para cubrir las variables necesarias de los integrantes que ponga y la forma en la que los ponga
        if nombre.lower() == "antony" or nombre == "tobías" or nombre == "antony tobías":
            print("================================================")
            print(antony)
            print("================================================")
        elif nombre.lower() == "andrea" or nombre.lower() == "nuñez" or nombre.lower() == "andrea nuñez":
            print("================================================")
            print(andrea)
            print("================================================")
        elif nombre.lower() == "geovanny"or nombre.lower == "gómez"or nombre.lower == "geovanny gómez":
            print("================================================")
            print(geovanny)
            print("================================================")
        elif nombre.lower() == "kevin" or nombre.lower() == "francisco"or nombre.lower() == "kevin francisco":
            print("================================================")
            print(kevin)
            print("================================================")
        elif nombre.lower() == "mauricio" or nombre.lower() == "romero" or nombre.lower() == "mauricio romero":
            print("================================================")
            print(mauricio)
            print("================================================")
#terminaos la parte necesaria por si el usuario se equivoca
        else:
            print("Nombre de integrante no es válido. Prueba de nuevo.") 
            continue
# terminamos la parte final de la estructura para cuando el usuario quiera poner otro integrante

        otro = input("¿Quieres buscar otro integrante? (si/no) ") 
        
# Y si no lo desea rompemos el bucle
        if otro.lower() == "no":
            break
        elif otro.lower() == "si":
            print("perfecto")
            
        
            
#Terminamos el IF principal para cuando el usuario no quiera usar el programa
else:
    print("\nEstá bien, vuelve cuando quieras.\n")
# indicamos el fin del programa

print("\nFin del programa, Gracias por usarlo\n")