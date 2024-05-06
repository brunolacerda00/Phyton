import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar.")
elif idade < 18:
    print("Voto opcional.")
elif idade < 65:
    print("Voto obrigatório.")
else:
    print("Não obrigatório.")