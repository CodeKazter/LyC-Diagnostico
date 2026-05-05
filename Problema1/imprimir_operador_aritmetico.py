import unicodedata
operacion = input("Ingresa una operación aritmetica: ")
i = 0
numeros = str([0,1,2,3,4,5,6,7,8,9,"."])
operadores = ["+", "-", "*", "/"]

try:
    res = eval(operacion)
    print(f"Resultado: {res}")
    print("")
except ZeroDivisionError:
        print("ERROR")
        exit()
except SyntaxError:
     print("No es posible evaluar: Solo ingresar numeros")
        
while i < len(operacion):
    if operacion[i] == " ":
         i += 1
         continue
    elif operacion[i] in numeros:
         str_temp= f"Numero {operacion[i]}"
         try:
            if operacion[i+1] in numeros:
                str_temp += operacion[i+1]
                i+=1
                print(str_temp)
         except IndexError:
            break

         i += 1
    elif operacion[i] in operadores:
         print(f"Operador {operacion[i]}")
         i += 1
    else:
         i += 1 
         continue
         