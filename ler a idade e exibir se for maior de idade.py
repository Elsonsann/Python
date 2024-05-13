# ler a idade e exibir se for maior de idade

idade_med = 18

pessoa_maior = 0

for i in range(20):

    idade = int(input(f"Digite a idade da pessoa{i+1}: "))
    if idade >= idade_med:
        pessoa_maior += 1

        print(f"Numero de pessoas maior de idade: {pessoa_maior}")
