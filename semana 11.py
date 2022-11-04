#1.-Solo permitir números enteros
while True:
    try:
      edad = int(input("Escribe tu edad: "))
      break
    except ValueError:
        print("¡Debes ingresar un número!")
if edad >= 18:
    print("Eres un adulto.")
else:
  print("Aún no eres un adulto.")
  
#2.-Solicitar edad definiendo funciones
def solicitar_edad():
    try:
      return int(input("Escribe tu edad: "))
    except ValueError:
      return solicitar_edad()
    
    edad = solicitar_edad()
    
#3.-Dividir entre 0 y enviar error
a=10
b=1

try:
    c = b / a
    print (c)
except (IOError,ZeroDivisionError) as x:
    print ("Error ",x)
else:
  print ("no error")
  
print ("Fin de programa")
  
#4.-Error dividiendo entre 0
try:
  print (5/0)
except (TypeError,ZeroDivisionError) as e:
    
  print ("Error ", e)
else:
  print (5/0)
  
print ("Fin de programa")

#5.-Creando una excepción de error
a=5
b=3

if a<b:
   raise Exception('El número restado no puede ser menor que el número restado')
   #return 0
else:
  print (a-b)
  
#6.-Error mostrando mensaje de sistema
import math
import sys

try:
  result = math.factorial(2.4)
except:
  print("Error inesperado.",sys.exc_info()[0])
else:
  print("El factorial es", result)
  
#7.-Introducir edad, hacer operación y limpiar programa con Finally
while True:
    try:
      x = int(input("Introduce un múmero entero: "))
    except ValueError:
        print("No es dato válido. Intenta de nuevo...")
    else:
      print("Divide entre 50 /", x,"el resultado es :", 50/x)
    finally:
      print("Finalización de un programa.")