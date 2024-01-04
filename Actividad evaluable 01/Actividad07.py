# Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”.
# Crea un método imprimir, y además dos métodos que quieras.
# En segundo lugar, haz que el programa pida un número “n” por teclado y se creen “n” instancias de
# la clase, donde cada instancia:
# ● Cada "matricula" tendrá un número consecutivo desde 1 hasta "n".
# ● El “color” será para cada instancia un color aleatorio obtenido de este listado [“red”, “white”,
# “black”, “pink”, “blue”)
# Por último, el programa deberá imprimir los valores de las 10 primeras instancias. En caso de que
# "n" sea menor que 10, sólo imprimirá "n" instancias.

import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def metodo1(self):
        print("Este es el método 1")

    def metodo2(self):
        print("Este es el método 2")

n = int(input("Ingresa un número 'n': "))

cars = []
for i in range(1, n + 1):
    color_aleatorio = random.choice(["red", "white", "black", "pink", "blue"])
    car_instance = Car(i, color_aleatorio)
    cars.append(car_instance)

for car_instance in cars[:10]:
    car_instance.imprimir()
