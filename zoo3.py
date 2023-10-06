import screen
import display
import resultados
from screen import Print
from datetime import date
from datetime import datetime
from datamemory import save
from datamemory import load
finalizar = 0
clientes ={"Bebe":0, "Menor": 0, "Adulto":0, "Juvilado":0}
registro = []
precios = {"Bebe":0, "Menor": 14, "Adulto":23, "Juvilado":18}
ventasDia=[]
screen.clear() 
display.pintaBanner()
screen.locate(2,1)
fechaHoy = "{}/{}/{}".format(date.today().day,date.today().month,date.today().year)
while finalizar != 1:
    edad = display.evaluaInput()
    if edad == "x":
        finalizar = 1
    elif edad == "z":
        if sum(clientes.values())!=0:
            resultado = display.aumentaclientes(registro, clientes, registro[-1], -1)
            registro = resultado[0]
            clientes = resultado[1]
            display.resutl(clientes, precios)
    elif edad == "v":
            delete = display.lastReg(registro)
            if delete[0] == "y":
                resultado = display.aumentaclientes(registro, clientes, int(registro[int(delete[1])]), -1, delete[1])
                registro = resultado[0]
                clientes = resultado[1]
            else:
                pass
    elif edad == "g":
        if sum(registro)==0:
            Print('no hago nada', linea=1, colunma=1)
        else:
            resultado = save(clientes, registro)
            registro = resultado[1]
            clientes = resultado[0]
    elif edad == "o":
        
        loaded = load(date.today().day,date.today().month,date.today().year)
        registro = []
        clientes ={"Bebe":0, "Menor": 0, "Adulto":0, "Juvilado":0}
        for element in loaded[1]:
            resultado = display.aumentaclientes(registro, clientes, element, 1)
            registro = resultado[0]
            clientes = resultado[1]
        display.resutl(clientes, precios)
        registro = []
        clientes ={"Bebe":0, "Menor": 0, "Adulto":0, "Juvilado":0}
    else:
        resultado = display.aumentaclientes(registro, clientes, edad, 1)
        registro = resultado[0]
        clientes = resultado[1]
        display.resutl(clientes, precios)
        
screen.locate(40,3)