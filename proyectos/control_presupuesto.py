saldo = 5000
total = 0 
while True: 
    try:
        gasto = int(input("Ingrese el importe del gasto: "))
        if gasto < 0:
           print("Ingrese valor valido")     
        
        elif gasto == 0:
        
            break 
        else:
            if gasto <= saldo:
                total += gasto
                saldo = saldo - gasto
                print("Presupuesto restante", saldo)
            else:
                print("Saldo insuficiente.")
    except ValueError:
        print("Debés ingresar un número válido.")
print("Total gastado", total)
print("Presupuesto restante", saldo)  
if saldo == 0:
    print("Presupueso agotado")
elif saldo >= 2500:
    print("Presupuesto Saludable")
else:
    print("Poco Presupuesto")
