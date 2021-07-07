
import pandas as pd
import matplotlib.pyplot as plt



x = [1,2,3]
y = [1,4,9]
plt.plot(x,y)
plt.title("Pacientes UCI")
plt.xlabel("Dias")
plt.ylabel("Casos")
plt.show()



datos= pd.read_csv("UCI_std.csv")

"""
archivo = open("UCI_std.csv","r")
contenido = archivo.readlines()
print(contenido)







menu = "0"
while menu != "5" :
    fila = 0
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    grafico1 = []
    grafico2 = []
    menu = input("Ingrese una de las opciones del 1 al 5: ")
    if menu == "1" :
        for i in regioncodigo :
            print(i)
    elif menu == "2" :
        comuna = input("Ingrese una comuna: ")
        if(comuna.isnumeric() == True) :
            for i in range(len(datos)) :
                if datos[i][3] == comuna :
                    print("Comuna encontrada: ", datos[i][2])
                    bandera1 = True
                    fila = i
            if bandera1 == False :
                print("Codigo invalido")
        else :
            for i in range(len(datos)) :
                if datos[i][2] == comuna :
                    print("Comuna confirmada, codigo es: ", datos[i][3])
                    bandera2 = True
                    fila = i
            if bandera2 == False :
                print("Nombre de la comuna invalido")
        if bandera1 == True or bandera2 == True :
            print("Ingrese el periodo de tiempo que quiere revisar")
            fecha1 = input("Ingrese la fecha de inicio: ")
            fecha2 = input("Ingrese la fecha final: ")
            for i in datos[0] :
                if fecha1 == i :
                    bandera3 = True
                if fecha2 == i :
                    bandera4 = True
            if bandera3 == False or bandera4 == False :
                print("Fecha incorrecta")
            else :
                for i in range(len(datos[0])) :
                    if bandera5 == False :
                        if fecha1 == datos[0][i] :
                            grafico1.append(datos[0][i])
                            grafico2.append(float(datos[fila][i]))
                            bandera5 = True
                    else :
                        grafico1.append(datos[0][i])
                        grafico2.append(float(datos[fila][i]))
                        if fecha2 == datos[0][i] :
                            bandera5 = False
                plt.plot(grafico1, grafico2)
                plt.show()
    elif menu == "3" :
        region = []
        porcentaje = []
        for i in range(len(datos)) :
            promedio = 0.0
            if datos[i][2] == "Total" :
                region.append(datos[i][0])
                for j in range(5, len(datos[i])) :
                    promedio = promedio + float(datos[i][j])
                porcentaje.append(int((promedio / float(datos[i][4]))* 100))
        menor = porcentaje[0] # porcentaje que esta contagiado en una región
        mayor = porcentaje[0]
        posicion1 = 0 
        posicion2 = 0
        for l in range(len(porcentaje)) :
            if menor > porcentaje[l + 1] : # la siguiente posición
                menor = porcentaje[l + 1] # almacenando el valor menor
                posicion1 = l
            if mayor < porcentaje[l + 1] :
                mayor = porcentaje[l + 1]
                posicion2 = l
            if l == (len(porcentaje)-2) : # para terminar el for
                break
        print("la region con menor densidad de contagio es: ",region[posicion1], " con un porcentaje de ", menor, "%" )
        labels = 'personas contagiadas', 'personas sanas' 
        sizes = [menor, 100-menor] # distribuir las proporciones
        explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots() 
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')  # el radio sea dibujado como un circulo
        plt.show() # mostrar el grafico circular
        labels = 'personas contagiadas', 'personas sanas'
        sizes = [mayor, 100-mayor]
        explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    elif menu == "4" :
       print("Holito")
    elif menu == "5" :
        print("Hello")
    else :
       print("Opción invalida")
"""