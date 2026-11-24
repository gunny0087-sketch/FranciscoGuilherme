
palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6

print("=" * 35)
print("       JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    if len(letras_descobertas) == len(palavra):
        break

    palpite = input("Digite uma letra: ").upper()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas uma letra")
        continue

    if palpite in letras_utilizadas:
        print("Essa letra ja foi utilizada")
        continue

    letras_utilizadas.append(palpite)

    if palpite in palavra:
        letras_descobertas.append(palpite)
        print("Voce acertou!")
    else:
        print("Voce errou!")
        erros += 1

print("\n" + "=" * 35)

if len(letras_descobertas) == len(palavra):
    print("Pabens! você ganhou")
else:
    print("Você perdeu!")

print(f"A palavra secreta era: {palavra}")

print("=" * 35)

