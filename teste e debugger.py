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

print(dose)
