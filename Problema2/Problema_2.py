import re

def validar_fen(c: str):

    partes = c.strip().split(' ')
    if len(partes) != 6:
        return False, f"Error: Una cadena FEN debe tener 6 partes separadas por espacios. Encontradas: {len(partes)}"
    
    piezas, turno, enroque, al_paso, medios_movs, movs_completos = partes
    
    # 1. Validar la disposición de las piezas (Campo 1)
    filas = piezas.split('/')
    if len(filas) != 8:
        return False, f"Error: El tablero debe tener exactamente 8 filas separadas por '/'. Encontradas: {len(filas)}"
    
    conteo_reyes = {'K': 0, 'k': 0}
    
    for i, fila in enumerate(filas):
        suma_casillas = 0
        anterior_es_numero = False
        
        for char in fila:
            if char.isdigit():
                if anterior_es_numero:
                    return False, f"Error en fila {8-i}: No puede haber números consecutivos (ej. '11' debe ser '2')."
                valor = int(char)
                if valor == 0:
                    return False, f"Error en fila {8-i}: El número 0 no es válido para casillas vacías."
                suma_casillas += valor
                anterior_es_numero = True
            elif char in "pnbrqkPNBRQK":
                suma_casillas += 1
                anterior_es_numero = False
                if char == 'K': conteo_reyes['K'] += 1
                if char == 'k': conteo_reyes['k'] += 1
            else:
                return False, f"Error en fila {8-i}: Carácter inválido '{char}'."
                
        if suma_casillas != 8:
            return False, f"Error en fila {8-i}: La suma de piezas y espacios debe ser exactamente 8. Actual: {suma_casillas}"
            
    if conteo_reyes['K'] != 1 or conteo_reyes['k'] != 1:
        return False, "Error: Debe haber exactamente un rey blanco ('K') y un rey negro ('k')."

    if turno not in ['w', 'b']:
        return False, "Error: El turno debe ser 'w' (blancas) o 'b' (negras)."
        
    if not re.fullmatch(r'-|[KQkq]{1,4}', enroque):
        return False, "Error: Enroque inválido. Debe ser '-' o una combinación de 'K', 'Q', 'k', 'q'."
        
    # 4. Validar casilla objetivo al paso (Campo 4)

    if not re.fullmatch(r'-|[a-h][36]', al_paso):
        return False, "Error: Casilla al paso inválida. Debe ser '-' o una coordenada válida (ej. 'e3', 'c6')."
        
    # 5. Validar reloj de medios movimientos (Campo 5)
    if not medios_movs.isdigit():
        return False, "Error: El reloj de medios movimientos debe ser un número entero mayor o igual a 0."
        
    # 6. Validar número de movimiento completo (Campo 6)
    if not movs_completos.isdigit() or int(movs_completos) < 1:
        return False, "Error: El número de movimiento completo debe ser un entero mayor o igual a 1."
        
    return True, "¡La cadena FEN es completamente válida!"

casos_prueba = [
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", # Posición inicial (Válida)
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1", # Tras 1. e4 (Válida)
    "8/8/8/8/8/8/8/8 w - - 0 1", # Inválida: faltan reyes
    "rnbqkbnr/pppppppp/9/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", # Inválida: fila suma 9
    "rnbqkbnr/pp1pp1pp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", # Válida: huecos intermedios
]

for c in casos_prueba:
    valida, mensaje = validar_fen(c)
    print(f"FEN: {c}\nResultado: {mensaje}\n")