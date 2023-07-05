"""
    Escribir una función que, dados cuatro números, devuelva el mayor producto de
    dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
    más grande que se puede obtener entre ellos (8 = −2 × −4).
"""

def mayor_producto(num1,num2,num3,num4):
    # Devuelve el mayor producto de dos de ellos
    numeros = [num1,num2,num3,num4]
    max_producto = 0

    for i in range(3):
        # print(f"i={i}")
        for j in range(i+1,4):
            producto=numeros[i]*numeros[j]
            # print(f"j={j}")
            # print(f"{numeros[i]} * {numeros[j]}= {producto}")
            if producto>max_producto:
                max_producto=producto 
            # print(f"max produc= {max_producto}")
    print(f"El mayor producto de los numeros: {num1}, {num2}, {num3} y {num4}, es: {max_producto}.")
    

mayor_producto(1,5,-2,-4)