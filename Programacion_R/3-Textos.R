# Asignamos una cadena de texto a nombre1
nombre1 <- "Hermenegildo"

# Contamos el número de caracteres en nombre1
nchar(nombre1)

# Convertimos nombre1 a mayúsculas
toupper(nombre1)

# Convertimos nombre1 a minúsculas
tolower(nombre1)

# Extraemos los caracteres desde la posición 2 a la 3
substr(nombre1, 2, 3)

# Extraemos caracteres desde la posición 2 a la 3 (función equivalente)
substring(nombre1, 2, 3)

# Extraemos los caracteres desde la posición 2 hasta el final
substring(nombre1, 2)

# Extraemos rangos múltiples con posiciones iniciales y finales vectorizadas
substring(nombre1, first = c(1, 3, 5), last = c(2, 5, 6))

# Asignamos una cadena a apellido1
apellido1 <- "Costa"

# Unimos nombre y apellido con espacio por defecto
paste(nombre1, apellido1)

# Unimos nombre y apellido sin espacio
paste0(nombre1, apellido1)

# Unimos nombre y apellido agregando un espacio manualmente
paste0(nombre1, " ", apellido1)

# Dividimos el texto usando la letra "e" como separador
strsplit(nombre1, "e")

# Buscamos si el patrón "erme" aparece en nombre1
grepl("erme", nombre1)

# Buscamos si el patrón "hugo" aparece en nombre1
grepl("hugo", nombre1)

# Reemplazamos "ildo" por "ildito" en nombre1
gsub("ildo", "ildito", nombre1)

# Formateamos un mensaje con texto, entero y número real con 1 decimal
sprintf("Hola %s, tienes %d ingreso nuevo, su importe es  %.1f dólares.", "Ana", 1, 1024.1365)

# Imprimimos texto en consola sin salto de línea final
cat("Prueba")
