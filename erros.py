#erros em tempo de compilação
#erros em tempo de execução
#erros de lógica

while True :
    try:
        a = float(input("digite um número: "))
        b = float(input("digite o segundo número: "))

        print(a/b)
    except ZeroDivisionError as error :
        print("não pode ser feita a divisão por zero")
    except ValueError as error :
        print("informe valores em números e não em letras")
    except Exception as error :
        print("ocorreu algum erro")
        print(error)
   