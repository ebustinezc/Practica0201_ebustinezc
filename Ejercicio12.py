#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y la ganancia final total.
barras = int(input('numero de barras vendidas que no son frescas '))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1 - descuento)
print('coste de barra fresca:' , (precio),'€')
print('descuento sobre una barra no fresca' , (descuento * 100) , '%')
print('coste final a pagar es:' , (round(coste, 2)) , '€')