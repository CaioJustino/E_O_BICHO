import PySimpleGUI as sg
from classes import *

# Criando o Banco de Dados

bd = BancoDeDados()

# Tema

sg.theme('Default')

# Páginas - Layout

headings = ['CPF','Nome', 'Idade', 'Sexo', 'Telefone', 'Email']

x = {'112323871263': 'ONG2',
     '213213412421': 'ONG1'}
     
def pag_inicial():
    layout = [
        [sg.Text('É O BICHO', text_color='blue')],
        [sg.Text('\nDeseja acessar:\n')],
        [sg.Button('Pessoa', size=(10, 1)),sg.Button('Animal', size=(10, 1)),sg.Button('ONG', size=(10, 1))]
        ]

    return sg.Window('Tela Inicial', layout, size=(400,150), element_justification='c', finalize=True)

# Cadastro - Pessoa

def pag_pessoa():
    layout = [
             [sg.Table(values=[v for k, v in x.items()], headings=headings, num_rows=5)],
             [sg.Text('\n')],
             [sg.Button('Cadastrar', size=(10, 1), key='-CDSTP-'),sg.Button('Remover', size=(10, 1)), sg.Button('Buscar', size=(10, 1)), sg.Button('Voltar', size=(10, 1))]
             ]

    return sg.Window('Tela Pessoa', layout, size=(500,200), element_justification='c', finalize=True)

def cdst_pessoa():
    layout = [
        [sg.Text('Nome:', size=10), sg.InputText(size=100, key='-NOMEAD-')],
        [sg.Text('Idade:', size=10), sg.InputText(size=100, key='-IDADEAD-')],
        [sg.Text('Sexo:', size=10), sg.InputText(size=100, key='-SEXOAD-')],
        [sg.Text('CPF:', size=10), sg.InputText(size=100, key='-CPF-')],
        [sg.Text('Telefone:',size=10), sg.InputText(size=100, key='-FONEAD-')],
        [sg.Text('Email:',size=10), sg.InputText(size=100, key='-EMAILAD-')],
        [sg.Text('Endereço', text_color='blue')],
        [sg.Text('Rua:', size=10), sg.InputText(size=100, key='-RUAAD-')],
        [sg.Text('Número:', size=10), sg.InputText(size=100, key='-NUMEROAD-')],
        [sg.Text('Bairro:', size=10), sg.InputText(size=100, key='-BAIRROAD-')],
        [sg.Text('Cidade:', size=10), sg.InputText(size=100, key='-CIDADEAD-')],
        [sg.Text('Deseja ser voluntário?'), sg.Checkbox('Sim', default=True), sg.Checkbox('Não')],
        [sg.Text('\n')],
        [sg.Submit('Enviar', key='-CDP-'), sg.Cancel('Cancelar')]
    ]
    return sg.Window('Cadastro Pessoa', layout, size=(400,400), finalize=True)

# Cadastro - Animal

def pag_animal():
    layout = [
             [sg.Table(values=[v for k, v in x.items()], headings=headings, num_rows=5)], # LEMBRAR DE ARRUMAR A TABELAA
             [sg.Text('\n')],
             [sg.Button('Cadastrar', size=(10, 1), key='-CDSTA-'),sg.Button('Remover', size=(10, 1)), sg.Button('Buscar', size=(10, 1)), sg.Button('Voltar', size=(10, 1))]
             ]

    return sg.Window('Tela Animal', layout, size=(500,200), element_justification='c', finalize=True)

def cdst_animal():
    layout = [
        [sg.Text('Nome:', size=10), sg.InputText(size=100, key='-NOMEA-')],
        [sg.Text('Idade:', size=10), sg.InputText(size=100, key='-IDADEA-')],
        [sg.Text('Sexo:', size=10), sg.InputText(size=100, key='-SEXOA-')],
        [sg.Text('Peso:', size=10), sg.InputText(size=100, key='-PESO-')],
        [sg.Text('Espécie:',size=10), sg.InputText(size=100, key='-ESPECIE-')],
        [sg.Text('Raça:',size=10), sg.InputText(size=100, key='-RAÇA-')],
        [sg.Text('\n')],
        [sg.Submit('Enviar', key='-CDA-'), sg.Cancel('Cancelar')]
    ]
    return sg.Window('Cadastro Animal', layout, size=(400,250), finalize=True)

