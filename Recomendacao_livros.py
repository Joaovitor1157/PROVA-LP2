livro = []

with open('livros_avaliacao.txt', 'r', encoding='utf-8') as livros:
    for linha in livros:
        linha = linha.strip("\n")
        linha = linha.split(", ")
        livro.append(linha)
for i in range(len(livro)): 
    if livro [i] [3]== "nao leu":
        livro [i] [3] = 0
print(livro)