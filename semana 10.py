1.-Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.

import pandas as pd

inicio=int(input('Introduceelañoinicial:'))
fin=int(input('Introduceelañofinal:'))
ventas={}
for i in range(inicio,fin+1):
      ventas[i]=float(input('Introducelasventasdelaño'+str(i)+':'))
ventas=pd.Series(ventas)
print('Ventas\n',ventas)
print('Ventascondescuento\n',ventas*0.9)

#2.-Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.
import pandas as pd
def estadistica_notas(notas):
    notas=pd.Series(notas)
    estadisticos=pd.Series([notas.min(),notas.max(),notas.mean(),notas.std()],inde
x=['Min','Max','Media','Desviacióntípica'])
    returnestadisticos
    
notas={'Juan':9,'María':6.5,'Pedro':4,'Carmen':8.5,'Luis':5}
print(estadistica_notas(notas))

#3.-Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
import pandas as pd
def aprobados(notas):
    notas=pd.Series(notas)
    returnnotas[notas>=5].sort_values(ascending=False)
    
notas={'Juan':9,'María':6.5,'Pedro':4,'Carmen':8.5,'Luis':5}
print(aprobados(notas))

#4.-Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
import pandas as pd
datos={'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
contabilidad=pd.DataFrame(datos)
print(contabilidad)

#5.-Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas -gastos) total en los meses indicados.
import pandas as pd
datos={'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
contabilidad=pd.DataFrame(datos)

def balance(contabilidad,meses):
    contabilidad['Balance']=contabilidad.Ventas-contabilidad.
    Gastos return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()
    
print(balance(contabilidad,['Enero','Marzo']))
    
#6.-El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:nombre(nombre de la empresa),Final(precio de la acción al cierre de bolsa),Máximo(precio máximo de la acción durante la jornada),Mínimo(precio mínimo de la acción durante la jornada),volumen(Volumen al cierre de bolsa),Efectivo(capitalización al cierre en miles de euros).
#Construiruna función que construya un DataFrame a partir del un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.
import pandas as pd
def resumen_cotizaciones(fichero):
    df=pd.read_csv(fichero,sep=';',decimal=',',thousands='.',index_col=0)return pd.DataFrame([df. min(),df. max(),df.mean()],index=['Mínimo','Máximo','Media'])
    
resumen_cotizaciones('cotizacion.csv')
    
archivo csv
#7.-Remover las últimasnfilas (registros) de un objetoDataFrameusandoiloc.
import pandas as pd
import numpy as np

nombre=['Oliva','Daniela','Juan','Germán','Edward','Alex','Julio','Edgar','Angie','Irlesa']
puntaje=[11.5,8,15.5,np.nan,8,19,13.5,np.nan,8,18]
intentos=[1,3,2,3,2,3,1,1,2,1]
califico=['Sí','No','Sí','No','No','Sí','Sí','No','No','Sí']
indices=['a','b','c','d','e','f','g','h','i','j']
jugadores={'nombre':nombre,'puntaje':puntaje,'intentos':intentos,'califico':califico}

df=pd.DataFrame(data=jugadores,index=indices)

print(df)
n = 5

print(df.iloc[0:-n])