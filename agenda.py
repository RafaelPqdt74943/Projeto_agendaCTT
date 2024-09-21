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
    

def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone" : telefone, 
        "email" : email, 
        "endereco" : endereco
        }

  
  
mostrar_contatos()   

incluir_contato( "Rafael", "983212344", "sgtrafael@gmail.com", "rua cap machado" )

mostrar_contatos()   

print("CONTATO INCLUÍDO COM SUCESSO> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") # o comando .fomart() serve para incluir uma variável no meio da string

#buscar_contato("guilherme")

