print("///////////////////////////1///////////////////////////////")

#1. Qué operadores utiliza Python en los siguientes casos:
#A. División Modular
#B. Exponenciación
#C. División que retorne entero.

num = 10
num1 = 5
print(f"A. División Modular: {num}%{num1}= {num%num1}")
print(f"B. Exponenciación: {num}**{num1}= {num**num1}")
print(f"C. División que retorne entero: {num}//{num1}= {num//num1}")

print("///////////////////////////2///////////////////////////////")

#2. En la jerarquía de operadores, cuáles son los que más
#prioridad tienen cuando el intérprete de Python los evalúa?

print("<Mayor> Operaciones entre paréntesis: ()")
print("Potencia: **")
print("Multiplicación y División, módulo o residuo,División entera: *, /, %, //")
print("Suma y resta: +, -")
print("Operadores relacionales: <, <=, >, >=, !=, ==")
print("Operador lógico AND: And")
print ("<Menor> Operador lógico OR: Or")
x = 5
y = 2
z = x + 3 * y
print("El producto tiene prioridad sobre la suma:",z)
z = (x + 3) * y
print("Los paréntesis tienen prioridad:",z)

print("///////////////////////////3///////////////////////////////")

#3. Si hay operadores de igual precedencia, en qué orden se
#ejecutan?
#A. De izquierda a derecha
#B. De derecha a izquierda

print ("Se ejecutan de izquierda a derecha")
operacion = x + x - y + y -x
print ("operacion = x + x - y + y -x =",operacion)

print("///////////////////////////4///////////////////////////////")
#4. Que son las expresiones regulares en Python?

print ("Las expresiones regulares son expresiones comodín que definen patrones de caracteres a emparejar y extraer de una cadena de texto.")

print("///////////////////////////5///////////////////////////////")
#5. Enumere 5 tipos de datos en Python y suministre un valor de
#ejemplo de cada uno.

numero = 12
numero_flotante = 14.4
numero_complejo = 7+6j
nombre = "Sebastian"
verdadero_falso = 3==3
print ("numero:",type(numero))
print ("numero_flotante:",type(numero_flotante))
print ("numero_complejp",type(numero_complejo))
print ("String",type(nombre))
print ("verdadero_falso",type(verdadero_falso))

print("///////////////////////////6///////////////////////////////")
#6. En sus propias palabras, qué son las funciones
#preconstruidas y proporcione 2 ejemplos.

print("Son funciones ya pre establesidas por Python para las diferentes opreaciones que necesitemos para realizar un proceso")
print("print(): permite mostrar en pantalla")
print("range(): Crea un rango de números")
ñ = range(8) 
print (list(ñ))

print("///////////////////////////7///////////////////////////////")

#7. Cuál es la diferencia entre un condicional simple y un
#condicional compuesto?

print("Condicional simple: Cuando se presenta la elección tenemos la opción de realizar una actividad o no realizar ninguna.")
print("Condicional compuesta: Cuando se presenta la elección tenemos la opción de realizar una actividad u otra. Es decir tenemos actividades por el verdadero y por el falso de la condición.")
calculo = 3
calculo2 = 2
if calculo > calculo2:
    print("correcto")
else:
    print("incorreto")

print("///////////////////////////8///////////////////////////////")

#8. Escriba un bloque cualquiera de código en Python en donde
#utilice 2 condicionales (if) anidados.

años = 20

if años == 20:
    print("Estas bien")

if años > 20:
    print("Viejo")

if años < 20:
    print("Joven")

print("///////////////////////////9///////////////////////////////")

#9. Construya un algoritmo en Python, que permita ingresar la
#información de un empleado e imprima el nombre, los
#apellidos y la antigüedad. Los datos que se deben solicitar
#son los siguientes:
#*Nombre * Teléfono *Año de ingreso a la empresa
#*Apellidos *Edad.


nombre = input("Cual es tu nombre?: ")
telefono = input("Tu telefono?: ")
añ = input("Año que ingreso a la empresa?: ")
apellidos = input("Sus apellidos son?: ")
edad = input("Su edad?: ")

rt=str(añ)

print("Nombre: ",nombre)
print("Telefono: ",telefono)
print("Años que a trabajado en la empresa: ",)
print("Apellidos: ",apellidos)
print("Edad: ",edad)


print("///////////////////////////10///////////////////////////////")

#10. En su casa le solicitan que realice un algoritmo en Python,
#que permita calcular el valor a pagar por concepto de
#energía eléctrica. Los datos que se conocen son los
#siguientes:
#- Mes de consumo - Valor kw
#-Total kw consumido en el mes - estrato

mes = input("Mes de consumo?: ")
kw = input("Valor kw: ")
consumo = input("Total kw consumido en el mes?: ")
estrato = input("Estrato?: ")

costo=mes*consumo/kw

print("Su valor a pagar es: ",costo)