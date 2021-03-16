'''
******************************************************************************************
Autor: Gabriel Cordeiro Moraes
Componente Curricular: Algoritmos I
Concluido em: 14/10/2011
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''

# Entrada de Dados
informacao_total = []
def Cadastro(informacao_total):
    informacao_de_cadatro = {}

    nome = input('Nome completo da pessoa vacinada\n>>>')
    teste_nome = nome.isdigit()
    while teste_nome == True:
        print('O nome não pode ser somente números.')
        nome = input('Nome completo da pessoa vacinada\n>>>')
        teste_nome = nome.isdigit()

    cpf = input('CPF da pessoa vacinada (somente números)\n>>>') #lembrar de dizer pq ficou strg
    teste_cpf = cpf.isdigit()
    tamanho_cpf = len(cpf)
    while teste_cpf is False or tamanho_cpf != 11:
        print('O CPF deve conter 11 digitos numericos.')
        cpf = input('>>>')
        teste_cpf = cpf.isdigit()
        tamanho_cpf = len(cpf)
    cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12]
    
    sexo = str(input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>'))
    teste_sexo = sexo.isdigit()

    while teste_sexo is False:
        print('Escolha uma opção válida.')
        sexo = input('>>>')
        teste_sexo = sexo.isdigit()

    sexo = int(sexo)
    while sexo < 1 or sexo > 2:
        print('Escolha uma das opções válidas.')
        sexo = input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>')
        sexo = int(sexo)
         
    if sexo == 1:
        sexo = 'Masculino'
    else:
        sexo = 'Feminino'
    
    print('Digite o número correspondente ao grupo prioritário da pessoa vacinada.')
    print('[1] Trabalhadores da saúde\n[2] Idosos acima de 75 anos\n[3] Idosos ILPI acima de 60 anos')
    print('[4] Pessoas acamadas\n[5] Deficiente institucionalizados\n[6] Indigenas aldeados')
    print('[7] Povos de comunidades tradicionais (quilombolas) e ribeirinhas\n[8] Idosos de 60 a 74 anos')
    print('[9] Comorbidades\n[10] Pessoas em situação de rua\n[11] Forças de segurança e salvamento')
    print('[12] Trabalhadores da educação\n[13] Pessoas com deficiência permanentemente severa')
    print('[14] Caminhoneiros\n[15] Trabalhadores do Transporte Coletivo Rodoviário e Metroferroviário de passageiros')
    print('[16] Trabalhadores de Transporte Aéreo\n[17] Trabalhadores portuários')
    print('[18] População Privada de Liberdade')
    
    grupoPrioritario = input('[19] Funcionários do sistema de Privação de Liberdade\n>>>')
    teste_grupoPrioritario = grupoPrioritario.isdigit()

    while teste_grupoPrioritario is False:
        print('Escolha uma opção válida.')
        grupoPrioritario = input('>>>')
        teste_grupoPrioritario = grupoPrioritario.isdigit()
    
    grupoPrioritario = int(grupoPrioritario)
    while 1 > grupoPrioritario > 19:
        print('Escolha uma opção válida.')
        grupoPrioritario('>>>')
    
    if grupoPrioritario == 1:
        grupoPrioritario = 'Trabalhadores da saúde'

    elif grupoPrioritario == 2:
        grupoPrioritario = 'Idosos > 75 anos'
    
    elif grupoPrioritario == 3:
        grupoPrioritario = 'Idosos ILPI > 60 anos'

    elif grupoPrioritario == 4:
        grupoPrioritario = 'Pessoas acamadas'
    
    elif grupoPrioritario == 5:
        grupoPrioritario = 'Deficiente institucionalizados'
    
    elif grupoPrioritario == 6:
        grupoPrioritario = 'Indigenas aldeados'
    
    elif grupoPrioritario == 7:
        grupoPrioritario = 'Povos de comunidades tradicionais (quilombolas) e ribeirinhas'

    elif grupoPrioritario == 8:
        grupoPrioritario = 'Idosos de 60 a 74 anos'

    elif grupoPrioritario == 9:
        grupoPrioritario = 'Comorbidades'

    elif grupoPrioritario == 10:
        grupoPrioritario = 'Pessoas em situação de rua'

    elif grupoPrioritario == 11:
        grupoPrioritario = 'Forças de segurança e salvamento'

    elif grupoPrioritario == 12:
        grupoPrioritario = 'Trabalhadores da educação'
    
    elif grupoPrioritario == 13:
        grupoPrioritario = 'Pessoas com deficiência permanentemente severa'

    elif grupoPrioritario == 14:
        grupoPrioritario = 'Caminhoneiros'

    elif grupoPrioritario == 15:
        grupoPrioritario = 'Trabalhadores do Transporte Coletivo Rodoviário e Metroferroviário de passageiros'

    elif grupoPrioritario == 16:
        grupoPrioritario = 'Trabalhadores de Transporte Aéreo'

    elif grupoPrioritario == 17:
        grupoPrioritario = 'Trabalhadores portuários'

    elif grupoPrioritario == 18:
        grupoPrioritario = ' População Privada de Liberdade'

    elif grupoPrioritario == 19:
        grupoPrioritario = 'Funcionários do sistema de Privação de Liberdade'
    
    local = input('Digite o local de vacinação\n>>>')

    data = input('Data de vacinação (ddmmaaaa)\n>>>')
    teste_data = data.isdigit()
    while teste_data is False:
        print('A data deve conter somente números.')
        data = input('>>>')
        teste_data = data.isdigit()
    data = data[0:2] + '/' + data[2:4] + '/' + data[4:8]

    horario = input('Horário de vacinação (hhmm)\n>>>')
    teste_horario = horario.isdigit()

    if teste_horario is False:
        while teste_horario is False:
            print('A horario deve conter somente números.')
            horario = input('>>>')
            teste_horario = horario.isdigit()
        
    else:
        horario = int(horario)
        hora = horario // 100
        minuto = horario % 100

        while 0 > hora or hora > 23:
            print('Digite uma hora válida.')
            horario = input('>>>')
            horario = int(horario)
            hora = horario // 100
            minuto = horario % 100
        
        while 0 > minuto or minuto > 59:
            print('Digite um horário válido.')
            horario = input('>>>')
            horario = int(horario)
            hora = horario // 100
            minuto = horario % 100
        
        if 6 < hora < 12:
            periodo = 'Manha'
        
        elif 12 < hora < 18:
            periodo = 'Tarde'
        
        elif 18 < hora < 24:
            periodo = 'Noite'
        
        else:
            periodo = 'Madrugada'
            
        horario = str(hora) + ':' + str(minuto)
    

    fabricante = input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>')
    teste_fabricante = fabricante.isdigit()
    while teste_fabricante is False:
        print('Escolha uma opção válida.')
        fabricante = input('>>>')
        teste_fabricante = fabricante.isdigit()

    fabricante = int(fabricante)

    while fabricante < 1 or fabricante > 2:
        print('Escolha uma das opções válidas.')
        fabricante = input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>')
        fabricante = int(fabricante)
            
    if fabricante == 1:
        fabricante = 'Coronavac'
    else:
        fabricante = 'Astrazeneca'

    lote = input('Lote da Vacina\n>>>')

    dose = input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>')
    teste_dose = dose.isdigit()
    while teste_dose is False:
        print('Escolha uma opção válida.')
        dose = input('>>>')
        teste_dose = dose.isdigit()

    dose = int(dose)

    while dose < 1 or dose > 2:
        print('Escolha uma das opções válidas.')
        dose = input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>')
        dose = int(dose)
            
    if dose == 1:
        dose = 'Primeira'
    else:
        dose = 'Segunda'

    salvar = input('Digite [1] para salvar a informações ou [2] para começar novamente.\n>>>')
    teste_salvar = salvar.isdigit()
    while teste_salvar is False:
        print('Escolha uma opção válida.')
        salvar = input('>>>')
        teste_salvar = dose.isdigit()
    
    salvar = int(salvar)
    if salvar != 1:
        exit()
    else:
        informacao_de_cadatro['nome'] = nome
        informacao_de_cadatro['cpf'] = cpf
        informacao_de_cadatro['sexo'] = sexo
        informacao_de_cadatro['grupo_prioritario'] = grupoPrioritario
        informacao_de_cadatro['local'] = local
        informacao_de_cadatro['data'] = data
        informacao_de_cadatro['horario'] = horario
        informacao_de_cadatro['periodo'] = periodo
        informacao_de_cadatro['fabricante'] = fabricante
        informacao_de_cadatro['lote'] = lote
        informacao_de_cadatro['dose'] = dose
    
    informacao_total.append(informacao_de_cadatro)


#Saída de Dados
def Relatorio(informacao_total):
    if not informacao_total:
        print('Não existe pessoas cadastradas!!!')
    else:
        quantidadeVacinados = 0
        primeiraDose = 0
        segundaDose = 0
        coronavac = 0
        astrazeneca = 0
        quantidadeIdosos = 0
        vacinadosManha = 0
        vacinadosTarde = 0
        quantidadeMasculino = 0
        quantidadefeminino = 0
        
        for pessoa_vacinada in informacao_total:
            quantidadeVacinados += 1
            informacao = pessoa_vacinada.values()
            for dado in informacao:

                if dado == 'Primeira':
                    primeiraDose +=1
                
                if dado == 'Segunda':
                    segundaDose += 1
        
        print('%d pessoas foram vacinadas e %d doses foram aplicadas' %(quantidadeVacinados, primeiraDose))
        print('%d pessoas receberam a 1ª dose e %d pessoas receberam a segunda dose' %(primeiraDose, segundaDose))
        
        for pessoa_vacinada in informacao_total:
            informacao = pessoa_vacinada.values()
            for dado in informacao:
        
                if dado == 'Coronavac':
                    coronavac += 1
                    porcentagemCoronavac = (coronavac*100) / quantidadeVacinados
                    
                elif dado == 'Astrazeneca':
                    astrazeneca += 1
                    porcentagemAstrazeneca = (astrazeneca*100) / quantidadeVacinados
        
        print('%.2f das pessoas receberam a vacina Coronavac e %.2f receberam Astrazeneca' %(porcentagemCoronavac, porcentagemAstrazeneca))
        
        for pessoa_vacinada in informacao_total:
            informacao = pessoa_vacinada.values()
            for dado in informacao:
        
                if dado == 'Idosos':
                    quantidadeIdosos +=1
                    porcentagemIdosos = (quantidadeIdosos*100) / quantidadeVacinados
        
        print('%.2f dos vacinados são idosos' %porcentagemIdosos) 
        
        for pessoa_vacinada in informacao_total:
            informacao = pessoa_vacinada.values()
            for dado in informacao:

                if dado == 'Manha':
                    vacinadosManha += 1
                    porcentagemManha = (vacinadosManha*100) / quantidadeVacinados
                
                elif dado == 'Tarde':
                    vacinadosTarde += 1
                    porcentagemTarde = (vacinadosTarde*100) / quantidadeVacinados

        print('%.2f das vacinas foram aplicadas pela manhã e %.2f foram aplicadas pela tarde' %(porcentagemManha, porcentagemTarde))

        for pessoa_vacinada in informacao_total:
            informacao = pessoa_vacinada.values()
            for dado in informacao:

                if dado == 'Masculino':
                    quantidadeMasculino += 1
                    porcentagemMasculino = (quantidadeMasculino*100) / quantidadeVacinados
                
                elif dado == 'feminino':
                    quantidadefeminino += 1
                    porcentagemFeminino = (quantidadefeminino*100) / quantidadeVacinados
        
        print('%2.f dos vacinados são do sexo Masculino e %.2f são do sexo feminino') %(porcentagemMasculino, porcentagemFeminino)

#Menu do programa
def Linhas(tam = 84):
    return('_')*tam

def Menu():
    print(Linhas())
    print('\nBem vindo ao cadastro de vacinados contra a COVID-19!!!')
    print(Linhas())
    
    def Opcoes():
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
        
        return int(opcaoMenu)
    
    while Opcoes() == 1:
        print(Linhas())
        Cadastro(informacao_total)
        print(Linhas())
        Opcoes()
        print(Linhas())
    
    while Opcoes() == 2:
        print(Linhas())
        Relatorio(informacao_total)
        print(Linhas())
        Opcoes()
        print(Linhas())

     
Menu()