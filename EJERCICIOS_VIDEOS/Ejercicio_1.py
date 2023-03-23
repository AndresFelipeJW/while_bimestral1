import math

n = int(input("Digite un número positivo: "))

while n < 0:
    print("Error, el número debe ser positivo")
    n = int(input("Digite un número positivo: "))

print(f"\nLa raiz cuadrada es: {(math.sqrt(n)):.2f}")