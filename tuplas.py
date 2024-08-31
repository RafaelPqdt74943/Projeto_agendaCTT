#!usr/bin/python3
 
tupla_cores = ("amarelo", "azul", "roxo") # na duplas não podemos adicionar elm e nem remover, vantagem disso pe fazer uma lista imutável por exemplo
lista_cores = ["rosa, lilaz, verde"]


lista_cores.append("red")

lista_cores[1] = "purple"

print(tupla_cores)
print(lista_cores)

for cor in tupla_cores :
    print(cor)
