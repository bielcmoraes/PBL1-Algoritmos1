'''
******************************************************************************************
Autor: Gabriel Cordeiro Moraes
Componente Curricular: EXA854 - MI - Algoritmos
Concluido em: 20/03/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''

'''A função Cadatro coleta as informações necessarias do usuário, faz as validações necessárias
e armazena as informações em um dicionário. O dicionário é armazenado em uma lista no programa
principal para separar as informações de cada vacinado'''

informacao_total = [] # Lista que armazena os dicionários com as informacoes dos vacinados.
def Cadastro(informacao_total):
    informacao_de_cadatro = {} #Dicionario que armazena as informacoes do vacinado.

    dose = input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>')
    teste_dose = dose.isdigit() #Retorna True se a opção escolhida nao for um numero inteiro.

    while teste_dose is False: #Enquanto um numero não for digitado é solicitado que o usuario digite uma opção valida
        print('Escolha uma opção válida.')
        dose = input('>>>')
        teste_dose = dose.isdigit()

    dose = int(dose) #Converte o valor digitado pelo usuario em inteiro para ser utilizado nas estruturas condicionais

    while dose < 1 or dose > 2: #Verifica se o número digitado corresponde a uma das opções disponiveis
        print('Escolha uma das opções válidas.')
        dose = input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>')
        dose = int(dose)
            
    if dose == 1: #Verifica qual a dose de acordo com a escolha do usuario e armazena o resultado na variavel dose
        dose = 'Primeira'
    else:
        dose = 'Segunda'
    
    '''Se a dose aplicada for a primeira as demais informações serão coletadas e armazenadas nas respectivas variaveis'''
    if dose == 'Primeira':

        #Coleta o nome e garante que não tenha somente numeros
        nome = input('Nome completo da pessoa vacinada\n>>>')
        teste_nome = nome.isdigit()
        
        while teste_nome == True:
            print('O nome não pode ser somente números.')
            nome = input('Nome completo da pessoa vacinada\n>>>')
            teste_nome = nome.isdigit()

        #Coleta o CPF e garante que não contenha letras e tenha onze caracteres
        cpf = input('CPF da pessoa vacinada (somente números)\n>>>')
        teste_cpf = cpf.isdigit()
        tamanho_cpf = len(cpf)
        
        while teste_cpf is False or tamanho_cpf != 11:
            print('O CPF deve conter 11 digitos numericos.')
            cpf = input('>>>')
            teste_cpf = cpf.isdigit()
            tamanho_cpf = len(cpf)
        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12] #Coloca o CPF no formato "xxx.xxx.xxx-xx"
        
        #Coleta o sexo (Masculino ou Feminino) e garante que a opcao escolhida seja valida
        sexo = str(input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>'))
        teste_sexo = sexo.isdigit()

        while teste_sexo is False:
            print('Escolha uma opção válida.')
            sexo = input('>>>')
            teste_sexo = sexo.isdigit()

        sexo = int(sexo) #Converte a opcao escolhida para inteiro
        while sexo < 1 or sexo > 2:
            print('Escolha uma das opções válidas.')
            sexo = input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>')
            sexo = int(sexo)

        #Armazena a opcao escolhida na variavel correspondente   
        if sexo == 1:
            sexo = 'Masculino'
        else:
            sexo = 'Feminino'
        
        #Coleta o grupo prioritario e garante que a opcao escolhida seja valida
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
        
        local = input('Digite o local de vacinação\n>>>') #Coleta o local de vacinacao

        #Coleta a data e garante que tenha somente numeros
        data = input('Data de vacinação (ddmmaaaa)\n>>>')
        teste_data = data.isdigit()
        while teste_data is False:
            print('A data deve conter somente números.')
            data = input('>>>')
            teste_data = data.isdigit()
        data = data[0:2] + '/' + data[2:4] + '/' + data[4:8] #Armazena a data no formaro "dd/mm/aaaa"

        #Coleta o horario de vacinacao e garante que tenha somente numeros
        horario = input('Horário de vacinação (hhmm)\n>>>')
        teste_horario = horario.isdigit()

        if teste_horario is False:
            while teste_horario is False:
                print('A horario deve conter somente números.')
                horario = input('>>>')
                teste_horario = horario.isdigit()
            
        else:
            horario = int(horario)
            hora = horario // 100 #Separa a hora dos minutos
            minuto = horario % 100 #Separa os minutos da hora

            #Garante que a hora digitada não seja invalida
            while 0 > hora or hora > 23:
                print('Digite uma hora válida.')
                horario = input('>>>')
                horario = int(horario)
                hora = horario // 100
                minuto = horario % 100
            
            #Garante que os minutos digitados não seja invalido 
            while 0 > minuto or minuto > 59:
                print('Digite um horário válido.')
                horario = input('>>>')
                horario = int(horario)
                hora = horario // 100
                minuto = horario % 100
            
            #Armazena os periodos de acordo com a hora
            if 6 < hora < 12:
                periodo = 'Manha'
            
            elif 12 < hora < 18:
                periodo = 'Tarde'
            
            elif 18 < hora < 24:
                periodo = 'Noite'
            
            else:
                periodo = 'Madrugada'
                
            horario = str(hora) + ':' + str(minuto) #Armazena o horario no formato "hh:mm"

        #Coleta o fabricante e garante que a opcao escolhida e valida    
        fabricante = input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>')
        teste_fabricante = fabricante.isdigit()
        while teste_fabricante is False:
            print('Escolha uma opção válida.')
            fabricante = input('>>>')
            teste_fabricante = fabricante.isdigit()

        fabricante = int(fabricante) #Converte a opcao escolhida para inteiro

        while fabricante < 1 or fabricante > 2:
            print('Escolha uma das opções válidas.')
            fabricante = input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>')
            fabricante = int(fabricante)

        #Armazena a opcao escolhida na respectiva variavel        
        if fabricante == 1:
            fabricante = 'Coronavac'
        else:
            fabricante = 'Astrazeneca'

        lote = input('Lote da Vacina\n>>>') #Coleta o lote da vacina

        #Verifica se o usuario que armazenar as informacoes
        salvar = input('Digite [1] para salvar a informações ou [2] para começar novamente.\n>>>')
        teste_salvar = salvar.isdigit()
        while teste_salvar is False:
            print('Escolha uma opção válida.')
            salvar = input('>>>')
            teste_salvar = dose.isdigit()
        
        salvar = int(salvar) #Converte a opção escolhida para inteiro
        
        #Se o usuario não quiser armazenar as informacoes a funcao acaba
        if salvar != 1: 
            exit()
        
        #Se o usuario quiser armazenar as informacoes, as informacoes são armazenadas em um dicionario
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
        
        informacao_total.append(informacao_de_cadatro) #O dicionario é armazenado dentro de uma lista no programa principal
    
    #Se a dose aplicada for a segunda coleta a data, o horario e consequentente o periodo, fazendo as verificacoes necessarias
    else:
        
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
            
            if 6 <= hora <= 12:
                periodo = 'Manha'
            
            elif 12 < hora < 18:
                periodo = 'Tarde'
            
            elif 18 < hora < 24:
                periodo = 'Noite'
            
            else:
                periodo = 'Madrugada'
                
            horario = str(hora) + ':' + str(minuto)

        #Verifica se o usuario quer armazenar as informacoes correspondentes a segunda dose
        salvar = input('Digite [1] para salvar a informações ou [2] para começar novamente.\n>>>')
        teste_salvar = salvar.isdigit()
        while teste_salvar is False:
            print('Escolha uma opção válida.')
            salvar = input('>>>')
            teste_salvar = dose.isdigit()
        
        salvar = int(salvar)
        
        #Se o usuario não quiser armazenar as informacoes a funcao acaba
        if salvar != 1:
            exit()
        
        #Armazena as informacoes em um dicionario
        else:
            informacao_de_cadatro['data'] = data
            informacao_de_cadatro['horario'] = horario
            informacao_de_cadatro['periodo'] = periodo
            informacao_de_cadatro['dose'] = dose
        
        informacao_total.append(informacao_de_cadatro) #Armazena o dicionario dentro de uma lista no programa principal
    


'''A funcao Relatorio faz todos os calculos e processamentos necessarios para mostrar ao usuario as informacoes desejadas a respeito das informacoes coletadas.'''

def Relatorio(informacao_total):
    #Se a lista no programa principal estiver vazia informa que não existe pessoas cadastradas
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
        
        for pessoa_vacinada in informacao_total: #Percorre cada dicionario armazenado na lista
            informacao = pessoa_vacinada.values() #Gera uma lista contendo somente os valores do dicionario
            for dado in informacao: #Percorre cada valor contido na lista gerada na linha anterior

                #Verifica os valores e conta a quantidade de primeiras e segundas doses
                if dado == 'Primeira':
                    quantidadeVacinados += 1 #A quantidade de vacinados é a quantidade de primeiras doses aplicadas
                    primeiraDose +=1
                
                if dado == 'Segunda':
                    segundaDose += 1
        
        dosesAplicadas = primeiraDose + segundaDose #O total de doses aplicadas é a soma da quantidade de primeiras e segundas doses
        
        print('%d pessoas foram vacinadas e %d doses foram aplicadas' %(quantidadeVacinados, dosesAplicadas))
        print('%d pessoas receberam a 1ª dose e %d pessoas receberam a segunda dose' %(primeiraDose, segundaDose))

        if quantidadeVacinados !=0: # Verifica se a quantidade de vacinados é diferente de zero afim de evitar erros

            # Verifica o tipo da vacina e calcula a porcentagem de vacinas aplicadas para cada tipo
            for pessoa_vacinada in informacao_total:
                informacao = pessoa_vacinada.values()

                for dado in informacao:
            
                    if dado == 'Coronavac':
                        coronavac += 1
                
                    porcentagemCoronavac = (coronavac*100) / quantidadeVacinados
                        
                    if dado == 'Astrazeneca':
                        astrazeneca += 1
    
                    porcentagemAstrazeneca = (astrazeneca*100) / quantidadeVacinados
            
        
            print('%.2f %% das pessoas receberam a vacina Coronavac' %porcentagemCoronavac)
            print('%.2f  %% das pessoas receberam Astrazeneca' %porcentagemAstrazeneca)
            
            #Verifica a quantidade de idosos vacinados e calcula a porcentagem em relacao ao total de vacinados
            for pessoa_vacinada in informacao_total:
                informacao = pessoa_vacinada.values()
                
                for dado in informacao:
            
                    if dado == 'Idosos > 75 anos':
                        quantidadeIdosos += 1
                    
                    if dado == 'Idosos ILPI > 60 anos':
                        quantidadeIdosos += 1
                    
                    if dado == 'Idosos de 60 a 74 anos':
                        quantidadeIdosos += 1
                    
                    porcentagemIdosos = (quantidadeIdosos*100) / quantidadeVacinados
            
            print('%.2f %% dos vacinados são idosos' %porcentagemIdosos) 
            
            #Verifica quantas vacinas foram aplicadas pela manha e pela tarde. Calcula as respectivas porcentagens em relacao ao numero total de vacinados 
            for pessoa_vacinada in informacao_total:
                informacao = pessoa_vacinada.values()
                for dado in informacao:

                    if dado == 'Manha':
                        vacinadosManha += 1
                    
                    porcentagemManha = (vacinadosManha*100) / quantidadeVacinados
                    
                    if dado == 'Tarde':
                        vacinadosTarde += 1
                    
                    porcentagemTarde = (vacinadosTarde*100) / quantidadeVacinados

            print('%.2f %% das vacinas foram aplicadas pela manhã e %.2f %% foram aplicadas pela tarde' %(porcentagemManha, porcentagemTarde))

            #Verifica a quantidade de vacinados por sexo e calcula as rescpectivas porcentagens
            for pessoa_vacinada in informacao_total:
                informacao = pessoa_vacinada.values()
                for dado in informacao:

                    if dado == 'Masculino':
                        quantidadeMasculino += 1
                    
                    porcentagemMasculino = (quantidadeMasculino*100) / quantidadeVacinados
                    
                    if dado == 'Feminino':
                        quantidadefeminino += 1
                    
                    porcentagemFeminino = (quantidadefeminino*100) / quantidadeVacinados
        
        else:
            print('Não existem pessoas cadastradas')


'''A funcao Menu permite que o usuario escolha se deseja acessar a funcao Cadatro, a funcao relatorio ou se deseja finalizar o programa.'''

def Menu():

    print('Bem vindo ao programa de cadastro de vacinados contra o COVID-19.\n')

    while True: #Garante apos acessar a funcao Relatorio ou a funcao Cadastro o usuario retorne para as opcoes do menu

        print('Digite [1] para cadastrar uma nova pessoa.')
        print('Digite [2] para visualizar o relatorio.')
        print('Digite [3] para sair.')

        opcaoMenu = input('>>>')
        #Garante que o usuario vai digitar uma opcao válida
        teste_opcaoMenu = opcaoMenu.isdigit()
        while teste_opcaoMenu == False:

            print('Digite uma opcao valida.\n')
            
            print('Digite [1] para cadastrar uma nova pessoa.')
            print('Digite [2] para visualizar o relatorio.')
            print('Digite [3] para sair.')
            opcaoMenu = input('>>>')
            teste_opcaoMenu = opcaoMenu.isdigit()
        
        opcaoMenu = int(opcaoMenu) #Converte a opcao escolhida para inteiro
        
        #Se a opcao escolhida for 1, pula uma linha e acessa a funcao Cadastro
        if opcaoMenu == 1:
            print('\n')
            Cadastro(informacao_total)
        
        #Se a opcao escolhida for 2, pula uma linha e acessa a funcao Relatorio
        elif opcaoMenu == 2:
            print('\n')
            Relatorio(informacao_total)
        
        #Se a opcao escolhida for 3, finaliza o programa
        elif opcaoMenu == 3:
            quit()
               
Menu()