# Pon un ejemplo de cómo pasar varios parámetros desde consola a un programa Python 3.
# Pon un ejemplo de cómo realizar “sobrecarga de funciones” (funciones que pueden recibir varios
# números de parámetros), incluyendo el caso de que el número de parámetros no sea definido.

import sys

# Obtener los argumentos de la línea de comandos
argumentos = sys.argv[1:]

# Imprimir los argumentos
print("Argumentos recibidos:", argumentos)


#Sobrecarga
def suma(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        resultado = args[0]
        for num in args[1:]:
            resultado += num
        return resultado

print(suma())      
print(suma(5))        
print(suma(2, 3, 4))   
print(suma(1, 2, 3, 4)) 


