# VECTORES
x <- c(1, 2, 3)
y <- c(4, 5, 6)
z <- c(7, 8, 9)

# rbind(x,y,z)  → apilar vectores como filas
rbind(x, y, z)

# cbind(x,y,z)  → unir vectores como columnas
cbind(x, y, z)

# MATRICES
A <- matrix(
  c(1, 2, 3,4, 5, 6,7, 8, 10),
  nrow = 3, ncol = 3, byrow = TRUE
)
A

# A[, c(a,b,c,...)]  → todas las filas, columnas específicas
A[, c(1, 3)]

# A[m,n]  → elemento de la fila m, columna n
A[2, 3]

# A[a:b, c:d]  → submatriz filas a..b y columnas c..d
A[1:2, 2:3]

# A[, c:d]  → todas las filas, columnas c..d
A[, 2:3]

# A[a:b, ]  → filas a..b, todas las columnas
A[1:2, ]


2:9

# A[a, ]  → fila a completa
A[2, ]

# A[, b]  → columna b completa
A[, 3]

# diag(A)  → extrae la diagonal de A
diag(A)

# dim(A)  → dimensiones de la matriz
dim(A)

# colSums(A)  → suma de cada columna
colSums(A)

# rowSums(A)  → suma de cada fila
rowSums(A)

summary(A)
