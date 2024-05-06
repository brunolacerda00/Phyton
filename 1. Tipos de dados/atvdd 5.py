import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
numeroUm = int(input("Digite o primeiro número: "))
numeroDois = int(input("Digite o segundo número: "))
soma = numeroUm + numeroDois
multiplicacao = numeroUm * numeroDois
media = soma / 2

if numeroUm > numeroDois:
    maior = numeroUm
else: maior = numeroDois

if numeroUm < numeroDois:
    menor = numeroUm
else:
    menor = numeroDois    

print("\n ===RESULTADOS=== \n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeiro número: {numeroUm}")
print(f"Segunda número: {numeroDois}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Média: {media}")