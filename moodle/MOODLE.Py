# 1. se hace un ciclo while para que el usuario ingrese el nombre del producto y se valida que no este vacio y que sea uno de los productos disponibles
while True:
    Producto = input(" INGRRESE EL  NOMBRE DEL PRODUCTO : \nmanzana , \npera , \nbanano , \ndulces : \n")
    if Producto.strip() == "":
        print("debes elegir un producto")
    elif Producto.lower() == "manzana":
        break
    elif Producto.lower() == "pera":
        break
    elif Producto.lower() == "banano":
        break
    elif Producto.lower() == "dulces":
        break
    else:
        print("Producto no disponible")
 # 2. se hacen las varibles de los otros requerimientos que nos piden y les asigna si es entero o float
while True:
    cantidad = input("Ingrese la cantidad de los productos:\n").strip()
    if cantidad.isdigit():
        cantidad = int(cantidad)
        break
    else:
        print(" Debes ingresar un número entero.")

while True:
    try:
        Precio = float(input("Ingrese el precio del producto:\n").strip())
        if Precio > 0:
            break  
        else: print(" El precio no puede ser negativo. Intenta nuevamente.")
    except ValueError:
        print(" Debes ingresar un número válido para el precio.")


while True:
    try:
        Descuento = float(input("Ingrese el descuento del producto (%):\n").strip())
        if 0 <= Descuento <= 100:
            break
        else:print(" El descuento no puede ser negativo y tiene que ser mayor o igual a 100. Intenta nuevamente.") 
    except ValueError:
        print(" Debes ingresar un número válido para el descuento.")
    
    # 3. se hace la funcion que nos pide que calcule el precio total con descuento y se retorna el total
def precio_total(cantidad, Precio, Descuento):
    if cantidad > 0 and Precio > 0:
        if 0 <= Descuento <= 100:
            total = cantidad * Precio
            total *= 1 - (Descuento / 100)
            return total
        else:
            print("El descuento es inválido. Debe estar entre 0 y 100.")
            return None   
    else:
        print("La cantidad y el precio deben ser mayores a 0.")
        return None
 # 4. se imprime el resultado de la factura de compra y se llama a la funcion que nos da el precio total con descuento, se muestra el nombre del producto y el precio total
print ("FACTURA DE COMPRA")
print ("=======================")
resultado= precio_total(cantidad, Precio, Descuento)
if resultado is not None:
    print(f"Producto: {Producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: {Precio}")
    print(f"Descuento: {Descuento}%")
    print(f"Total a pagar: {resultado:.2f}")
else:
    print("Error en la factura de compra")

 