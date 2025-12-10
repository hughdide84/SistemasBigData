# Instalar librerías necesarias
install.packages("nycflights13")

# Cargamos las librerías necesarias
library(nycflights13)

# Cargamos el data frame flights (ya viene dentro de nycflights13)
flights <- nycflights13::flights

# Número de filas
nrow(flights)

# Número de columnas
ncol(flights)

# Mostramos las primeras 6 filas
head(flights)

# Mostramos la estructura interna: tipo de cada columna
str(flights)

# Resumen estadístico de todas las columnas
summary(flights)

# Número de vuelos el 1 de enero
vuelos_1_enero <- flights[flights$month == 1 & flights$day == 1, ]
nrow(vuelos_1_enero)

# Número de vuelos desde JFK
vuelos_JFK <- flights[flights$origin == "JFK", ]
nrow(vuelos_JFK)

# Número de vuelos con retraso de llegada mayor a 60 minutos
vuelos_mas_60 <- flights[flights$arr_delay > 60, ]
nrow(vuelos_mas_60)


# Creamos nueva columna con el retraso total
flights <- cbind(
  flights,
  total_delay = flights$dep_delay + flights$arr_delay
)
flights