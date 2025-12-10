# Creamos una lista con distintos tipos de elementos
x <- list(
  numeros = c(1, 2, 3),
  texto = "Hola",
  logico = TRUE,
  matriz = matrix(1:4, nrow = 2)
)
x

# Obtenemos cuántos elementos contiene la lista
length(x)

# Consultamos los nombres actuales de los elementos
names(x)

# Asignamos nuevos nombres a los elementos de la lista
names(x) <- c("nums", "saludo", "flag", "mat")

# Verificamos los nuevos nombres
x
names(x)

# Mostramos la estructura interna de la lista de forma compacta
str(x)

# Comprobamos si x es una lista
is.list(x)

# Comprobamos si un vector NO es una lista
is.list(c(1, 2, 3))

# Convertimos un vector en una lista
as.list(1:5)

# Añadimos un nuevo elemento al final de la lista
x <- append(x, list(nuevo = "Elemento agregado"))
x

# Convertimos una lista simple en vector
lista_simple <- list(1, 2, 3, 4)
v <- unlist(lista_simple)
v
is.list(v)

# Atención: si hay tipos distintos, devuelve vector “mezclado”
unlist(list(1, "hola", TRUE))
