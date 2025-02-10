# print('test')
# numero=4
# print('quadrado de',numero,'=',numero**2,sep='_')
# exemplo 01
# n1 = int(input('informe o primeiro número:  '))
# n2 = int(input('informe o segundo número:   '))
# n3 = int(input('informe o terceiro número:  '))
# n4 = int(input('informe o quarto número:  '))

#Exercício 01
# media = ((n1*1)+(n2*2)+(n3*3)+(n4*4))/(1+2+3+4)
# print('Média ponderada é ', media)

# Exercício 02
# dolar = float(input('Qual a contação do dolar:  '))
# quantidade = int(input('quatidade de dolares guardado:  '))
# valor = dolar*quantidade
# print('O valor no cofre é de ', valor)

valorcompra = float(input('Qual o valor da compra?  '))
parcela = valorcompra / 5
print('Sua parcela é de  ', parcela)

custo = float(input('Qual o preço de custo?  '))
percentual = float(input('Qual o percentual de lucro? '))
print('O valor do seu produto é ', (custo+(custo*(percentual/100))))