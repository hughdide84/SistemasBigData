v1 <- c(1, 2, 3)
v2 <- c(4, 5, 6)

A <- matrix(1:6, nrow = 2, byrow = TRUE)
B <- matrix(c(2, 2, 2, 2, 2, 2), nrow = 2)

# OPERADORES ARITMÉTICOS CON VECTORES

# Suma elemento a elemento
v1 + v2

# Resultado: c(5, 7, 9)

# Resta elemento a elemento
v2 - v1

# Multiplicación elemento a elemento
v1 * v2

# División elemento a elemento
v2 / v1

# Potencia elemento a elemento
v1 ^ 2

# Resto de la división elemento a elemento
v2 %% v1

# División entera (cociente sin decimales)
v2 %/% v1

# OPERADORES ARITMÉTICOS CON MATRICES

# Suma de matrices
A + B

# Resta de matrices
A - B

# Multiplicación elemento a elemento (no matricial)
A * B

# División elemento a elemento
A / B

# Potencia elemento a elemento
A ^ 2

# Resto de la división elemento a elemento
A %% B

# División entera elemento a elemento
A %/% B

