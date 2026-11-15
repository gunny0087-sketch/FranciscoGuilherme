import random
nomes = []
while True:
    nome = input("Digite o nome do comprador (ou 'E' para finalizar): ")
    if nome.upper() == "E":
        break
    nomes.append(nome)
ganhador = random.choice(nomes)
print("O ganhador é:", ganhador)
