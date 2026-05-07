frase = str(input("Digite uma frase: ")).lower()
vogais = (
    frase.count("a") +
    frase.count("e") +
    frase.count("i") +
    frase.count("o")+
    frase.count("u")
)
espaco = frase.count(" ")

print(f"Vogais: {vogais}")
print(f"Espaços: {espaco}")

