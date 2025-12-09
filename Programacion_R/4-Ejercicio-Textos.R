# EJERCICIO 1
x <- "Programación en R"
# Obtén el número de caracteres.
nchar(x)
# Convierte todo a mayúsculas.
toupper(x)
# Convierte solo la palabra “Programación” a minúsculas usando substr().
x2 <- x
substr(x2, 1, 13) <- tolower(substr(x2, 1, 13))
x2


# EJERCICIO 2
nombre <- "Hermenegildo"
# Usa substr() para extraer "negi".
substr(nombre, 6, 9)
# Usa substring() para obtener cada letra desde posiciones 1, 3, 5.
substring(nombre, first = c(1,3,5), last = c(1,3,5))
# Convierte las 4 primeras letras a mayúsculas usando substr().
nombre2 <- nombre
substr(nombre2, 1, 4) <- toupper(substr(nombre2, 1, 4))
nombre2


# EJERCICIO 3
texto <- "El coche es rojo y el coche es rápido"
# Usa grepl() para comprobar si aparece la palabra "rojo".
grepl("rojo", texto)
# Usa gsub() para reemplazar "coche" por "auto".
gsub("coche", "auto", texto)
# Reemplaza solo la primera vez "auto" por "vehículo".
texto2 <- gsub("coche", "auto", texto)
sub("auto", "vehículo", texto2)

# EJERCICIO 4
dni <- "12345678a"
# Convierte la letra final a mayúsculas.
dni2 <- dni
substr(dni2, 9, 9) <- toupper(substr(dni2, 9, 9))
dni2
# Comprueba con grepl() si la cadena tiene exactamente 8 dígitos seguidos de 1 letra.
valido <- grepl("^[0-9]{8}[A-Za-z]$", dni2)
valido
# Construye un mensaje con sprintf() indicando si el formato es válido.
sprintf("El DNI %s tiene un formato %s",dni2,if (valido) "válido" else "no válido")


