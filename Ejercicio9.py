#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad = float(input('¿cantidad a invertir? '))
interes = float(input('¿interes porcentual anual? '))
años = int(input('¿años?'))
print('capital final:' + str(round(cantidad + (interes /100 + 1)** años, 2)))