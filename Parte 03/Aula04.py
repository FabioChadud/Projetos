nome = ''
nportugues = 0
nmatematica = 0
nconhecgerais = 0
continua = True

dicCandidatos = {}  # {'nomeCandidato':[NP, NM, NCG]}
dicMedias = {}  # {'nomeCandidato': media}
listaAprovados = []
listaNotas = []
listaMedias = []

# Entrada de dados
while continua:
    nome = input('Informe o nome do candidato: ')
    nportugues = float(input(f'Informe a nota de Português do candidato {nome}: '))
    nmatematica = float(input(f'Informe a nota de Matemática do candidato {nome}: '))
    nconhecgerais = float(input(f'Informe a nota de Conhecimentos Gerais do candidato {nome}: '))
    
    listaNotas = [nportugues, nmatematica, nconhecgerais]  # Lista de notas reiniciada
    dicCandidatos[nome] = listaNotas
    
    pergunta_respondida = 'OK'
    while pergunta_respondida == 'OK':
        resposta = input("\nDeseja cadastrar novo candidato (S)IM ou (N)ÃO): ")
        if resposta.upper() == 'S' or resposta.upper() == 'N':
            if resposta.upper() == 'N':
                continua = False
            pergunta_respondida = 'NOK'  # Finaliza a repetição do while
        
        else:
            print("\nInforme na pergunta 'S' para 'SIM' ou 'N' para 'NÃO'.")
    
# Processamento

# Calcular médias
for chave in dicCandidatos.keys():
    notas_aluno = dicCandidatos[chave]
    media = sum(notas_aluno) / len(notas_aluno)
    dicMedias[chave] = media

print(dicMedias)

# Recuperar aprovados e candidatos com média > 4.5 e nota de CG > 6
qtdCandidatosMediaMaior45 = 0
for chave in dicCandidatos.keys():
    notas_aluno = dicCandidatos[chave]
    aprovado = True  # Inicializa como aprovado

    # Verifica se tem alguma das notas menor que 2
    if notas_aluno[0] < 2 or notas_aluno[1] < 2 or notas_aluno[2] < 2:
        aprovado = False
    
    # Verifica se ele foi aprovado
    if dicMedias[chave] > 4 and aprovado:
        listaAprovados.append(chave)

    # Candidatos com média > 4.5 e nota de CG > 6
    if dicMedias[chave] > 4.5 and notas_aluno[2] > 6:
        qtdCandidatosMediaMaior45 += 1

# Média da prova de português
somaNotas = sum([dicCandidatos[chave][0] for chave in dicCandidatos.keys()])
media = somaNotas / len(dicCandidatos)

# Quantidade de candidatos aprovados com nota de Matemática > 5
qtdCandidatosAprovadosMatematicaMaior5 = 0
for chave in dicCandidatos.keys():
    notas_aluno = dicCandidatos[chave]
    if dicMedias[chave] > 4 and notas_aluno[1] > 5:
        qtdCandidatosAprovadosMatematicaMaior5 += 1

# Exibindo resultados
for chave in dicCandidatos.keys():
    notas_aluno = dicCandidatos[chave]
    print(f"{chave} => Português: {notas_aluno[0]} / Matemática: {notas_aluno[1]} / Conhec. Gerais: {notas_aluno[2]}")

print(f"\nMédias dos Candidatos: {dicMedias}")
print(f"\nCandidatos Aprovados: {listaAprovados}")
print(f"A média da prova de Português foi {media:.2f}")        
print(f"Qtd Candidatos com média > 4.5 e nota Conhec. Gerais > 6: {qtdCandidatosMediaMaior45}")    
print(f"Qtd Candidatos aprovados com nota de Matemática > 5: {qtdCandidatosAprovadosMatematicaMaior5}")
