# Creamos un array con números del 1 al 12, con dimensiones 3x2x2
arr <- array(1:12, dim = c(3, 2, 2))
arr

# Obtenemos las dimensiones del array (3 filas, 2 columnas, 2 capas)
dim(arr)

# Cambiamos las dimensiones del array a 2x2x3
dim(arr) <- c(2, 2, 3)
arr

# Obtenemos el número total de elementos (siempre producto de las dimensiones)
length(arr)

# Asignamos nombres a filas, columnas y capas
dimnames(arr) <- list(
  Filas = c("F1", "F2"),
  Columnas = c("C1", "C2"),
  Capas = c("K1", "K2", "K3")
)
arr

# Calculamos la suma por FILAS (margin = 1)
apply(arr, 1, sum)

# Calculamos la suma por COLUMNAS (margin = 2)
apply(arr, 2, sum)

# Calculamos la suma por CAPAS (margin = 3)
apply(arr, 3, sum)
