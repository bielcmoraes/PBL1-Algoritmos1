def Linhas(tam = 84):
    return('_')*tam

def Opcoes():
    print(Linhas())
    print('\nBem vindo ao cadastro de vacinados contra a COVID-19!!!')
    print(Linhas())
    
    print('Digite [1] para realizar um cadastro')
    print('Digite [2] para visualizar o relatorio')
    opcaoMenu = input('Digite [3] para sair\n>>>')
    testeOpcaoMenu = opcaoMenu.isdigit()
    print(Linhas())

    while opcaoMenu.isdigit() == False or len(opcaoMenu) >3:
        print(Linhas())
        print('Escolha uma opcao valida.')
        print('Digite [1] para realizar um cadastro')
        print('Digite [2] para visualizar o relatorio')
        opcaoMenu = input('Digite [3] para sair\n>>>')
        print(Linhas())
    
    if int(opcaoMenu) == 1:
        print(Linhas())
        import Cadastro
    print(Linhas())


        






Opcoes()