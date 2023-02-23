print ("///////////////////////////////1///////////////////////////////")

#Campus requiere administrar algunos datos de sus Campers
#como por ejemplo, la creación, eliminación o búsqueda de los
#developers, entre otros, por tal razón, ha solicitado el diseño de
#un programa que cuente con el siguiente menú como panel de
#control:

print ("---------------------------MENU---------------------------")
print ("1.\tCREAR GRUPO DE ARTEMIS\n")
print ("1.1\tLISTAR GRUPO DE ARTEMIS\n")
print ("1.2\tAGREGAR CAMPERS A ARTEMIS\n")
print ("1.3\tELIMINAR CAMPERS DE ARTEMIS\n")
print ("1.4\tORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n")
print ("1.5\tBUSCAR CAMPER EN LISTA DE ARTEMIS\n")
print ("2.\tCRAR GRUPO DE SPUTNIK\n")
print ("2.1\tLISTAR GRUPO DE SPUTNIK\n")
print ("2.2\tAGREGAR CAMPERS A SPUTNIK\n")
print ("2.3\tELIMINAR CAMPERS DE SPUTNIK\n")
print ("2.4\tORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n")
print ("2.5\tBUSCAR CAMPER EN LISTA DE SPUTNIK\n")
opcion=str(input("Digite opcion:\t"))

opcion = float(input("Digite opcion: "))
if opcion == 1.:
    print("///////////////////////////////Crear grupo artemis///////////////////////////////")
    name = input("Digite el nombre del grupo artemis: ")
    print(f"El grupo se llama {name}")

elif opcion == 1.1:
    print("///////////////////////////////Listar campers de artemis///////////////////////////////")
    list=['Pedro','Pascal','Alejo','Matias','Juan']
    print(list)

elif opcion == 1.2:
    print("///////////////////////////////Agregar campers a artemis///////////////////////////////")
    list=['Pedro','Pascal','Alejo','Matias','Juan']
    print(list)
    name = input("Digite el nombre del nuevo camper: ")
    list.insert(5,(name))
    print("El camper se ha añadido exitosamente:")
    print(list)

elif opcion == 1.3:
    print("///////////////////////////////Eliminar campers de artemis///////////////////////////////")
    list=['Pedro','Pascal','Alejo','Matias','Juan']
    print(list)
    name = int(input("Digite la posicion del camper que desea eliminar: "))
    del list[(name)]
    print("El camper se ha eliminado exitosamente:")
    print(list)

elif opcion == 1.4:
    print("///////////////////////////////Lista de artemis ordenada alfabeticamente///////////////////////////////")
    list=['Pedro','Pascal','Alejo','Matias','Juan']
    ordenados = sorted(list)
    print(ordenados)

elif opcion == 1.5:
    print("///////////////////////////////Buscar campers en la lista de artemis///////////////////////////////")
    list=['Pedro','Pascal','Alejo','Matias','Juan']
    print(list)
    name = int(input("Digite la posicion del camper que desea buscar: "))
    print(list[name])
    print("Camper encontrado")

elif opcion == 2.:
    print("///////////////////////////////Crear grupo sputnik///////////////////////////////")
    name = input("Digite el nombre del grupo sputnik: ")
    print(f"El grupo se llama {name}")

elif opcion == 2.1:
    print("///////////////////////////////Listar campers de sputnik///////////////////////////////")
    list=['Lina','Jana','Chucho','Pepe','Hernesto']
    print(list)

elif opcion == 2.2:
    print("///////////////////////////////Agregar campers a sputnik///////////////////////////////")
    list=['Lina','Jana','Chucho','Pepe','Hernesto']
    print(list)
    name = input("Digite el nombre del nuevo camper: ")
    list.insert(5,(name))
    print("El camper se ha añadido exitosamente:")
    print(list)

elif opcion == 2.3:
    print("///////////////////////////////Eliminar campers de sputnik///////////////////////////////")
    list=['Lina','Jana','Chucho','Pepe','Hernesto']
    print(list)
    name = int(input("Digite la posicion del camper que desea eliminar: "))
    del list[(name)]
    print("El camper se ha eliminado exitosamente:")
    print(list)

elif opcion == 2.4:
    print("///////////////////////////////Lista de sputnik ordenada alfabeticamente///////////////////////////////")
    list=['Lina','Jana','Chucho','Pepe','Hernesto']
    ordenados = sorted(list)
    print(ordenados)

elif opcion == 2.5:
    print("///////////////////////////////Buscar campers en la lista de sputnik///////////////////////////////")
    list=['Lina','Jana','Chucho','Pepe','Hernesto']
    print(list)
    name = int(input("Digite la posicion del camper que desea buscar: "))
    print(list[name])
    print("Camper encontrado")


