nome = input ("Digite o seu nome: ")
idade = int (input("Digite a sua idade: "))
print (nome)

if idade > 17:
    print ("Voce pode entrar na festa")
else:
    print ("Voce nao pode entrar na festa")

with open ("base-dados.csv", "a") as arquivo:
    arquivo.write (f"Seja bem vindo {nome} .\n")
