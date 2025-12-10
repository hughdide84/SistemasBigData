# Creamos una matriz de 10 filas y 3 columnas rellenada por filas
x <- matrix(
  c(1, 2, 3,
    4, 5, 6,
    7, 8, 1,
    2, 8, 2,
    3, 5, 3,
    7, 6, 6,
    4, 8, 1,
    7, 3, 2,
    5, 2, 4,
    7, 1, 3
  ),
  nrow = 10, ncol = 3, byrow = TRUE
)

# Obtenemos la clase del objeto x
class(x)

# Consultamos el tipo interno de datos de x
typeof(x)

# Obtenemos la longitud total (número total de elementos) de x
length(x)

# Obtenemos las dimensiones de la matriz (filas y columnas)
dim(x)

# Consultamos los nombres de filas/columnas (si no existen, devuelve NULL)
names(x)

# Mostramos las primeras 6 filas de la matriz
head(x)

# Mostramos las últimas 6 filas de la matriz
tail(x)

# Mostramos la estructura interna del objeto (tipo, dimensiones, datos)
str(x)

# Generamos un resumen estadístico de cada columna
summary(x)

# Consultamos todos los atributos asociados al objeto x
attributes(x)