import math
import os
import random
import turtle as t
import colorsys
import socket as s

area_circulo = 1
sqrt2 = 2
mult_lista_previa = 3
factori = 4
cuenta_regresiv = 5
sumar_digit = 6
suma_matrices= 7
palindrom=8
gráfica=9
ip_nom=10
exponent=11
traducic=12
entero_a_binario= 13
salir = 0

def imprimir_menu():
    os.system('cls')     
    print(f'''    M E N U :
{area_circulo})  Area/circulo
{sqrt2})  Sqrt
{mult_lista_previa})  Multiplicar una lista
{factori})  Factorial
{cuenta_regresiv})  Cuenta regresiva
{sumar_digit})  Sumar digitos
{suma_matrices})  Sumar matrices
{palindrom})  Palíndromo
{gráfica})  Gráfica en turtle
{ip_nom}) Nombre_ip del equipo
{exponent}) Elevar a una potencia
{traducic}) Traducir de binario o hexa a entero
{entero_a_binario}) Traducir de entero a binario
{salir})  Salir''')

def area_del_circulo ():
    r= float(input('Digita el radio: '))
    a = math.pi * (r**2)
    l = 2 * math.pi * r
    print (f" El área de tu circulo es: {a: .2f} m2")
    print (f" Y su longitud: {l: .2f} m")    
        
def sqrt ():
    num= float(input('Ingresa un número: '))
    if num > 0:
        num2= math.sqrt(num)    
        print(f' Su raiz cuadrada es:  {num2: .2f}')
    elif num <= 0:
        print('Error..')
            
def multiplicar_lista():
    lista= list(range(1, 21))    
    print('Lista original: ')    
    for i in lista:
        print(i, end= ', ')
    valor= int(input('\nDigita un valor: '))
    for indice, i in enumerate(lista):  
        lista[indice]*= valor        
    print(f'\nLista final por el valor {valor}: ')
    for i in lista:
        print( i, end= ', ')

def factorial(numero):                    
    if numero < 0:
        print (" Error, el número debe ser positivo")    
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
            s1= "{:,}".format(factorial)
        print (f" El factorial del numero {numero} es: {s1}\n")
            
def cuenta_regresiva(num):               
    if num>0:
        print(num, end=' ')
        cuenta_regresiva (num - 1)
    else:
        print('\n Booom...!')   

def sumar_digitos(num):  
    if num == 0:
        suma = 0     
    else:
        suma= sumar_digitos (int(num/10)) + (num % 10)
        print (suma, end=' ')  
        
    return suma

def suma_de_matrices(n):
    print(f'Realizar la suma de matrices {n} x {n}: \n')
    m1= [[random.randint(1, 50) for j in range(n)] for i in range(n)]
    m2= [[random.randint(1, 50) for j in range(n)] for i in range(n)]
    resultado= [[m1[i][j] + m2[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):       
        if i == n//2:
             print(f'{m1[i]} + {m2[i]} = {resultado[i]}')
        else:
            print(f'{m1[i]}   {m2[i]}   {resultado[i]}')
            
def palindromo(sol):
    sol= sol.replace(" ","")
    sol2= sol[::-1]
    print( f"La cadena invertida es:  {sol2}")
    if sol==sol2:
        print(f"\nLa palabra SI es palíndromo")
    else:
        print("\nLa palabra NO es palíndromo")
        
def grafica():
    t.width(3)
    t.tracer(10)
    t.bgcolor('black')
    h=0
    n=50
    for i in range(250):
        c= colorsys.hsv_to_rgb(h,1,0.8)
        h += 1/n
        t.pencolor(c)
        t.circle(i, 90)
        t.forward(i)
        t.right(270)
        t.circle(i,270)
        t.forward(i)
        t.right(180)        
    t.done()
    
def ip_y_nombre():
    hostname= s.gethostname()
    ip= s.gethostbyname(hostname)
    print(f'El nombre de éste equipo es: '+ hostname)
    print(f'La IP de éste equipo es:  '+ ip)
    
def exponente(x):
    y= int(input('A que potencia lo quieres elevar?: '))
    if x > 0:       
        resultado =(pow(x, y))
        print('\nResultado: ')
        s1= "{:,}".format(resultado)
        print(s1)      
    elif x <= 0:
        print ('Error')
        
def traducir_binarios_y_hexa(n):
    if n== 'binario':
        s= input('Escribe tu número binario: ')
        r= int(s, 2)
        print(f'Este binario equivale a: {r}')
    elif n== 'hexadecimal':
        s= input('Escribe tu número hexadecimal: ')
        r= int(s, 16)
        print(f'Este hexadecimal equivale a: {r}')
        
def traducir_entero_a_binario(n):
    r = bin(n)
    print(f'Equivale a: {r} en Binario')
       
def main():
    continuar= True           #para ser un menu ciclico
    while continuar:
        imprimir_menu()
        opcion= input('Selecciona una opción: ')
        
        try:
            opcion = int(opcion)
        except ValueError as error:
            opcion = -1
            print('Error...no ingreses texto')
            input('Presiona enter para continuar...')
              
        os.system('cls')
        if opcion== 1:
            area_del_circulo()
        elif opcion== 2:
            sqrt()
        elif opcion== 3:
            multiplicar_lista()
        elif opcion== 4:
            numero= int(input('Digite número: '))
            factorial(numero)          
        elif opcion== 5:
            num= int(input('Digita número del que partirá: '))
            cuenta_regresiva(num)
        elif opcion== 6: 
            num= int(input('Ingresa los digitos a sumar: '))
            sumar_digitos(num)
        elif opcion== 7:
            n= int(input('Digita el numero de matrices: '))
            suma_de_matrices(n)
        elif opcion== 8:
            sol= input("\nDigita una cadena: ").lower() 
            palindromo(sol)
        elif opcion== 9:
            grafica()
        elif opcion== 10:
            ip_y_nombre()
        elif opcion== 11:
            x= int(input('Ingresa un numero:  '))
            exponente(x)
        elif opcion== 12:
            n= input('Traducir a binario o hexadecimal?:  ').lower()
            traducir_binarios_y_hexa(n)  
        elif opcion== 13:
            n= int(input('Ingresa el número entero que quieres traducir: '))
            traducir_entero_a_binario(n)
        elif opcion== salir:
            print('Hasta pronto...')
            continuar= False 
        else:
            print('Opción no válida..!')
        input('\nPresiona enter para continuar...')

if __name__=='__main__':      #la selectiva simple para continuar el programa
    main()

