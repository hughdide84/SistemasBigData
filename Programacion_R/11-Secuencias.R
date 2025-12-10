# Generamos una secuencia simple del 1 al 10
1:10

# Generamos una secuencia del 5 al 20 disminuyendo de 1 en 1
20:5

# Creamos una secuencia desde 0 hasta 10 incrementando de 2 en 2
seq(from = 0, to = 10, by = 2)

# Creamos una secuencia desde 1 hasta 2 incrementando de 0.1 en 0.1
seq(from = 1, to = 2, by = 0.1)

# Generamos una secuencia entre 0 y 1 con 5 elementos equiespaciados
seq(from = 0, to = 1, length.out = 5)

# Repetimos el vector c(1, 2, 3) tres veces
rep(c(1, 2, 3), times = 3)

# Repetimos cada valor de c(10, 20) cinco veces antes de pasar al siguiente
rep(c(1, 2, 3), each = 3)

# Creamos un vector de ejemplo
v <- c(10, 20, 30, 40)

# Generamos una secuencia desde 1 hasta la longitud del vector v
seq_along(v)   # Resultado: 1 2 3 4

# Generamos una secuencia desde 1 hasta n = 6
seq_len(6)