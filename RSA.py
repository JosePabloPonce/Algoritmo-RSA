
#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def esprimo(a):
    
    if(number == 0 or number == 1 or number<1 ):
        return False
    
    else:
        for i in range(2,a):
            if num % i ==0:
                return False
            else:
                return True
        
        
p=0
q=0
n=0
fi=0
e=0
d=0
while True:
    print(p)
    print("Ingrese el numero de opcion que desea elegir: ")
    print("1. Generar claves públicas y privada ")
    print("2. Encriptar ")
    print("3. Desencriptar ")
    opcion = int(input())
    print(" ")

    if(opcion == 1):
        p = int(input("Ingrese el numero primo p mayor a 1: "))
        q = int(input("Ingrese el numero primo q mayor a 1: "))
        n = p*q
        
        print ("n es igual a: " + str(n))
        fi = (p-1)*(q-1)
        print ("fi es igual a: " + str(fi) + "\n")
        
        e = int(input("Ingrese el numero primo e mayor a 1 y menor a fi: "))
        d= modinv(e,fi)
        print("el exponente privado d es: " + str(d)+"\n")
        print("Las claves generadas son:")
        print("La clave publica es: (" + str(e) + "," + str(n)+")")
        print("La clave privada es: (" + str(d) + "," + str(n)+")")



    