print ("///////////////////////////////2///////////////////////////////")

#N atletas han pasado a finales en salto triple en los juegos
#olímpicos de 2022.

#Diseñe un programa que pida por teclado los nombres de cada
#atleta finalista y a su vez, sus marcas del salto en metros.

#Informar el nombre de la atleta campeona que se quede
#con la medalla de oro y si rompió récord, reportar el pago que
#será de 500 millones. El récord esta en 15,50 metros.

print("------nombre de atletas------")

nombre1 = input("Atleta Numero 1: ")
nombre2 = input("Atleta Numero 2: ")
nombre3 = input("Atleta Numero 3: ")

print("------Marcas de salto------")

atleta1 = int(input("Atleta Numero 1: "))
atleta2 = int(input("Atleta Numero 2: "))
atleta3 = int(input("Atleta Numero 3: "))

if  atleta1 > (atleta2 + atleta3)/2 :
        
        print("El atleta ",nombre1,"Botuvo la medalla de oro")
        
        if  atleta1 > 15.50:
            
            print("Rompio Record")   
                  
else:
     print("El atleta ",nombre2,"Botuvo la medalla de oro")    
     if  atleta2 > 15.50:
            print("Rompio Record")
            
     else:
      print("El atleta ",nombre3,"Botuvo la medalla de oro")    
     if  atleta3 > 15.50:
            print("Rompio Record")
            
            
print ("///////////////////////////////3///////////////////////////////")

#En pocos días comienza la vuelta a España y la federación
#colombiana de ciclismo, como incentivo ha determinado pagar
#un valor adicional. El programa pedirá por teclado el sueldo
#básico por kilometro recorrido, el número de kilómetros
#recorridos durante toda la vuelta, numero de kilómetros
#recorridos con la camiseta de líder.
#Calcular el valor a pagar total, si se sabe que si recorre en la
#bici más de 1800 kilómetros con la camiseta de líder, esos
#kilómetros se consideran especiales y tendrán un recargo de
#25%.
#El total de kilómetros por recorrer durante toda la vuelta serán
#3.277 kilómetros,el ganador de la vuelta a España recibirá 700
#millones de pesos.

kmCosto = int(input("sueldo básico por kilometro recorrido: "))
kmRecoridos = int(input("número de kilómetros recorridos durante toda la vuelta: "))
kmLider = int(input("kilómetros recorridos con la camiseta de líder: "))

costo = kmCosto * kmRecoridos

print("Valor: ",costo)

if kmLider >= 1800 :
       operacion = kmLider * 100 / 25
       print("Adicional: ",operacion)
elif  kmRecoridos > 3277:
       print("el ganador de la vuelta a España recibirá 700 millones de pesos.")

print ("///////////////////////////////4///////////////////////////////")

#Una empresa tiene 500 almacenes. Cada almacén debe
#reportar el nombre y 5 registros c/u, contiene el tipo de articulo
#y el número de unidades vendidas de ese artículo.

#Haga un programa en Python para determinar cuál fue el
#almacén que mas vendió, cual fue el articulo más vendido de
#ese almacén y cual el más vendido en general.

print("-------------------Almacen de Frutas-------------------")
Durazno = int(input("Duraznos vendidos: "))
bananos = int(input("Bananos vendidos: "))
peras = int(input("Peras vendidas: "))
manzanas = int(input("Manzanas vendidas: "))
naranjas = int(input("Naranjas vendidas: "))

d2 = dict([
    ("Duraznos",(Durazno)), 
    ("Bananos",(bananos)), 
    ("Peras",(peras)), 
    ("Manzanas",(manzanas)), 
    ("Naranjas",(naranjas)),
])

print(d2)

print("-------------------Almacen de Ropa-------------------")
camisas = int(input("Camisas vendidas: "))
pantalones = int(input("Pantalones vendidos: "))
boxers = int(input("Boxers vendidos: "))
Buzo = int(input("Buzos vendidos: "))
medias = int(input("Medias vendidas: "))


d1 = dict([
    ("Camisas",(camisas)), 
    ("Pantalones",(pantalones)), 
    ("Boxers",(boxers)), 
    ("Buzo",(Buzo)), 
    ("Medias",(medias)),
])

print(d1)


ropavendida = ((camisas)+(pantalones)+(boxers)+(Buzo)+(medias))
frutavendida = ((Durazno)+(bananos)+(peras)+(manzanas)+(naranjas))
print("ALMACEN QUE MÁS VENDIÓ: ")

if ropavendida > frutavendida:
    print("Almacen de ropa")
    print(ropavendida)

else: print("Almacen de fruta")
print(frutavendida)