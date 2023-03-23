
# PROGRAMA PARA HALLAR EL CAPITAL DEL INTERES COMPUESTO DEL 5% MENSUAL

print ("----------------------------------------------------------------------------")
print ("----PROGRAMA PARA HALLAR EL CAPITAL DEL INTERES COMPUESTO DEL 5% MENSUAL----")
print ("----------------------------------------------------------------------------")

# input

capital = float(input("Ingrese el capital: "))
duplicado = capital + capital
meses = 0
interes =0

# processing

meses = 0 # contador de meses

while capital < duplicado:
    interes = capital*0.05 # interés compuesto mensual del 5%
    capital = capital + interes
    meses = meses + 1

    
print("EL CAPITAL SE DUPLICA EN:" + str(meses) + " MESES ")






