# Asignamos el valor 4 al objeto numero1
numero1 <- 4

# Verificamos si numero1 es de tipo entero
is.integer(numero1)

# Verificamos si numero1 es un valor numérico
is.numeric(numero1)

# Asignamos el valor entero 2 (con sufijo L) a numero2
numero2 <- 2L

# Verificamos si numero2 es de tipo entero
is.integer(numero2)

# Verificamos si numero2 es numérico
is.numeric(numero2)

# Convertimos numero2 a numérico y comprobamos si es entero
is.integer(as.numeric(numero2))

# Obtenemos el valor máximo entre numero1 y numero2
max(numero1, numero2)

# Obtenemos el valor mínimo entre numero1 y numero2
min(numero1, numero2)