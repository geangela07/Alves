def calcular_pagamento (qtd_horas,valor_hora):
    horas= float(qtd_horas)
    taxa= float(valor_hora)
    if horas <=40:
        salario= horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario

horaTrabalhada= input("Quantas você trabalha?")
valordahora= input("O valor da hora trabalhada")


salariorecebido= calcular_pagamento(horaTrabalhada,valordahora)
print("Seu salario é:",salariorecebido)