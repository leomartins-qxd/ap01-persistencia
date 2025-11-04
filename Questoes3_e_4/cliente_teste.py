import httpx

BASE_URL = "http://127.0.0.1:8000"

def adicionar_aluno(nome: str, nota: float):
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome":nome,"nota":nota}
    )
    print(resp.json())
    return resp


def listar_alunos():
    resp = httpx.get(
        f"{BASE_URL}/alunos"
    )
    print(resp.json())

def obter_nota(nome: str):
    resp = httpx.get(
        f"{BASE_URL}/alunos/{nome}"
    )
    print(resp.json())

aluno_teste = {
    'nome': 'Mariana',
    'nota': 1.5
}

#print(aluno_teste.get('nota'))
obter_nota('Mariana')
adicionar_aluno(aluno_teste.get('nome'), aluno_teste.get('nota'))
listar_alunos()
adicionar_aluno(aluno_teste.get('nome'), 9.5)
obter_nota('Mariana')
