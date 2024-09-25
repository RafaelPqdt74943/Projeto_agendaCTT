#!usr/bin/python3

AGENDA = {}

AGENDA ["guilherme"] = { "telefone" : "99999-7777",
                        "email" : "gui.123@gmail.com",
                        "endereco" : "av.123 -rj",

}

AGENDA ["Suzana"] = { "telefone" : "99999-8888",
                        "email" : "SUZU.321@gmail.com",
                        "endereco" : "av.456 -rj",

}

AGENDA ["Miguel"] = { "telefone" : "99999-7546",
                        "email" : "miguel.321@gmail.com",
                        "endereco" : "av.888 -rj",

}

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print("-----------------------------------------")



def buscar_contato(contato) :
    print("nome ", contato)
    print("Telefone",AGENDA[contato]["telefone"])
    print("email", AGENDA[contato]["email"])
    print("endereço", AGENDA[contato]["endereco"])
    print("-----------------------------------------")
    

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone" : telefone, 
        "email" : email, 
        "endereco" : endereco
        }
    print()
    print("CONTATO {} INCLUÍDO/EDITADO COM SUCESSO> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(contato))
    print()
    
def excluir_contato(contato):
    AGENDA.pop(contato) #o .pop é um método pronto do python que exclui um item e um objeto
    print("Contato excluído {} com sucesso".format(contato))
  

def imprimir_menu ():
    print("-------------------------------------------")
    print("1-Mostrar todos os contatos da agenda")
    print("2-Buscar contatos")
    print("3-Incluir Contatos")
    print("4-Editar Contatos")
    print("5-Excluir Contatos")
    print("0- Fechar Agenda")
    print("-------------------------------------------")


while True :
       
    imprimir_menu()

    Opcao = input("escolha uma Opção: ")

    print(Opcao)


    if Opcao == "1" :
        mostrar_contatos()
    elif Opcao =="2" :
        contato = input("Digite o nome do contato")
        buscar_contato(contato)
    elif Opcao == "3" or Opcao == "4" :
        contato = input("Digite o nome do Contato")
        telefone = input("Digite o telefone do Contato")
        email = input("Digite o email do Contato")
        endereco = input("Digite o endereço do Contato")
        incluir_editar_contato(contato, telefone, email, endereco)
        mostrar_contatos()
    elif Opcao == "5" : 
        contato = input("Digite o nome do contato")
        excluir_contato(contato)
        mostrar_contatos()
    elif Opcao == "0" : 
        print(">>>>>>>>Fim/fechando do programa!!!!!!!!")
        break
    else :
        print(">>>>>>>>>>>>>>DIGITE O COMANDO CORRETO!!!!!!!, OPÇÃO INVALIDA!!!")