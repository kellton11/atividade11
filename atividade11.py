# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)
i = int(input("digite a idade:"))

if i <=12:
    print("criança")
elif i <=17:
    print("adolescente")
elif i <=59:
    print("adulto")
elif i >=60:
    print("idoso")