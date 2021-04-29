#11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#o	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#o	salários até R$ 280,00 (incluindo) : aumento de 20%
#o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o	o salário antes do reajuste;
#o	o percentual de aumento aplicado;
#o	o valor do aumento;
#o	o novo salário, após o aumento.



sal = int(input("Digite seu salario: "))
print("salario antes do reajuste: ", sal)

if sal < 280:
    reajuste = sal*0.20
    sal = sal + reajuste
    print("Valor do aumento : ", reajuste)

elif sal >= 280 and sal <= 700:
    reajuste = sal * 0.15
    sal = sal + reajuste
    print("Valor do aumento : ", reajuste)

elif sal >= 700 and sal <= 1500:
    reajuste = sal * 0.10
    sal = sal + reajuste
    print("Valor do aumento : ", reajuste)

elif sal > 1500:
    reajuste = sal * 0.05
    sal = sal + reajuste
    print("Valor do aumento : ", reajuste)


print ("Novo Salario: ",sal)
