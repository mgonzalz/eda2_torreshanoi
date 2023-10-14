from pilaHanoi import Pila

def getTablero(n):
    tablero = []
    for i in range(3):
        tablero.append(Pila(i+1))
    for i in range(n, 0, -1):
        tablero[0].apilar(i)
    return tablero


def solve(tablero, n, A, B, C, movimientos):
    if n == 1:
        disco = tablero[A].desapilar()
        tablero[C].apilar(disco)
        movimientos.append(f"D{disco} from T{A + 1} to T{C + 1}")
        return

    solve(tablero, n - 1, A, C, B, movimientos)
    disco = tablero[A].desapilar()
    tablero[B].apilar(disco)
    movimientos.append(f"D{disco} from T{A + 1} to T{C + 1}")
    solve(tablero, n - 1, C, B, A, movimientos)

if __name__ == '__main__':
    print('INICIO TORRES')
    tablero = getTablero(5)
    for i in range(3):
        print(tablero[i])
    
    print('MOVIMIENTOS')
    movimientos = []
    solve(tablero, len(tablero), 0, 1, 2, movimientos)
    for i in movimientos:
        print(i)
    
    print('FIN TORRES')
    for i in range(3):
        print(tablero[i])
