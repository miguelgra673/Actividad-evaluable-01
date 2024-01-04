# Lista de listas con tamaño y peso
listado = [
    [180, 70],
    [160, 60],
    [180, 65],
    [160, 55],
    [170, 68]
]

# Definir una función que sirva como key function
# La key function toma una sublista y devuelve una tupla (altura, peso)
# El peso se utiliza para ordenar por menor peso en caso de igualdad en la altura
def key_function(sublista):
    return (sublista[0], -sublista[1])

listado_ordenado = sorted(listado, key=key_function, reverse=True)

print("Listado original:", listado)
print("Listado ordenado:", listado_ordenado)