# Cadastro - ONG

def pag_ong():
    layout = [
             [sg.Table(values=[v for k, v in x.items()], headings=headings, num_rows=5)], # LEMBRAR DE ARRUMAR A TABELAA
             [sg.Text('\n')],
             [sg.Button('Cadastrar', size=(10, 1), key='-CDSTONG-'),sg.Button('Remover', size=(10, 1)), sg.Button('Buscar', size=(10, 1)), sg.Button('Voltar', size=(10, 1))]
             ]

    return sg.Window('Tela ONG', layout, size=(500,200), element_justification='c', finalize=True)

def cdst_ong():
    layout = [
        [sg.Text('Nome:', size=10), sg.InputText(size=100, key='-NOMEONG-')],
        [sg.Text('Telefone:',size=10), sg.InputText(size=100, key='-FONEONG-')],
        [sg.Text('Email:',size=10), sg.InputText(size=100, key='-EMAILONG-')],
        [sg.Text('Endereço', text_color='blue')],
        [sg.Text('Rua:', size=10), sg.InputText(size=100, key='-RUAONG-')],
        [sg.Text('Número:', size=10), sg.InputText(size=100, key='-NUMEROONG-')],
        [sg.Text('Bairro:', size=10), sg.InputText(size=100, key='-BAIRROONG-')],
        [sg.Text('Cidade:', size=10), sg.InputText(size=100, key='-CIDADEONG-')],
        [sg.Text('\n')],
        [sg.Submit('Enviar', key='-CDONG-'), sg.Cancel('Cancelar')]
    ]
    return sg.Window('Cadastro ONG', layout, size=(400,300), finalize=True)

# Abrir Páginas

tela_inicial = pag_inicial()
tela_pessoa = pag_pessoa()
tela_pessoa.hide()
tela_cdst_p = cdst_pessoa()
tela_cdst_p.hide()

tela_animal = pag_animal()
tela_animal.hide()
tela_cdst_animal = cdst_animal()
tela_cdst_animal.hide()

tela_ong = pag_ong()
tela_ong.hide()
tela_cdst_ong = cdst_ong()
tela_cdst_ong.hide()


while True:
    window, event, values = sg.read_all_windows()
    print(event, values)
    
    if event == sg.WIN_CLOSED or event is None:
        break

    if event == 'Cancelar':
        tela_cdst_p.hide()
        tela_cdst_ong.hide()
        tela_cdst_animal.hide()
        tela_inicial.un_hide()
    
    if event == 'Voltar':
        tela_pessoa.hide()
        tela_ong.hide()
        tela_animal.hide()
        tela_inicial.un_hide()

    # Pessoa (Interface)

    if event == 'Pessoa':
        tela_inicial.hide()
        tela_pessoa.un_hide()

    if event == '-CDSTP-':
        tela_pessoa.hide()
        tela_cdst_p.un_hide()

    if event == '-CDP-':
        tela_cdst_p.hide()
        tela_pessoa.un_hide()
        sg.popup('Cadastro concluído com sucesso!')
    
    # Animal (Interface)

    if event == 'Animal':
        tela_inicial.hide()
        tela_animal.un_hide()

    if event == '-CDSTA-':
        tela_animal.hide()
        tela_cdst_animal.un_hide()

    if event == '-CDA-':
        tela_cdst_animal.hide()
        tela_animal.un_hide()
        sg.popup('Cadastro concluído com sucesso!')
    
    # ONG (Interface)

    if event == 'ONG':
        tela_inicial.hide()
        tela_ong.un_hide()

    if event == '-CDSTONG-':
        tela_ong.hide()
        tela_cdst_ong.un_hide()

    if event == '-CDONG-':
        tela_cdst_ong.hide()
        tela_ong.un_hide()
        sg.popup('Cadastro concluído com sucesso!')


    