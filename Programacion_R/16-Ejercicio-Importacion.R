# Importar el archivo con read.csv()
cities <- read.csv("C:\\Users\\docencia\\Downloads\\cities.csv")

# Mostrar las primeras filas
head(cities)

# Obtener nombres de columnas
colnames(cities)

# Inspeccionar la estructura del data frame
str(cities)

# Filtrar filas donde State == " OH" (Ohio)
ohio <- cities[cities$State == " OH", ]
ohio

# Limpiar espacios
cities$City  <- trimws(gsub('"', '', cities$City))
cities$State <- trimws(gsub('"', '', cities$State))

# Filtrar filas donde State == "OH" (Ohio)
ohio <- cities[cities$State == "OH", ]
ohio