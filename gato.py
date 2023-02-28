from random import choice

def gato():
    '''Juego del gato'''
    en_juego = True
    gano = False
    tablero_str = "123456789"
    tablero = { pos:pos for pos in tablero_str } # compresión | comprehension llave:valor
    jugadas = 0
    mostrar_tablero(tablero)
    while en_juego == True and jugadas < 9:

        simbolo = input("Seleccione celda a jugar (entre 1 y 9):")
        if simbolo in tablero:               #existe el símbolo en el tablero?
            if simbolo == tablero[simbolo]:  #está la celda ocupada?
                tablero[simbolo] = 'X'
                jugadas += 1
                if checar_si_gano(tablero,"X") == True:
                    gano = True
                    en_juego = False
                else:
                    simbolo = checar_disponible(tablero)
                    tablero[simbolo] = "O"
                    jugadas += 1
                    if checar_si_gano(tablero,"O") == True:
                        en_juego == False
            else:
                print("Celda ocupada, seleccione otra...")
        else:
            print("Celda no existe, seleccione una entre 1 y 9 ...")
        # pedir input
        # registrar input en el tablero
        # checar o verificar si ganó
            # si ya ganó, salimos
            # si no ganó:
                #ahora juega la computadora, le pedimos su "input"
                #verificamos si ganó
                    # si ganó, salimos
        mostrar_tablero(tablero)
    if gano == True:
        print("¡Felicidades!")
    else:
        print("¡Lástima!")

def checar_si_gano(tablero,simbolo):
    # 1 2 3
    # 4 5 6 
    # 7 8 9
    # if simbolo == tablero['1'] and simbolo == tablero['2'] and simbolo == tablero['3']:
    #     return True
    # if simbolo == tablero['4'] and simbolo == tablero['5'] and simbolo == tablero['6']:
    #     return True
    # if simbolo == tablero['7'] and simbolo == tablero['8'] and simbolo == tablero['9']:
    #     return True
    combinaciones = [ ['1','2','3'],
                      ['4','5','6'],
                      ['7','8','9'],
                      ['1','4','7'],
                      ['2','5','8'],
                      ['3','6','9'],
                      ['1','5','9'],
                      ['7','5','3']
    ]
    for combo in combinaciones:
        contador = 0
        for celda in combo:
            if simbolo == tablero[celda]:
                contador += 1
        if contador == 3:
            return True
    return False

def checar_disponible(tablero:dict)->str:
    disponibles = []
    for llave,valor in tablero.items():
        if llave == valor:  #está la celda disponible?
            disponibles.append(valor)
    return choice(disponibles)


def  mostrar_tablero(tablero:dict)->None:
    '''Despliega el tablero de Juego'''
    #print(tablero)
    print(tablero['1'],"|",tablero['2'],"|",tablero['3'])
    print("---------")
    print(tablero['4'],"|",tablero['5'],"|",tablero['6'])
    print("---------")
    print(tablero['7'],"|",tablero['8'],"|",tablero['9'])
    print("")


def asignar_simbolo(tablero:dict,celda:str,simbolo:str):
    if celda == tablero[celda]:
        tablero[celda] = simbolo

def limpia_tablero():
    tablero_str = "123456789"
    tablero = { pos:pos for pos in tablero_str } # compresión | comprehension llave:valor
    return tablero


def main():
    gato()

if __name__ == "__main__":
    main()