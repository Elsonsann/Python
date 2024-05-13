# Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.

nome_pessoa_nova = ""
idade_pessoa_nova = float('inf')

for i in range(10):
    nome = input(f"Digite o nome de uma pessoa{i+1}: ")
    idade = int(input(f"Digite a idade da pessoa{i+1}:"))

    if idade < idade_pessoa_nova:
        nome_pessoa_nova = nome
        idade_pessoa_nova = idade
