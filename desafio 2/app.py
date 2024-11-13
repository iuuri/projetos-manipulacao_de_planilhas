import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('vagas')
sheet_vagas = workbook['vagas']
sheet_vagas.append(['Empresa', 'Vaga', 'Data da Aplicação', 'Retorno Extra'])
continuar = 's'

while continuar == 's':
    empresa = input('Empresa: ')
    vaga = input('Vaga: ')
    data_aplicacao = input('Data da aplicação: ')
    retorno_extra = input('Retorno extra: ')
    sheet_vagas.append([empresa, vaga, data_aplicacao, retorno_extra])

    continuar = input('Deseja adicionar mais alguma vaga? (s/n)')

workbook.save('Acompanhamento de Vagas.xlsx')