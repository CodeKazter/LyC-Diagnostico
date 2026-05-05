def calcular_collatz(n):
    pasos = 0
    secuencia = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
        secuencia.append(n)
        pasos += 1
        
    return pasos, secuencia

def verificar_intervalo_collatz(p, q):
    """
    Verifica la conjetura de Collatz para todos los enteros en el intervalo [p, q],
    exigiendo la regla q >= 100p.
    """
    # Validación básica de enteros positivos
    if p < 1:
        print("Error: El límite inferior 'p' debe ser un entero positivo (p >= 1).")
        return

    # Nueva regla estricta: q debe ser mayor o igual a 100 veces p
    if q < 100 * p:
        print(f"Los numeros actuales cincumplen la regla de q >= 100p")
        print(f"Valores actuales: p = {p}, q = {q}. Se requiere que q sea al menos {100 * p}.")
        return
    
    max_pasos = 0
    num_max_pasos = p
    
    for i in range(p, q + 1):
        pasos, secuencia = calcular_collatz(i)
        
        print(f"{secuencia[0]}: {secuencia}")
        print()

        if pasos > max_pasos:
            max_pasos = pasos
            num_max_pasos = i
    
            
    print(" Todos los números en el intervalo llegaron a 1.")
    print(f"El número con la secuencia más larga fue {num_max_pasos}, requiriendo {max_pasos} pasos.")

# --- Ejemplo de uso ---
try:
    p = int(input("Introduce el valor de p (limite inferior): "))
    q = int(input("introduce el valor de q (limite superior): "))
except TypeError:
    print("Ingrese solo numeros por favor")
    exit() 
except ValueError:
    print("Ingrese solo numeros por favor")
    exit() 
verificar_intervalo_collatz(p, q)