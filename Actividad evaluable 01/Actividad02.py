# En Python 3 los tipos simples se pasan por valor y los compuestos por referencia.
# Crea un ejemplo con 3 funciones que:
# ● Reciba 2 números y devuelva la suma.
# ● Reciba una lista y modifique esa misma lista (referencia) doblando los valores de todos los
# elementos. No debe devolver nada.
# ● Reciba una lista y devuelva una copia de la lista misma lista (referencia) doblando los valores
# de todos los elementos. La lista original no debe modificarse.


def suma_numeros(a, b):
    return a + b

def doblar_valores_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2

def doblar_valores_copia(lista):
    copia_lista = lista.copy()
    for i in range(len(copia_lista)):
        copia_lista[i] *= 2
    return copia_lista


num1 = 5
num2 = 7
resultado_suma = suma_numeros(num1, num2)
print("Suma de {} y {}: {}".format(num1, num2, resultado_suma))

mi_lista = [1, 2, 3, 4]
doblar_valores_lista(mi_lista)
print("Lista después de modificarla directamente:", mi_lista)

copia_doblada = doblar_valores_copia(mi_lista)
print("Lista original:", mi_lista)
print("Copia de la lista modificada:", copia_doblada)
