#Universidad Del Valle De Guatemala
#Matematica Discreta
#Gabriel Quiroz 19255, Jose Pablo Ponce 19092
#25/11/2020
#Cifrado RSA

#Se importa la libreria random 
import random

#
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
#Funcion para encontrar el modulo inverso
def modinv(a, m):
    g, x, y = egcd(a, m)
    while g != 1:
        return False
    else:
        return x % m  

#Funcion para desencriptar
def desencriptar(cifrado,llavePriv):
    try:
        llave,n = llavePriv
        mensaje = [chr(pow(char,llave,n)) for char in cifrado]
        return "".join(mensaje)
    except TypeError as e:
        print(e)
#Funcion para encriptar
def encriptar(mensaje,llavePubli):
    llave,n = llavePubli
    cifrado = [pow(ord(char),llave,n) for char in mensaje]
    return cifrado

#Funcion para determinar si el numero random que se obtiene es primo
def esprimo(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

#Funcion para asignar un numero primo random a p y q
def PrimoRandom():
    while(1):
        primo = random.randint(0,10000000000)
        if esprimo(primo):
            return primo
        
#Declaracion de algunas variables iniciales que sirven como banderas
d=False
mensaje = ""
bandera = True

#Inicio del menu
while bandera:
    print("Ingrese el numero de opcion que desea elegir: ")
    print("1. Generar claves públicas y privada ")
    print("2. Encriptar ")
    print("3. Desencriptar ")
    print("4. Salir ")
    opcion = int(input())
    print(" ")

    if(opcion == 1):
        
        #Asignacion de un numero primo a p y q
        p = PrimoRandom()
        q = PrimoRandom()
                   
        #Calculo de n
        n = p*q
        print ("n es igual a: " + str(n))
        
        #Calculo de fi
        fi = (p-1)*(q-1)
        print ("fi es igual a: " + str(fi) + "\n")
        
        #Asignacion de un valor valido a e y d
        while(d == False):
            e = random.randint(1, fi)
            print ("e es igual a: " + str(e) + "\n")
            d= modinv(e,fi)
            
        print("el exponente privado d es: " + str(d)+"\n")
        
        print("Generando claves...")
        print("Las claves generadas son:")
        print("La clave publica es: (" + str(e) + "," + str(n)+")")
        print("La clave privada es: (" + str(d) + "," + str(n)+")")
        
    if(opcion == 2):
        #Validacion para que antes de encriptar genere las llaves
        if(p == 0):
            print("Debe generar las llaves para poder encriptar")
        else:
            #Se pide el mensaje y se encripta el mismo
            mensaje = input("Ingrese el mensaje que desea encriptar:\n")  
            print("Encriptando...")
            mensajeencriptado =encriptar(mensaje, (e,n) )
            print(mensajeencriptado)
    if(opcion == 3):
        #Validacion para que antes de desencroptar encripte un mensaje
        if(mensaje == ""):
            print("Debe encriptar un mensaje para poder desencriptar")
        else:
            #Se desencripta el mensaje
             print("Desencriptando...")
             mensajedesencriptado = desencriptar(mensajeencriptado, (d,n))
             print(mensajedesencriptado)
            
    if(opcion == 4):
        print("Saliendo...")
        print("Vuelva pronto")
        bandera = False
            
