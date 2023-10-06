import screen
from screen import Print
from screen import Input
#Estas 2 funciones limpian las zona de menu y resultado
def clearMenu():   
    for i in range (6,39):
        Print("|"+ " "*47,linea=i,columna=1, color='blue')
def clearRegs():   
    for i in range (16,39):
        Print("|"+ " "*47,linea=i,columna=1, color='blue')
def clearRegsdel(fin):   
    for i in range (fin,39):
        Print("|"+ " "*47,linea=i,columna=1, color='blue')   
   
def clearResult():
    for i in range (6,39):
        Print("|"+ " "*68,linea=i,columna=50, color='blue')
#Esta pinta el marco y pone el titulo de arriba 

def pintaBanner():
    horizontal="|" + "="*118 + "|"
    Print(horizontal, linea=1, columna=1, color='blue')
    for i in range(1,40):
        Print("|",linea=i+1,columna=1, color='blue')
        if i > 4:
            Print("|",linea=i+1,columna=50, color='blue')

        Print("|",linea=i+1,columna=len(horizontal), color='blue')

    Print(horizontal, linea=5, columna=1, color='blue')
    Print(horizontal, linea=40, columna=1, color='blue')
    titulo = "- - - - PRACTICA ZOO - - - -"
    Print(titulo, linea=3, columna=int((len(horizontal)/2) - (len(titulo)/2)), color='red')
def locateH(ini, cad):
    return ini - len(str(cad))
    
def resutl(clientes, precios):
    linea = 9
    inicio= 63
    fin = 98
    totalPrecio = 0
    totalClientes =0
    clearResult()
    for key in clientes:
        if clientes[key]>0:
            locate=locateH(inicio, clientes[key])
            Print("{} entrada de {} a {}€".format(clientes[key],key, precios[key]),linea=linea, columna=locate)
            locate=locateH(fin, clientes[key] * precios[key])
            Print("Total {}€".format(clientes[key] * precios[key]),linea=linea, columna=locate)
            linea += 1
            totalPrecio = totalPrecio + clientes[key] * precios[key]
            totalClientes = totalClientes + clientes[key]
    Print("-"*48, linea=linea, columna= inicio - len(str(totalClientes)),style='bold')
    locate=locateH(inicio, totalClientes)
    Print("Total entradas: {}".format(totalClientes),linea=1+linea, columna=locate, style='bold', color='green')
    locate=locateH(fin, totalPrecio)
    Print("Total {}€".format(totalPrecio),linea=1+linea, columna=locate, style='bold', color='green')
    pintaBanner()
    if sum(clientes.values())==0:
        clearResult()
def menu0():
    
    Print("[x] EXIT", linea=10, columna=3, color='black', bg='white')
    Print("[z] DEL ANTERIOR", linea=11, columna=3, color='black', bg='white')
    Print("[v] MUESTRA REGISTROS", linea=12, columna=3, color='black', bg='white')
    Print("[g] GUARDAR VENTA", linea=13, columna=3, color='black', bg='white')
    Print("[o] MOSTRAR VENTAS GUARDAS", linea=14, columna=3, color='black', bg='white')
    valueStr = Input("Introduca Edad:", linea=7, columna=3,style='bold')
    valueStr = valueStr.replace(',', '.')
    return valueStr
def lastReg(reg):
    avanza=0
    for i in range(0,len(reg),15) :
        avanza=-1
        clearRegsdel(20+avanza)
        for j in range(0,15) :
            if len(reg)>i+j:
                avanza +=1
                texto="posicion {}".format(i+j) + " "*(6-len(str(i+j))) + "-" + " "*(6-len(str(reg[i+j]))) + "{} años".format(reg[i+j], end="")
                Print(texto, linea=20+avanza, columna=11)
                
            

        #una entrada para {}.
        finregistros= avanza +21
        clearRegsdel(finregistros)
        Input("Intro para continuar", linea=21+avanza, columna=11, color='black', bg='white')
        screen.reset()
            
        avanza +=1
        finregistros= avanza +21
        clearRegsdel(finregistros)
    Print("Fin de la lista", linea=20+avanza, columna=11, color='black', bg='white')
    indice = "f"
    delete = Input("Desea eliminar algun elemento? y/N", linea=21+avanza, columna=11, color='black', bg='white')
    screen.reset()
    while delete.lower() == 'y':
        indice= (Input("Introduzca indice a eliminar? ", linea=22+avanza, columna=11, color='black', bg='white'))
        try:
            Print("Se va a eliminar el elemento", linea=23+avanza, columna=11, color='black', bg='white')
            Print("posicion {} - {} años".format(int(indice), reg[int(indice)]), linea=25+avanza, columna=11)
            delete = Input("Esa seguro? y/N ", linea=27+avanza, columna=11, color='black', bg='white')
            screen.reset()
            print(indice)
            return (delete.lower(), indice)
        except:
            Input("El elemento seleccionado no existe.", linea=29+avanza, columna=11, color='red', bg='yellow')
            screen.reset()
            clearRegsdel(finregistros)
            delete = Input("Desea eliminar algun elemento? y/N", linea=21+avanza, columna=11, color='black', bg='white')
            screen.reset()
    screen.reset()
    return (delete.lower(), indice)
    
    
def evaluaInput():
    repeat = True    
    while repeat == True:
        clearMenu()
        valueStr = menu0()
        
        if valueStr.lower() == "x":
            return "x"
        elif valueStr.lower() == "z":
             return "z"
        elif valueStr.lower() == "v":
            return "v"
        elif valueStr.lower() == "g":
            return "g"
        elif valueStr.lower() == "o":
            return "o"
        else:
            value = entero(valueStr)
            if value == None or value < 0:
                Input("Valor o parametro invalido",linea=8,columna=3,color='yellow', bg='red')
                screen.reset()
            else:
                repeat = False
                return value
def entero(n):   
    try:
        e = int(n)
    except:
        e = None
    return e

def recuperaTipo(a):
    if a <= 2:
        return "Bebe"
    elif a <= 12:
        return "Menor"
    elif a < 65:
        return "Adulto"
    else:
        return "Juvilado"

def aumentaclientes(reg,acumulador , age, i, index=-1):
    if i == 1:
        reg.append(age)
    else:
        reg.pop(int(index))
    key = recuperaTipo(age)
    acumulador[key] = acumulador[key] + i
    return (reg,acumulador)
