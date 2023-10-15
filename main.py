from pilaHanoi import Pila

def getTablero(n):
    tablero = []
    for i in range(3):
        tablero.append(Pila())
    for i in range(n, 0, -1):
        tablero[0].apilar(i)
    return tablero


def solve(tablero, n, origen, destino, aux, movimientos):
    if n == 1:
        disco = tablero[origen].desapilar()
        tablero[destino].apilar(disco)
        movimientos.append(f"D{disco} from T{origen + 1} to T{destino + 1}")
        return

    solve(tablero, n - 1, origen, aux, destino, movimientos)
    disco = tablero[origen].desapilar()
    tablero[destino].apilar(disco)
    movimientos.append(f"D{disco} from T{origen + 1} to T{destino + 1}")
    solve(tablero, n - 1, aux, destino, origen, movimientos)

if __name__ == '__main__':
    n = 5
    print('INICIO TORRES')
    tablero = getTablero(n)
    for i in tablero:
        print(f'Tablero: {i}')
    print('MOVIMIENTOS')
    movimientos = []
    solve(tablero, n, 0, 1, 2, movimientos)
    for i in movimientos:
        print(i)
    
    print('FIN TORRES')
    for i in tablero:
        print(f'Tablero: {i}')

