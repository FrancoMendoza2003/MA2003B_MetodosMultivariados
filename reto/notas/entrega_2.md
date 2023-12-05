

- Precursores de O3
- Buscar posibles causas de las condiciones (valores) de las variables según las zonas (si hay industria cerca, aeropuerto, etc.) 
- Imputación: Media entre siguiente y anterior valor válido.

- Valores Nulos: Si el valor atípico está muy alejado de los demás valores, entonces se quita. 
- Checar si se necesita normalidad para el tema a elegir.
- Si se tiene una normal multivariada casi 'garantiza' normal univariada.

- Condiciones de estaciones. 

> **Intentar acotar únicamente a uno de los siguientes temas**:
1. Suavizar (desestacionalizar) (puede necesitar normalidad)
2. Regresión de contaminación (con variable proporción PM2.5/PM10) (sí )
3. Conglomeración (clustering de zonas)


> **Cosas que hacer**
1. Verificar datos atípicos, si están muy alejados de los demás valores se puede quitar (preguntar al OSF que tanto es tanto)
2. Definir tema bien
3. Hacer mejor método de relleno de nulos (promedio de siguiente y anterior valor nulo)
4. Crear nueva variable? (PM2.5/PM10)
5. Checar si realmente se quiere normalidad de los datos según el tema elegido
