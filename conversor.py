# El numeral coloca la linea en comentario
menu = """BIENVENIDO AL CONVERSOR DE MODEDAS

1 - Pesos Colombianos 
2 - Pesos Argentinos
3 - Pesos Mexicanos 

Elige una opción: """

opcion = int(input(menu)) 

if opcion == 1: 
    pesos = float(input("¿Cuántos pesos Colombianos tienes? "))
    valor_dolar = 3875
    dolares = round(pesos /valor_dolar, 2)
    print("Tienes $" + str(dolares)+ " dólares")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos Argentinos tienes? "))
    valor_dolar = 65
    dolares = round(pesos /valor_dolar, 2)
    print("Tienes $" + str(dolares)+ " dólares")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos Mexicanos tienes? "))
    valor_dolar = 24
    dolares = round(pesos /valor_dolar, 2)
    print("Tienes $" + str(dolares)+ " dólares")
else:
    print("Ingresa una opción correcta")