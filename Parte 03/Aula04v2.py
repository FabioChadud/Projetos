candidatos = []

while True:
    print(f"\nCadastro de Candidato:")
    nome = input("Nome: ")
    portugues = float(input("Nota em Português: "))
    conhecimento_gerais = float(input("Nota em Conhecimentos Gerais: "))
    matematica = float(input("Nota em Matemática: "))

    candidatos.append({
        "nome": nome,
        "portugues": portugues,
        "conhecimento_gerais": conhecimento_gerais,
        "matematica": matematica
    })

    continuar = input("\nDeseja cadastrar outro candidato? (S/N): ").strip().upper()
    if continuar != 'S':
        break


aprovados = []
media_45_e_conhecimento_6 = 0
aprovados_matematica_5 = 0
quantidade_aprovados = 0
soma_notas_portugues = 0

for candidato in candidatos:
    media = (candidato["portugues"] + candidato["conhecimento_gerais"] + candidato["matematica"]) / 3

    if media > 4.0 and candidato["portugues"] >= 2.0 and candidato["conhecimento_gerais"] >= 2.0 and candidato["matematica"] >= 2.0:
        quantidade_aprovados += 1
        aprovados.append({
            "nome": candidato["nome"],
            "portugues": candidato["portugues"],
            "conhecimento_gerais": candidato["conhecimento_gerais"],
            "matematica": candidato["matematica"],
            "media": media
        })

    if media == 4.5 and candidato["conhecimento_gerais"] > 6.0:
        media_45_e_conhecimento_6 += 1

    if media > 4.0 and candidato["matematica"] > 5.0:
        aprovados_matematica_5 += 1

    soma_notas_portugues += candidato["portugues"]

media_portugues = soma_notas_portugues / len(candidatos)

print("\nResultados:")
print(f"Quantidade de candidatos aprovados: {quantidade_aprovados}")
print(f"Quantidade de candidatos com média 4.5 e nota de Conhecimentos Gerais maior que 6.0: {media_45_e_conhecimento_6}")
print(f"Quantidade de candidatos aprovados com nota maior que 5.0 em Matemática: {aprovados_matematica_5}")
print(f"Média das notas em Português: {media_portugues:.2f}")
print("\nLista de pessoas aprovadas:")
for aprovado in aprovados:
    print(f"Nome: {aprovado['nome']}, Português: {aprovado['portugues']}, Conhecimentos Gerais: {aprovado['conhecimento_gerais']}, Matemática: {aprovado['matematica']}, Média: {aprovado['media']:.2f}")