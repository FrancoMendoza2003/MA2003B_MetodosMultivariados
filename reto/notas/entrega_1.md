# Primera Entrega de Reto
**10 de noviembre de 2023**

- Se eligieron los datos de Norte2, Sur, Sureste

**Variables elegidas por el momento: **
1. PM10
2. PM2.5
3. O3
4. PRS
5. WSR

> **Sheldon**

- Nada más tomé los datos desde Marzo de 2021 porque las zonas que escogimos tienen muchos valores nulos. Especialmente para O3 y PM2.5

- Impute los campos de fechas/horas faltante en los datasets, y TODOS los valores nulos fueron rellenados con metodo backfill (bfill) donde se copia el siguiente valor no nulo

- Apliqué una transformación de datos utilizando boxcox para TODAS las zonas, especialmente para las  variables PM10, PM2.5, O3 y WSR.
