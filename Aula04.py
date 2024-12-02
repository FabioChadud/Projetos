# # Truques com Python
# Numero = 0
# Numero = 5

# # Avançar em casa a frebte com Int
# Numero+=1
# Numero = Numero+1

# #Avanço utilizando outra variavel
# Avancar = 3
# Numero = Numero+Avancar
# VariavelNova = Numero+Avancar

# # Pega uma parte da String 
# String = "AlunoeAluna"
# String[:4] # Vai gerar a string do final do texto
# String[4:] # Vai gerar a String do inicio do texto
# String[1:6] # Vai gerar a string do período demarcado

# #conversão de string para Lista
# listaDeNomes = "luana;Raphael;Natalia;Lucas"
# listaDeNomes = listaDeNomes.split(";")
# print(listaDeNomes[1])

# # for[] X WHILE X FOR I IN RANGE
# # O WHILE PODE DAR PROBLEMA POR CAUSA DA LOOP INFINITO
# # FOR VOCÊ FAZ QUANDO SE TEM ITENS QUE NÃO TEM A QUANTIDADE! EX: APLICAR DESCONTO EM UM CARINHO DE COMPRAS!
# # NO WHILE TEM QUE TER UMA VARIAVEL (X<10 --> x+=1 --> X<10), PARA FAZER UMA VARREDURA SEM UMA CONDIÇÕA FIXA DE PARADA.

# # CRIE UM LAÇO QUE EXECUTE 10 VEZES E SENORE EXECUTAR MULTIPLIQUE A VARIAVEL DE "taxa" por 1.2

# taxa = 0.2
# for T in range(0,10):
#     print("Executou"+str(T))
#     taxa = taxa*1.2
# print(taxa)

# Crie um laço de repetição em lista de int chamada valores e some cada um dos valores por 4

# valores = [2,5,6,7,8]
# soma = 0
# for i in valores:
#     print(i+4)
#     soma=soma+i+4
# print(soma)

# Crie um laço de repetição que faça 8 repetições e a cada repetição adicione +2 na variavel "Escala" e a cada interação adicionar o valor modificando na lista "ValorsEscala"

Escala = 2
ValoresEscala = []
# # fazendo com in rage:
# for i in range (8):
#     Escala += 2
#     ValoresEscala.append(Escala)
# print(ValoresEscala)

# # fazendo com While:
# contador=0
# while contador<8:
#     Escala += 2
#     ValoresEscala.append(Escala)
#     contador+=1
# print(ValoresEscala)

# fazendo com o for:

for v in [None] * 8:
    print([5] * 8)
    Escala += 2
    ValoresEscala.append(Escala)
print(ValoresEscala)
    
