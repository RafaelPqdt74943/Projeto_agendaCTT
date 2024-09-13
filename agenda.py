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
        print("nome ", contato)
        print("Telefone",AGENDA[contato]["telefone"])
        print("email", AGENDA[contato]["email"])
        print("endereço", AGENDA[contato]["endereco"])
        print("-----------------------------------------")



mostrar_contatos()
