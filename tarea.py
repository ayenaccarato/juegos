import PySimpleGUI as sg
import json
import hangman
import reversegam
import tictactoeModificado
from os.path import isfile

''' Para crear la estructura, uso 2 diccionarios:
1-Contiene el nombre del jugador
2-Contiene los juegos con la cantidad de veces que jugó a cada uno
Utilicé json porque al ser un archivo de texto independiente del lenguaje que se use,
es más legible para el usuario al momento que se quiera acceder a los datos, y con los 2 diccionarios
me pareció la manera más prolija de presentar los datos guardados'''

nombre = 'tareaJuegos.json'
dic = {}
dic2 = {'Ahorcado': 0, 'Ta-Te-Ti': 0, 'Otello': 0}

def leerArchivo(nombre):
    with open(nombre, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos (nombre,dic):
    with open(nombre,'w') as f:
        json.dump(dic,f)

def cargar_jugadores (nombre,values,dic):
    nom = values[0].lower()
    if isfile('tareaJuegos.json'):
        dic = leerArchivo(nombre)

        if nom in dic.keys():
            if dic2['Ahorcado'] != 0:
                dic[nom]['Ahorcado']  += dic2['Ahorcado']
            if dic2['Ta-Te-Ti'] != 0:
                dic[nom]['Ta-Te-Ti'] += dic2['Ta-Te-Ti']
            if dic2['Otello'] != 0:
                dic[nom]['Otello'] += dic2['Otello']
        else:
            dic[nom] = dic2
    else:
        dic[nom] = dic2

    guardar_datos(nombre,dic)
    dic2['Ahorcado'] = 0
    dic2['Ta-Te-Ti'] = 0
    dic2['Otello'] = 0

layout = [[sg.Text('Menu')],[sg.Text('Nombre del jugador'),sg.InputText()],
[sg.Text('Juego')], [sg.Button('Ahorcado'),sg.Button('Ta-Te-Ti'),sg.Button('Otello')],
[sg.Button('Salir')]]

window = sg.Window('Bienvenido').Layout(layout)
window.Finalize()

while True:
    event, values = window.Read()
    if event is None or event == 'Salir':
        break
    elif event is 'Ahorcado':
        hangman.main()
        dic2['Ahorcado'] += 1
    elif event is 'Ta-Te-Ti':
        tictactoeModificado.main()
        dic2['Ta-Te-Ti'] += 1
    elif event is 'Otello':
        reversegam.main()
        dic2['Otello'] += 1
    cargar_jugadores(nombre,values,dic)
