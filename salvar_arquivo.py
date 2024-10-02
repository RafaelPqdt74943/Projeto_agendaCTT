try :
    with open("nomes.txt", "a") as arquivo :
        arquivo.write("Rafael MS \n")
except Exception as error :
    print("algum erro ocorreu")
    print(error)


'''
'r' - abre para ler
'w' - abre para escrever / arquivo é sobrescrito
'a' - abre para escrever / novo conteúdo é adicionado ao final do arquivo
'+'
'b'
'''