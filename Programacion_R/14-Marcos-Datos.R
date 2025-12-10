# Creamos un pequeño data frame con 5 filas
df <- data.frame(
  nombre = c("Ana", "Luis", "Sara", "Leo", "Nora"),
  edad   = c(23, 31, 19, 45, 28),
  nota   = c(8.5, 7.2, 9.1, 6.8, 7.9)
)

df

# Mostramos las primeras 6 filas (por defecto)
head(df)

# Mostramos las primeras 3 filas
head(df, 3)

tail(df)

# Mostramos las últimas 2 filas
tail(df, 2)

# Estructura del data frame
str(df)

# Resumen descriptivo
summary(df)

# Número de filas del data frame
nrow(df)

# Número de columnas del data frame
ncol(df)

# Mostramos los nombres de columnas
colnames(df)

# Cambiamos los nombres de columnas
colnames(df) <- c("NOMBRE", "EDAD", "NOTA")

# Mostramos los nombres de filas
rownames(df)

# Cambiamos los nombres de filas
rownames(df) <- paste0("Fila", 1:5)
rownames(df)

# Filas donde la edad es mayor que 25
subset(df, EDAD > 25)

# Filas donde la nota sea mayor o igual que 8
subset(df, NOTA >= 8)

# Seleccionar columnas específicas
subset(df, select = c(NOMBRE, NOTA))

# Añadimos una columna nueva: aprobado (TRUE/FALSE)
df2 <- cbind(df, aprobado = df$NOTA >= 7)
df2

df2 <- cbind(df, siempre1 = 1)
df2

# Creamos una fila nueva como data frame
nueva_fila <- data.frame(
  NOMBRE = "Mario",
  EDAD   = 30,
  NOTA   = 8.3
)

# Añadimos la nueva fila al final
df3 <- rbind(df, nueva_fila)
df3

# Creamos un segundo data frame con una columna en común
df_extra <- data.frame(
  NOMBRE = c("Ana", "Sara", "Leo"),
  ciudad = c("Madrid", "Valencia", "Sevilla")
)

df_extra

# Unimos los dos data frames por la columna NOMBRE
df_merged <- merge(df3, df_extra, by = "NOMBRE")
df_merged

# Convertimos una matriz en data frame
mat <- matrix(1:6, nrow = 3)
as.data.frame(mat)
