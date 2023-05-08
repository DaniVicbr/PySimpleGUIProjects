#Verificador de ano bissexto:
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Digite o ano (Ex.: 1500):')],
            [sg.InputText(size = (20, 1))],  
            [sg.Text('Resultado:')], 
            [sg.InputText(size = (20, 1), key = 'year')], 
            [sg.Button('Ok'), sg.Button('Cancelar')]] 

window = sg.Window('Verificador Ano Bissexto', layout) # element_justification='c'

def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

        
while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Ok':
        year = int(values[0])
        if is_leap(year):
                window['year'].update('ANO BISSEXTO!')
        else:
            window['year'].update('NÃO É BISSEXTO!')

window.close()


