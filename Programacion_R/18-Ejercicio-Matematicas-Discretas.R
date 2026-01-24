# Creamos los vectores de estudiantes de cada taller
taller_A <- c("Hugo", "Pepe", "Rodrigo", "Ana", "Lucía")
taller_B <- c("Oscar", "Pepe", "Marcos", "Rebeca", "Lucía")

# Obtenemos todos los estudiantes presentes en A o B
union(taller_A, taller_B)

# Obtenemos los estudiantes que están en A y también en B
intersect(taller_A, taller_B)

# Diferencia: elementos de A que no aparecen en B
setdiff(taller_A, taller_B)

# Diferencia: elementos de B que no aparecen en A
setdiff(taller_B, taller_A)
