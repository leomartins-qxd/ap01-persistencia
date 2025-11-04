from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

contador_id = 4

alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Fulano", "Sicrano", "Beltrano"],
        "nota": [5.6, 9.2, 7.5]
    }
)

class Aluno(BaseModel):
    nome: str
    nota: float

@app.post("/alunos")
def adicionar_aluno(aluno: Aluno):
    global alunos_df, contador_id
    novo_aluno = {
        'id': contador_id,
        'nome': aluno.nome,
        'nota': aluno.nota
    }

    filtro_igual = alunos_df['nome'] == aluno.nome
    if not (alunos_df[filtro_igual].empty):
        
        alunos_df.loc[filtro_igual, 'nota'] = aluno.nota
        return 'Aluno já estava registrado, então sua nota foi atualizada.'
        
    else:
        alunos_df = alunos_df._append(novo_aluno, ignore_index=True)
        contador_id += 1
        return 'Aluno criado com sucesso.'

@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient = "records")

@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    checar_registro = alunos_df[alunos_df['nome'] == nome]
    if checar_registro.empty:
        return 'O aluno não foi registrado'
    
    nota = checar_registro.to_dict(orient='records')[0].get('nota')
    return f'A nota de {nome} é {nota}'

aluno_teste = {
    'nome': 'Mariana',
    'nota': 10
}

