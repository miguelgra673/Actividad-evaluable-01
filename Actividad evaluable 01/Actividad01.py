# Prepara con un ejemplo donde explicas cómo hacer en Python 3:
# ● Clonar una lista.
# ○ ¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”?
# ● Agregar un elemento a una lista.
# Quitar un elemento a una lista.
# ● Crear una lista nueva con los 4 últimos elementos de una lista.
# ● Convertir las palabras de una cadena (separadas por espacio) a una lista.
# ● Comentarios con una línea.
# ● Comentarios multilínea.

original_lista = [1, 2, 3, 4, 5]
shallow_copia = original_lista.copy() 
deep_copia = original_lista.copy()[:]  

print("Original:", original_lista)
print("Shallow Copy:", shallow_copia)
print("Deep Copy:", deep_copia)
