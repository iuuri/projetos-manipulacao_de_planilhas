import openpyxl

workbook = openpyxl.Workbook()
workbook.create_sheet('funcionarios')
sheet_funcionarios = workbook['funcionarios']
sheet_funcionarios.append(['nome', 'cargo', 'salário'])
continuar = 's'

while continuar == 's':
    nome = input('Nome: ')
    cargo = input('Cargo: ')
    salario = input('Salário: ')
    sheet_funcionarios.append([nome, cargo, salario])
    continuar = input('Adcionar mais um funcionario? (s/n)')

workbook.save('Funcionarios.xlsx')
