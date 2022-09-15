

# Esse projeto consiste em uma tela na qual o usuário pode consultar a alta e a baixa da moeda(Dólar,
# Euro ou Bitcoin) em relação ao real

# Nesse projeto eu utilizei uma API que atualiza o valor das moedas a cada 30 segundos
import PySimpleGUI as sg

import requests

import json

import time

import datetime

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacao = json.loads(requisicao.text)

# Criando as janelas(funções)

def Tela_inicial():

    #layout
    layout = [
        [sg.Text('Escolha a moeda abaixo:',size=(30,0))],
        [sg.Button('Dólar'),sg.Button('Euro'),sg.Button('Bitcoin')]
       
    ]


    #janela
    return sg.Window("Cotação da moeda",layout = layout, finalize = True)

def Dolar():
    
    sg.theme('DarkGreen')
    #layout
    layout = [
        [sg.Text('Cotação do Dólar:')],
        [sg.Output(size=(35,4))],
        [sg.Button('Voltar')]

    ]

    #janela
    return sg.Window("Cotação do Dólar",layout = layout, finalize = True)

    

def Euro():
    
    sg.theme('DarkGreen')
    #layout
    layout = [
        [sg.Text('Cotação do Euro:')],
        [sg.Output(size=(35,4))],
        [sg.Button('Voltar')]

    ]
    #janela
    return sg.Window("Cotação do Euro",layout = layout, finalize = True)

def Bitcoin():
    
    sg.theme('DarkGreen')
    #layout
    layout = [
        [sg.Text('Cotação do Bitcoin:')],
        [sg.Output(size=(35,4))],
        [sg.Button('Voltar')]

    ]
    #janela
    return sg.Window("Cotação do Bitcoin",layout = layout, finalize = True)
    


janela_iniciar,janela_dolar,janela_euro,janela_bitcoin = Tela_inicial(),None,None,None  

# Criando o loop que mantém as janelas funcionando
while True:
    janela, botao , valores =  sg.read_all_windows()
        
        
    if janela == janela_iniciar and botao == sg.WIN_CLOSED:
        break
    
    # Entrando na janela "Dólar"
    if janela == janela_iniciar and botao == 'Dólar':
        janela_dolar = Dolar()
        janela_iniciar.hide()
        print('Horário:',datetime.datetime.now())
        print('Alta do Dólar :',cotacao['USDBRL']['high'])
        print('Baixa do Dólar :',cotacao['USDBRL']['low'])

    if janela == janela_dolar and botao == 'Voltar':
        janela_iniciar.un_hide()
        janela_dolar.hide()

    if janela == janela_dolar and botao == sg.WIN_CLOSED:
        break

    # Entrando na janela "Euro"
    if janela == janela_iniciar and botao == 'Euro':
        janela_euro = Euro()
        janela_iniciar.hide()
        print('Horário:',datetime.datetime.now())
        print('Alta do Euro :',cotacao['EURBRL']['high'])
        print('Baixa do Euro :',cotacao['EURBRL']['low'])

    if janela == janela_euro and botao == 'Voltar':
        janela_iniciar.un_hide()
        janela_euro.hide()

    if janela == janela_euro and botao == sg.WIN_CLOSED:
        break
    
    # Entrando na janela "Bitcoin"
    if janela == janela_iniciar and botao == 'Bitcoin':
        janela_bitcoin = Bitcoin()
        janela_iniciar.hide()
        print('Horário:',datetime.datetime.now())
        print('Alta do Bitcoin :',cotacao['BTCBRL']['high'])
        print('Baixa do Bitcoin :',cotacao['BTCBRL']['low'])

    if janela == janela_bitcoin and botao == 'Voltar':
        janela_iniciar.un_hide()
        janela_bitcoin.hide()

    if janela == janela_bitcoin and botao == sg.WIN_CLOSED:
        break

   




