from datetime import date
from datetime import datetime
import display

def save(diccionario, lista):
    fEntradas = open('ventas{}{}{}.txt'.format(date.today().day,date.today().month,date.today().year), 'a+')
    ticket=lista

    lista=[]
    diccionario ={"Bebe":0, "Menor": 0, "Adulto":0, "Juvilado":0}
    strTotal=''
    for elemento in ticket:
        strTotal = strTotal + str(elemento)+';'
    strTotal = strTotal[:-1] +'\n'
    fEntradas.write(strTotal)
    fEntradas.close()
    display.clearResult()
    return (diccionario, lista)
def load(dia,mes,anno):
    reg=[]
    registro=[]
    listaTotal=[]
    fEntradas = open('ventas{}{}{}.txt'.format(str(dia),mes,anno), 'r+')
    data= fEntradas.read()
    data=data.split('\n')
    
    for i in range(len(data)):
        reg=(data[i].split(';'))
        listaEnteros=[]
        for elemento in reg:

            listaEnteros.append(int(elemento))
            listaTotal.append(int(elemento))

        
        registro.append(listaEnteros)
    return (registro, listaTotal)
load(date.today().day,date.today().month,date.today().year)
