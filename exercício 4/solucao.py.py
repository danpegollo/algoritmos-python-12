quantidade_eleitores = int(input("Coloque a quantidade de eleitores: "))
#voto Antônio 1
#voto Breno 2 
#voto Carlos 3 
#voto Daniel 4
#nulo 5
# branco 6
votos_Antônio = 0  
votos_Breno = 0 
votos_Carlos = 0 
votos_Daniel = 0 
nulo = 0 
branco = 0

while quantidade_eleitores > 0:
    voto = int((input("Em quem você quer votar? Digite de 1 a 6: ")))
    if voto == 1:
        votos_Antônio += 1
    elif voto == 2:
        votos_Breno += 1
    elif voto == 3:
        votos_Carlos += 1
    elif voto == 4:
        votos_Daniel += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        print("Vote inválido, tente novamente")
        continue
        
    quantidade_eleitores -= 1

total = votos_Antônio + votos_Breno + votos_Carlos + votos_Daniel + nulo + branco
print(f"O total de votos para o Antônio foi de {votos_Antônio}, para o Breno foi de {votos_Breno}, para o Carlos foi de {votos_Carlos} e para o Daniel {votos_Daniel}") #a
print(f"O total de votos nulos é de {nulo}") #b
print(f"O total de votos brancos foi de {branco}") #c

if total > 0:
    percentual_nulos = (nulo/total) * 100
    print(f"O total de votos nulos sobre o total de votos foi de {percentual_nulos}")
    percentual_branco = (branco/total) * 100
    print(f"O total de votos em branco sobre o total de votos foi de {percentual_branco}")
else: 
    percentual_branco = 0
    percentual_nulos = 0
    print("Não há votos nulos")