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

informacao_cadastrada = {}
def Cadastro():

    nome = input('Nome completo da pessoa vacinada\n>>>')
    teste_nome = nome.isdigit()
    while teste_nome == True:
        print('O nome não pode ser somente números.')
        nome = input('Nome completo da pessoa vacinada\n>>>')
        teste_nome = nome.isdigit()

    cpf = input('CPF da pessoa vacinada (somente números)\n>>>') #lembrar de dizer pq ficou strg
    teste_cpf = cpf.isdigit()
    while teste_cpf is False:
        print('O CPF deve conter somente números.')
        cpf = input('>>>')
        teste_cpf = cpf.isdigit()
    cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12]
    
    sexo = str(input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>'))
    teste_sexo = sexo.isdigit()

    while teste_sexo is False:
        print('Escolha uma opção válida.')
        sexo = input('>>>')
        teste_sexo = sexo.isdigit()

    sexo = int(sexo)
    while sexo < 1 and sexo > 2:
        print('Escolha uma das opções válidas.')
        sexo = input('Digite [1] para sexo Masculino ou [2] para sexo Feminino\n>>>')
         
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
        grupoPrioritario = 'Idoso > 75 anos'
    
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
    data = input('Data de vacinação\n>>>')
    hora = input('Horário de vacinação\n>>>')
    fabricante = int(input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>'))
    lote = input('Lote da Vacina\n>>>')
    dose = int(input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>'))

Cadastro()
