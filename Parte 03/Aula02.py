# print('O salário de {0} no mês de {1} foi R$ {2:.2f}'.format(nome, mes, salario).upper)        #UPPER --> LETRA GRANDE
# Nome = Maria
# mes = abril
# salario = 10500.50

# nome = "Maria"
# mes = "abril"
# salario = 10500.50

# print("O salário de Maria no mês de abril foi R$ 10500.50")
# texto_resultado = "O salário de {0} no mês de {1} foi R$ {2:.2f}".format(nome, mes, salario)
# print()
# print("O salário de {0} no mês de {1} foi R$ {2:.2f}".format(nome, mes, salario))
# print(texto_resultado)

# # imprimir cada caracter da string
# for caracter in texto_resultado:
#     print(caracter)

# # imprimir tamanho da string
# tamanho_string = len(texto_resultado)
# print("A string tem {0} caracter(es)".format(tamanho_string))

# EXERCÍCIO 03

valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

# EXERCÍCIO 04

numeros = []
for i in range(4):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\nNúmeros divisíveis por 2 e 3:")
for num in numeros:
    if num % 2 == 0 and num % 3 == 0:
        print(num)

# EXERCÍCIO 05

def calcular_imposto(ganhos):
    if ganhos <= 500.00:
        return 0.00  
    elif 500.01 <= ganhos <= 1500.00:
        return ganhos * 0.10  
    elif 1500.01 <= ganhos <= 2500.00:
        return ganhos * 0.15  
    else:
        return ganhos * 0.20  

ganhos = float(input("Digite o total de ganhos (em reais): R$ "))

imposto = calcular_imposto(ganhos)

print(f"O valor do imposto a ser pago é: R$ {imposto:.2f}")
