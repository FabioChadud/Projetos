# def RepetirECalcular(VezesRepetição, ValorInicial, ValorIncremento, Opção='+'):
#     for i in range(VezesRepetição):
#         if Opção == '+':
#             ValorInicial= ValorInicial+ValorIncremento
#         else:
#             ValorInicial = ValorInicial-ValorIncremento
#     return ValorInicial

# print(RepetirECalcular(4,0,1))

# def MaiorValor(a,b):
#     if a > b:
#         return a
#     if b > a:
#         return b
#     else:
#         return 'Números iguais'

# print(MaiorValor(6,6)) 

def calc(a,b,c,opção="+"):
    if opção =='+':
        total = a+b+c
    else:
        total = a*b*c
    return total

print(calc(8,9,7,'*'))

d = "Vai"
e = "fazer"
f = "sol"

def frase(d,e,f,g=0):
    if g == 0:
        return str(d+" "+e+" "+f)
print(frase(d,e,f))





