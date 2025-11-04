from bs4 import BeautifulSoup

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("tbody")
rows = table.find_all('tr')

pontos_jogador1 = 0

for row in rows:
    tds = row.find_all("td")
    jogadas_rodada = []
    for td in tds:
        jogadas_rodada.append(td.get_text())
    
    if len(jogadas_rodada)>0:
        if jogadas_rodada[0] == 'pedra' and jogadas_rodada[1] == 'tesoura':
            pontos_jogador1 += 1
        if jogadas_rodada[0] == 'papel' and jogadas_rodada[1] == 'pedra':
            pontos_jogador1 += 1
        if jogadas_rodada[0] == 'tesoura' and jogadas_rodada[1] == 'papel':
            pontos_jogador1 += 1

        #print(jogadas_rodada)


print(f"Número de vitórias do Jogador 1: {pontos_jogador1}")
