# Vector base con nombres
x <- c(5, 10, 15, 20, 25, 30, 35)
names(x) <- c("Ana", "Paco", "Juan", "Lucia", "Juan", "Perico", "Pepe")

# 1) x[n] → elemento en la posición 3
# Esperado: 15
x[3]

# 2) x[-n] → vector sin la posición 3
# Esperado: 5, 10, 20, 25, 30, 35 (sin 15)
x[-3]

# 3) x[1:n] → posiciones de 1 a 4
# Esperado: 5, 10, 15, 20
x[1:4]

# 4) x[a:b] → posiciones de 3 a 6
# Esperado: 15, 20, 25, 30
x[3:6]

# 5) x[-(1:n)] → excluir posiciones 1 y 2
# Esperado: 15, 20, 25, 30, 35
x[-(1:2)]

# 6) x[-(a:b)] → excluir posiciones 3 a 5
# Esperado: 5, 10, 30, 35
x[-(3:5)]

# 7) x[c(a,b,c)] → posiciones 1, 4 y 7
# Esperado: 5, 20, 35
x[c(1,4,7)]

# 8) x[x > 15] → elementos mayores que 15
# Esperado: 20, 25, 30, 35
x2 <- x[x > 15]
x2

# 9) x[x > 10 & x < 30] → mayores que 10 y menores que 30
# Esperado: 15, 20, 25
x[x > 10 & x < 30]

# 10) x["cuatro"] → seleccionar por nombre
# Esperado: 20
x["Juan"]
