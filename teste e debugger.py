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
