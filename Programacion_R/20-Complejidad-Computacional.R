
# Tiempos sort
v <- runif(1000000, min = 1, max = 20)
print(system.time(sort(v))[3])
v <- runif(2000000, min = 1, max = 20)
print(system.time(sort(v))[3])
v <- runif(4000000, min = 1, max = 20)
print(system.time(sort(v))[3])
# Complejidad teórica O(n log n)


# Tiempos unique
v <- runif(1000000, min = 1, max = 20)
print(system.time(unique(v))[3])
v <- runif(2000000, min = 1, max = 20)
print(system.time(unique(v))[3])
v <- runif(4000000, min = 1, max = 20)
print(system.time(unique(v))[3])
# Complejidad teórica O(n)


# Tiempos in
v <- runif(10000000, min = 1, max = 20)
print(system.time(0.5 %in% v)[3])
v <- runif(20000000, min = 1, max = 20)
print(system.time(0.5 %in% v)[3])
v <- runif(40000000, min = 1, max = 20)
print(system.time(0.5 %in% v)[3])
# Complejidad teórica 0(n)

# Tiempos min
v <- runif(10000000, min = 1, max = 20)
print(system.time(min(v))[3])
v <- runif(20000000, min = 1, max = 20)
print(system.time(min(v))[3])
v <- runif(40000000, min = 1, max = 20)
print(system.time(min(v))[3])
# Complejidad teórica 0(n)


# Tiempos order
v <- runif(10000000, min = 1, max = 20)
print(system.time(order(v))[3])
v <- runif(20000000, min = 1, max = 20)
print(system.time(order(v))[3])
v <- runif(40000000, min = 1, max = 20)
print(system.time(order(v))[3])
# Complejidad teórica O(n log n)