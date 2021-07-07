
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


archivo = open("UCI_std.csv","r")
contenido = archivo.readlines()
print(contenido)





