def clear():
    print("\033[2J")
def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")
colors ={
    'black':'30',
    'red':'31',
    'green':'32',
    'yellow':'33',
    'blue':'34',
    'magenta':'35',
    'cyan':'36',
    'white':'37',
    'reset':'39'
    }
colorsbg ={
    'black':'40',
    'red':'41',
    'green':'42',
    'yellow':'43',
    'blue':'44',
    'magenta':'45',
    'cyan':'46',
    'white':'47',
    'reset':'49'
    }
style ={
    'bold':'1',
    'underline':'4',
    'blink':'5',
    'reverse':'7',
    'reset':'0'
    }
def procesarparametros(params):
    if 'linea' in params:
        linea = params ['linea']
        columna = 1
        if 'columna' in params:
            columna = params ['columna']
    locate(linea, columna)
    if 'color' in params and params['color'] in colors:
        print("\33[{}m".format(colors[params['color']]), end="")
    if 'bg' in params and params['bg'] in colorsbg:
        print("\33[{}m".format(colorsbg[params['bg']]), end="")
    if 'style' in params and params['style'] in style:
        print("\33[{}m".format(style[params['style']]), end="")
    
def Print(texto, **parametros):
    procesarparametros(parametros)
    print(texto)
    reset()
    #linea, columna, estilo, colortx, color bg, tend
def Input(texto, **parametros):
    procesarparametros(parametros)
    return input(texto)
    #linea, columna, estilo, colortx, color bg, tend
def reset():
    print("\33[{}m".format(colors['reset']), end="")
    print("\33[{}m".format(colorsbg['reset']), end="")
    print("\33[{}m".format(style['reset']), end="")