#gph=ganho por hora;
gph=float(input("Quanto você ganha por hora?\n"))
#ht=horas trabalhadas;
ht=float(input("Quantas horas você trabalha ao mês?\n"))

imp=1.11
inss=1.08
sindicato=1.05
salariobruto=(gph*ht)
desc_imp=salariobruto*imp-salariobruto
desc_inss=salariobruto*inss-salariobruto
desc_sind=salariobruto*sindicato-salariobruto
salarioliquido=salariobruto-desc_imp-desc_inss-desc_sind

print("Seu salário bruto mensal é de %.2f"%salariobruto)
print("Você pagou R$%.2f em imposto"%desc_imp)
print("Você pagou R$%.2f em INSS"%desc_inss)
print("Você pagou R$%.2f para o sindicato"%desc_sind)

print("Seu salário líquido mensal é de %.2f"%salarioliquido)