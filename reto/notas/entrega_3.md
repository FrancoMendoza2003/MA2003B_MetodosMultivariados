# DUDAS
1. En la descripción de la variable de la dirección del viento (WDR) se menciona que:

        Son los grados de inclinación con las que el sensor recibe el viento. Son de 0 - 360 . 360 es lo mismo que 0, solo que 0 significa Norte-este y 360 es Norte-oeste

    Esto quiere decir que si WDR = 0, el viento va viendo al noreste?

2. Para realizar una regresión lineal múltiple, debe haber correlación entre las variables predictoras y la variable dependiente, pero no entre las variables predictoras. ¿Esto se comprueba con los datos iniciales, ya después de pre-procesar/transformar, o la correlación de variables se mantiene igual? 

# Juicio de mejoras zonas 
**según menor número de valores nulos (visualmente)**

## Poblaciones que se ven **BIEN**
- centro
- <span style="color:cyan">**sureste3**

## Poblaciones que se ven **REGULAR** 
- <span style="color:cyan">**norte2**
- sureste2
- noreste2
- noroeste

## Poblaciones que se ven **HORRIBLE**
- suroeste
- <span style="color:cyan">**noroeste2**
- noreste
- suroeste2
- norte
- sur
- sureste
---
# Transformación de datos:
Para la transformación de datos se hizo el siguiente proceso:
1. Agarras los cleaned_datasets/ los cuales ya no tienen valores nulos
2. Sacas su promedio móvil (lo cual hace que los primeros observaciones se vuelvan nulos y que la distribución de datos se suavice)
3. Agrupas los datos por periodos de 4 horas donde sacas su media (?)


# Pruebas de Normalidad
- La variable de **RAINF** se comporta de manera extraña. Por ejemplo, en zona centro de plano es 0 en todas las horas. Al tener esto no se puede hacer la prueba de normalidad multivariada, pues parece que se necesita sacar la matriz de correlaciones entre las variables y al ser siempre 0, tiene covarianza 0 con todas las demás variables

- Al realizar la prueba de normalidad (**con todas las variables excepto date y RAINF**) de un solo DataFrame con todas las observaciones, la computadora se muere :(, Me empezó a ocupar 12GB de RAM y no terminó el proceso. 

- Agrupación de fechas por cada 4 horas parece ser adecuado (no se muere la computadora)
