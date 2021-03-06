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

    if sexo == 2:
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
    
    grupo_priotario = input('[19] Funcionários do sistema de Privação de Liberdade\n\n>>>')

    if grupo_priotario == 1:
        grupo_priotario = 'Trabalhadores da saúde'

    elif grupo_priotario == 2:
        grupo_priotario = 'Idoso > 75 anos'
    
    elif grupo_priotario == 3:
        grupo_priotario = 'Idosos ILPI > 60 anos'

    elif grupo_priotario == 4:
        grupo_priotario = 'Pessoas acamadas'
    
    elif grupo_priotario == 5:
        grupo_priotario = 'Deficiente institucionalizados'
    
    elif grupo_priotario == 6:
        grupo_priotario = 'Indigenas aldeados'
    
    elif grupo_priotario == 7:
        grupo_priotario = 'Povos de comunidades tradicionais (quilombolas) e ribeirinhas'

    elif grupo_priotario == 8:
        grupo_priotario = 'Idosos de 60 a 74 anos'

    elif grupo_priotario == 9:
        grupo_priotario = 'Comorbidades'

    elif grupo_priotario == 10:
        grupo_priotario = 'Pessoas em situação de rua'

    elif grupo_priotario == 11:
        grupo_priotario = 'Forças de segurança e salvamento'

    elif grupo_priotario == 12:
        grupo_priotario = 'Trabalhadores da educação'
    
    elif grupo_priotario == 13:
        grupo_priotario = 'Pessoas com deficiência permanentemente severa'

    elif grupo_priotario == 14:
        grupo_priotario = 'Caminhoneiros'

    elif grupo_priotario == 15:
        grupo_priotario = 'Trabalhadores do Transporte Coletivo Rodoviário e Metroferroviário de passageiros'

    elif grupo_priotario == 16:
        grupo_priotario = 'Trabalhadores de Transporte Aéreo'

    elif grupo_priotario == 17:
        grupo_priotario = 'Trabalhadores portuários'

    elif grupo_priotario == 18:
        grupo_priotario = ' População Privada de Liberdade'

    elif grupo_priotario == 19:
        grupo_priotario = 'Funcionários do sistema de Privação de Liberdade'
    
    else:
        print('Escolha uma das opções válidas.')
    
    local = input('Digite o local de vacinação\n>>>')
    data = input('Data de vacinação\n>>>')
    hora = input('Horário de vacinação\n>>>')
    fabricante = int(input('Digite [1] se a vacina que foi aplicada é Coronavac ou [2] se foi a Astrazeneca\n>>>'))
    lote = input('Lote da Vacina\n>>>')
    dose = int(input('Digite [1] se a dose aplicada foi a PRIMEIRA ou [2] se foi a SEGUNDA dose\n>>>'))

Cadastro()
