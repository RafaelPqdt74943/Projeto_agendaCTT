#erros em tempo de compilação
#erros em tempo de execução
#erros de lógica



def divisão(a, b) :
    try :
        print(a/b)
    except Exception as e:
        print("Divisão invalida")
        print(e)
        
        
divisão(20,0)