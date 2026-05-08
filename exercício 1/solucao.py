x = int(input("Coloque o valor de um número: "))
expoente = 25
divisor = 1
resultado = 0
while divisor <= 25:
    soma = (x ** expoente)/divisor
    if divisor %2 == 0:
        resultado = resultado - soma
    else: 
        resultado = resultado + soma
    expoente -= 1
    divisor += 1
print(resultado)