livro = []
new_txt = []
recomendar = []
with open('livros_avaliacao.txt', 'r', encoding='utf-8') as livros:
    for linha in livros:
        linha = linha.strip("\n")
        linha = linha.split(", ")
        livro.append(linha)

for i in range(len(livro)):
    if livro [i] [3] != "nao lido" and livro [i] [3] != "0":
        new_txt.append(livro [i])

for i in range(len(new_txt)):
    new_txt [i] [3] = float(new_txt [i] [3])

recomendacao = sorted([iten[3] for iten in new_txt] , reverse= True)

for i in range(len(recomendacao)):
    for o in range(len(recomendacao)):
        if new_txt [o] [3] == recomendacao [i]:
            new_txt [o] [3] = str(new_txt [o] [3])
            recomendar.append(new_txt [o])

with open("livros_recomendados.txt", "w") as f:
    for linha in recomendar:
        linha_str = ', '.join(map(str, linha))
        f.write(linha_str + "\n")