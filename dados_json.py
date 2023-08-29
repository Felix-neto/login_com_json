import json
banco_de_dados = {}

while True:
    op = input("(1)criar conta \n(2)login \n(3)excluir cadastro \n(4)exibir todos cadastros \n(5)sair:  ")
    if op == "1":
        usuario = input("Cadastre seu nome de usuario: ")   
        senha = input("Cadastre sua senha: ")
        banco_de_dados[usuario] = senha

        with open("dados.json","w") as dados:
            json.dump(banco_de_dados, dados)
            print("usuario cadastrado")

    elif op == "2":
        with open("dados.json","r") as dados:
            dad = json.load(dados)
        
        usu = input("Digite seu nome de usuario: ")
        if usu in dad:
            senha = input("Digite sua senha: ")
            if senha == dad[usu]:
                print("logado")
            else:
                print("senha incorreta")
        else:
            print("usuario não existe")

    elif op == "3":
        op2 = input("(1)deletar apenas um cadastro \n(2) deletar todos: ")
        if op2 == "1":
            with open("dados.json", "r") as dados:
                ler = json.load(dados)
                elemente = input("qual cadastro gostaria de deletar: ")
                
                if elemente in ler:
                    del ler[elemente]
                    with open("dados.json", "w") as dados:
                        json.dump(ler, dados)
                    print("cadastro deletado")
                else:
                    print("cadastro não existe")
        if op2 == "2":
            with open("dados.json", "w") as dados:
                json.dump({}, dados)
            print("todos cadastros foram deletados")


    elif op == "4":
        with open("dados.json", "r") as dados:
            try:
                dad = json.load(dados)
                if not dad:
                    print("sem dados")
                else:
                    print(dad)
            except Exception:
                print("ERRO")


    elif op == "5":
        print("adeus")
        break