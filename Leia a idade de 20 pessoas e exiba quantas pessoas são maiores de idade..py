maiores_de_idade = 0

for i in range(20):
    idade = int (input(f"Digite a idade da {i+1} pessoa: "))
    if idade >= 18:
        maiores_de_idade += 1

        print("O numero de pessoas maior de idade e",maiores_de_idade )
