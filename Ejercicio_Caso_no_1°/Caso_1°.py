# Programa para allar la suma de los primeros N números naturales

print ("--------------------------------------------------------------")
print ("----PROGRAMA PARA HALLAR LA SUMA DE LOS PRIMEROS N NÚMEROS----")
print ("--------------------------------------------------------------")

# input

n = int(input("Digite el valor de N  : "))


# processing

suma = 0 
i = 1
while (i<=n):
    suma = suma + i
    i = i + 1
    
print("LA SUMA DE LOS PRIMEROS NÚMEROS NATURALES ES: ") 
print(suma)

