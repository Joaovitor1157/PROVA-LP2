livro = []
new_txt = []
with open('livros_recomendados.txt', 'r', encoding='utf-8') as livros:
    for linha in livros:
        linha = linha.strip("\n")
        linha = linha.split(", ")
        livro.append(linha)

print("Ranking de recomendação: ")

for i in range(len(livro)):
    print("    %i° - %s de %s com %s de avaliação." %(i+1, livro [i] [1], livro [i] [2], livro [i] [3]))