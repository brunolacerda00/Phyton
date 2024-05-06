import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
soma = nota1 + nota2

media = soma / 2

print("\n ===RESULTADOS=== \n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média: {media}")

if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")