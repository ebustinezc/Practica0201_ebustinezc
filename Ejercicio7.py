#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input('¿Cual es tu peso en kg?'))
estatura = float(input('¿cual es tu estatura en metros?'))
imc = round(peso / (estatura * estatura), 2)
print ('tu indice de masa corporal es ', imc)
