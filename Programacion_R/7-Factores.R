# FACTORES

# Crear factor
colores <- factor(c("rojo", "verde", "rojo", "azul"))
colores

# Valores solo
as.character(colores)

# Niveles
levels(colores)

# Puedes indicar qué categorías existen y en qué orden
tallas <- factor(c("M", "L", "S", "M"), levels = c("S", "M", "L"), ordered = TRUE)
tallas

# Ver los valores internos como números
as.numeric(tallas)

# Modificar un nivel
levels(colores)[levels(colores) == "rojo"] <- "rojo_intenso"
colores

# Agregar nivel 
levels(colores) <- c(levels(colores), "amarillo")
colores


