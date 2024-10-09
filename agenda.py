#!usr/bin/python3

AGENDA = {}
'''
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
'''
def mostrar_contatos():
    if AGENDA :
        for contato in AGENDA:
            buscar_contato(contato)
            print("-----------------------------------------")
    else :
        print(">>>>>>> Agenda Vazia")


def buscar_contato(contato) :
    try:
        print("nome ", contato)
        print("Telefone",AGENDA[contato]["telefone"])
        print("email", AGENDA[contato]["email"])
        print("endereço", AGENDA[contato]["endereco"])
        print("-----------------------------------------")
    except KeyError:
        print('>>>> Contato inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)   

def ler_detalhes_contato() :
    telefone = input("Digite o telefone do Contato")
    email = input("Digite o email do Contato")
    endereco = input("Digite o endereço do Contato")
    return telefone,email,endereco
    

def incluir_editar_contato(contato,telefone,email,endereco):    
    AGENDA[contato] = {
        "telefone" : telefone, 
        "email" : email, 
        "endereco" : endereco
        }
    salvar()
    print("-------------------------------------------")
    print("CONTATO {} INCLUÍDO/EDITADO COM SUCESSO> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(contato))
    print("-------------------------------------------")
    
def excluir_contato(contato):
    try :
        print("-------------------------------------------")
        AGENDA.pop(contato) #o .pop é um método pronto do python que exclui um item e um objeto
        salvar()
        print("Contato excluído {} com sucesso".format(contato))
        print("-------------------------------------------")
    except KeyError:
        print('>>>> Contato inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        
def exportar_contatos(nome_do_arquivo):
    try :        
            with open(nome_do_arquivo,"w") as arquivo:
                for contato in AGENDA:
                    telefone=AGENDA[contato]["telefone"]
                    email=AGENDA[contato]["email"]
                    endereco=AGENDA[contato]["endereco"]
                    arquivo.write("{},{},{},{} \n".format(contato, telefone, email, endereco))
            print("arquivo exportado com sucesso!!!!!!!!!!!!")      
    except Exception as error:
        print("algum erro ocorreu")
        print(error)
        
        
def importar_contatos(nome_do_arquivo):
    try :
        with open(nome_do_arquivo, "r") as arquivo:
            linhas=arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                
                incluir_editar_contato(nome,telefone, email, endereco)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)
        
def salvar():
    exportar_contatos("database.csv")
    
    
def carregar():
    try :
        with open("database.csv", "r") as arquivo:
            linhas=arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
              
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                
                AGENDA[nome] = {
                "telefone" : telefone, 
                "email" : email, 
                "endereco" : endereco
                }
        print(">>>>Database carregado com sucesso")
        print(">>>> {} contatos carregados com sucesso".format(len(AGENDA)))
    except Exception as error :
        print(error)
        print("algum erro inesperado ocorreu")
    except FileNotFoundError :
        print("arquivo não encontrado")
                
                
        

def imprimir_menu ():
    print("-------------------------------------------")
    print("1-Mostrar todos os contatos da agenda")
    print("2-Buscar contatos")
    print("3-Incluir Contatos")
    print("4-Editar Contatos")
    print("5-Excluir Contatos")
    print("6-Exportar contatos CSV")
    print("7-Importar contatos CSV")
    print("0- Fechar Agenda")
    print("-------------------------------------------")


#INÍCIO DO PROGRAMA

carregar()

while True :
    imprimir_menu()

    Opcao = input("escolha uma Opção: ")

    print(Opcao)


    if Opcao == "1" :
        mostrar_contatos()
    elif Opcao =="2" :
        contato = input("Digite o nome do contato")
        buscar_contato(contato)
    elif Opcao == "3":
        contato = input("Digite o nome do Contato")
        try :
            AGENDA[contato]
            print(">>>>>> Contato já existente")
        except KeyError: 
            telefone,email,endereco = ler_detalhes_contato()  
            incluir_editar_contato(contato,telefone,email, endereco)
    elif Opcao == "4":
        contato = input("Digite o nome do Contato")
        try :
            AGENDA[contato]
            print(">>>>>> Editando Contato ", contato)
            telefone,email,endereco = ler_detalhes_contato()  
            incluir_editar_contato(contato,telefone,email, endereco)
        except:
            print(">>>>>>>>>>>>contato não existe")   
                
    elif Opcao == "5" : 
        contato = input("Digite o nome do contato")
        excluir_contato(contato)
    elif Opcao == "6":
        nome_do_arquivo = input("digite o nome do arquivo a ser exportado: ")
        exportar_contatos(nome_do_arquivo)
    elif Opcao == "7":
        nome_do_arquivo = input("digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_do_arquivo)
    elif Opcao == "0" : 
        print(">>>>>>>>Fim/fechando do programa!!!!!!!!")
        break
    else :
        print(">>>>>>>>>>>>>>DIGITE O COMANDO CORRETO!!!!!!!, OPÇÃO INVALIDA!!!")