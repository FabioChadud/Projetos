# crie um programa basico que tenha como objetivo
#Armazenar 2 valores que o usuario digitar.
# O primeiro valor deve ser o seu nome e o
# segundo a sua profisão.
#Após isso se o usuario digitou "estudante"
# programa deve perguntar em qual faculdade / escola
# este estudante estuda.
# No final do programa deve exibir a seguinte informação:
# O usuario {nome} é um {Profissao}
# e se ele for estudante deve mostrar a informação extra
# E estuda na instituição {faculdadeEcola}

# Extras!
# * Uso de função para a rotina funcionar
# * Conseguir fazer um loop para cadastrar varias pessoas

nome=[]
profissao=[]
ensino=[]
parada="S"

def registro (nome, profissao,ensino):
    print(profissao)
    if profissao != str("estudante"):
        return "O usuário "+nome+" "+"é um "+profissao
    if profissao == str("estudante"):
        return "O usuário "+nome+" "+" é um "+profissao+" "+" e estuda na instituição "+ensino

while parada == "S":
    nome.append(input("Qual o seu nome?  "))
    profissao.append(input("Qual a sua profissão?  "))
    if profissao[len(profissao)-1]=="estudante":
        ensino.append(input("Qual a sua faculdade?  "))
        print(registro(nome[len(nome)-1], profissao[len(profissao)-1], ensino[len(ensino)-1]))
    else:
        ensino.append(None)
        print(registro(nome[len(nome)-1], profissao[len(profissao)-1],""))
    parada=input("Você deseja Continuar? S/N     ")

Pessoas=[]
Perguntas = ["Qual é seu Nome?", "Qual a sua profissão?", "Qual a sua escola"]
def CadastroPessoa(NomePessoa, Profissao,Escola=None):
    Pessoas.append([NomePessoa, Profissao, Escola])

def Mensagens(NomePessoa, Profissao, Escola=0):
    if Profissao == "estudante":
        return f"A pessoa {NomePessoa} é um {Profissao} e estuda no {Escola} "
    else:
        return f"A pessoa{NomePessoa} é um {Profissao}"
    
while True:
    Dados = []
    for i in Perguntas:
        if len(Dados)-1 >= 1:
            if Dados[1] == "estudante":
                Dados.append(input(i))
                break
            else:
                Dados.append(None)
                break
        Dados.append(input(i))

    CadastroPessoa(Dados[0], Dados [1], Dados[2])
    Mensagens(Dados[0], Dados[1], Dados[2])



 