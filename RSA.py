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
        return False
    else:
        return x % m
    

def esprimo(n):
   if (n <= 1 or n % 1 > 0):
      return False
   for i in range(2, n//2):
      if (n % i == 0 or n<=1):
         return False
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
        while True:
            p = int(input("Ingrese el numero primo p mayor a 1: "))
            if(esprimo(p)):
                break
        
        while True:
            q = int(input("Ingrese el numero primo q mayor a 1: "))
            if(esprimo(q)):
                break        
        
        n = p*q
        print ("n es igual a: " + str(n))
        
        fi = (p-1)*(q-1)
        print ("fi es igual a: " + str(fi) + "\n")
        
        while True:
            e = int(input("Ingrese el numero primo e mayor a 1, menor a fi y que tenga inverso modular con fi: "))
            if(modinv(e,fi) != False):
                if(esprimo(e) and e<fi): 
                    break
            
        d= modinv(e,fi)
        print("el exponente privado d es: " + str(d)+"\n")
        
        print("Las claves generadas son:")
        print("La clave publica es: (" + str(e) + "," + str(n)+")")
        print("La clave privada es: (" + str(d) + "," + str(n)+")")
        

    
