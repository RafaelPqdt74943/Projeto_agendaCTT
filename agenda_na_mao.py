#!/usr/bin/python3

AGENDA = {
 "Guilherme": {"tel":"99999-3265",
               "email":"gui@solyd.com.br",
               "endereco":"rua tal nr 1"},
  "Maria": {"tel":"99999-2020",
               "email":"Maria@solyd.com.br",
               "endereco":"rua tal nr 1"},
 "João" : {"tel":"99999-1212",
               "email":"João@solyd.com.br",
               "endereco":"rua tal nr 1"}   
}

AGENDA["João"]["email"] = "joãomudouemail@solyd.com.br"

AGENDA["lucas"] = {"tel":"5555-265",
               "email":"Lucas@solyd.com.br",
               "endereco":"rua tal nr 1"}  


print(AGENDA["João"])

print(AGENDA["Guilherme"]["email"])

print(AGENDA["lucas"])

for contato in AGENDA :
    print(contato)
    
