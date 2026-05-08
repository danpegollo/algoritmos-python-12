n1 = 3
n2 = 2
resultado = 1
while n1 <= 99 and n2 <= 50:
    div = n1/n2
    resultado = div + resultado
    n1 = n1 + 2
    n2 = n2 + 1
print(n1, n2)
print(f"{resultado:.2f}")