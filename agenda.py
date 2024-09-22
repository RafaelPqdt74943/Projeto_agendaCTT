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
    

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone" : telefone, 
        "email" : email, 
        "endereco" : endereco
        }
    print("CONTATO {} INCLUÍDO/EDITADO COM SUCESSO> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(contato))
  
  

incluir_editar_contato( "Rafael", "983212344", "sgtrafael@gmail.com", "rua cap machado" )
incluir_editar_contato( "Rafael", "99999-9999", "sgtrafael@gmail.com", "rua cap machado" )
incluir_editar_contato("josé","9999-6523", "", None)

mostrar_contatos()   