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
cantidad = int(input("Ingrese la cantidad de los productos : \n"))
Precio = float(input("Ingrese el precio del producto : \n"))
Descuento = float(input("Ingrese el descuento del producto : \n"))
print("quieres seguir comprando si o no? \n")
products.append(Producto) 
    # 3. se hace la funcion que nos pide que calcule el precio total con descuento y se retorna el total
def precio_total(cantidad, precio, descuento):
    if cantidad > 0 and precio > 0:
        total = cantidad * precio
        if 0 <= descuento <= 100:
            total *= 1 - (descuento / 100)
        else:
            print("El descuento es inválido. Debe estar entre 0 y 100.")
            return None
        return total
    else:
        print("La cantidad y el precio deben ser mayores a 0.")
        return None
 # 4. se imprime el resultado de la factura de compra y se llama a la funcion que nos da el precio total con descuento, se muestra el nombre del producto y el precio total
print ("FACTURA DE COMPRA")
print ("=======================")

print(f"EL PRODUCTO ES : {Producto}\n EL PRECIO TOTAL CON DESCUENTO ES : {precio_total(cantidad,Precio,Descuento)}")
