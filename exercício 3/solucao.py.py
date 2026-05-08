total_fun = int(input("Coloque a quantidade de funcionários: "))
contador_mulheres = 0
contador_homens = 0
soma_salario_homem = 0
contador_reajuste = 0

while total_fun > 0:
    nome = str(input("Coloque o nome do empregado: "))
    sexo = str(input("Coloque o sexo do empregado: ").upper())
    salario = float(input("Coloque o salário do funcionário: "))

    while sexo!= "M" and sexo!= "F":
        sexo = (input("O empregado apenas pode possuir sexo M ou F:").upper())
    while salario < 850:
        salario = float(input("O salário do funcionário não pode ser menor que 850"))

    if salario >= 3000:
        novo_salario = salario + (salario * 0.045)
    elif salario >= 2000:
        novo_salario = salario + (salario * 0.065)
        contador_reajuste += 1
    else:
        novo_salario = salario + (salario * 0.085)

    if sexo == "F":
        contador_mulheres += 1
    else:
        contador_homens += 1
        soma_salario_homem += novo_salario

    print(f"O nome do empregado é {nome}, seu salário foi de {salario} para {novo_salario}")#a
    total_fun -= 1

total = contador_homens + contador_mulheres
percentual = (contador_mulheres/total)*100

print(f"A quantidade de funcionários que receberam reajuste de 6,5% foi de {contador_reajuste}")#b
if contador_homens > 0:
    media_salario_homem = soma_salario_homem/contador_homens
    print(f"A média de salários ajustados dos empregados do sexo masculino foi de {media_salario_homem:.2f}")
else:
    print("Não há homens na empresa")
print(f"O percentual de empregados do sexo feminino entre o total de empregados foi de: {percentual:.2f}%")#d
