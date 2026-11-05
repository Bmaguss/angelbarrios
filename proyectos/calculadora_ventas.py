Precio Base
precio = 250
#Valida la cantidad ingresada
while True:
    try:
        cantidad = int(input("Ingrese la cantidad "))

        if cantidad <= 0:
            print("Cantidad no válida. Ingrese un número mayor que cero.")
        else:
            break

    except ValueError:
        print("Debés ingresar un número válido.")

descuento = 0
total = precio * cantidad

if cantidad >= 5:
    print("«Compra por mayor»")
else:
    print("«Compra minorista»")

if total >= 2000:
    print("Compra muy Grande")
elif total >= 1000:
    print("Compra Grande")
else:
    print("Compra pequeña")

if cantidad >= 5 and total >= 1000:
    descuento = 100
    print("Descuento especial")
elif cantidad >= 5:
    descuento = 50
    print("Descuento por cantidad")
else:
    descuento = 0
    print("Sin Descuento")

resultado = total - descuento
print("Precio original", total)
print("Descuento", descuento)
print("El precio es", resultado)
