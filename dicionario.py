#!/usr/bin/python3

dicionario ={"tijolo" :  "objeto para montar estruturas como uma muros",   
             "constituição": "Lei máxima de um país",
             "guilherm" : 19,
             "maria" : 17,
             "João" : 21
             }


#print(dicionario["João"], dicionario["tijolo"])

for item_do_dicionario in dicionario.values() :
    print(item_do_dicionario)


for dicionario_percorrendo_valores_sem_usarOValues in dicionario :
    print(dicionario[dicionario_percorrendo_valores_sem_usarOValues])