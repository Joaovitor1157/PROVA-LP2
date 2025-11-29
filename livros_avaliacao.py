livro = []
new_txt = []
with open('livros.txt', 'r', encoding='utf-8') as livros:
    for linha in livros:
        linha = linha.strip("\n")
        linha = linha.split(", ")
        livro.append(linha)

for i in range(len(livro)):
    while True:
        status = input("Qual seu status(Lendo, Lido, Na Fila) referente ao livro %s, escrito por %s em %s? " %(livro [i] [1], livro [i] [2], livro [i] [0])).lower()
        if status == "lendo" or status == "lido":
            while True:
                avaliacao = input("Qual nota(0 - 10) você da ao livro %s? " %livro [i] [1]).replace("," , ".")
                if float(avaliacao) > 10.0 or float(avaliacao) < 0:
                    print("Nota fora dos parametros, Por favor tente novamente.")
                else:
                    break
            break
        elif status == "na fila":
            avaliacao = "nao lido"
            break
        else:
            print("Resposta não condiz com a pergunta, Por favor tente novamente.")
    juncao = ["%s, %s, %s, %s, %s " %(livro [i] [0], livro [i] [1], livro [i] [2], avaliacao, status)]
    new_txt.append(juncao)
with open("livros_avaliacao.txt", "w") as f:
    for linha in new_txt:
        linha_str = ''.join(map(str, linha))
        f.write(linha_str + "\n")