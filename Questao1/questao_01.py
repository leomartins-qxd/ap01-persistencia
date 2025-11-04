maior_nota = 0
maior_aluno = ''
menor_nota = 10
menor_aluno = ''
contagem_alunos = 0
soma_notas = 0

with open("dados_alunos.txt","r") as file:
    linha = file.readline()
    #print(linha)
    while(linha):
        contagem_alunos += 1
        linhas_separadas = linha.strip().split('#')

        soma_notas += float(linhas_separadas[2])

        if(float(linhas_separadas[2])>float(maior_nota)):
            maior_nota = linhas_separadas[2]
            maior_aluno = linhas_separadas[0]

        if(float(linhas_separadas[2])<float(menor_nota)):
            menor_nota = linhas_separadas[2]
            menor_aluno = linhas_separadas[0]

        #print(type(float(linhas_separadas[2])))
        linha = file.readline()


if maior_aluno != '':
    media = soma_notas/contagem_alunos
    print(f"Média da turma: {round(media, 2)}")
    print(f"Maior nota: {maior_nota} ({maior_aluno})")
    print(f"Menor nota: {menor_nota} ({menor_aluno})")
else:
    print("Não há alunos")
