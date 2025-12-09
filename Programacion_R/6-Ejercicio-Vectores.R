nombres <- c(" Ana  ", "lUIS", "mArIa  ", "  PEPE")

# 1) Eliminar espacios al inicio y final
# Esperado: "Ana" , "lUIS" , "mArIa" , "PEPE"
nombres_limpios <- gsub("^\\s+|\\s+$", "", nombres)
nombres_limpios
# 2) Convertir solo primera letra a mayúscula y el resto a minúsculas
# Esperado: "Ana" , "Luis" , "Maria" , "Pepe"
nombres_formateados <- paste0(
  toupper(substring(nombres_limpios, 1, 1)),
  tolower(substring(nombres_limpios, 2))
)
nombres_formateados
# 3) Calcular longitud de cada nombre
# Esperado: 3 , 4 , 5 , 4
nchar(nombres_formateados)


productos <- c(
  "ID23: manzana roja, precio = 1.25",
  "ID45: pera verde, precio = 0.99",
  "ID67: melón dulce, precio = 3.40",
  "ID12: fresa, precio = 2.10"
)

# 1) Extraer el ID numérico
# Esperado: "23", "45", "67", "12"
# Con substring toma los primeros 5 caracteres de cada texto.
# Con gsub elimina todo lo que no sea un dígito.
id <- substring(productos, 1, 5)
id <- gsub("[^0-9]", "", id)
id

# 2) Extraer el nombre de la fruta
# Esperado: "manzana roja", "pera verde", "melón dulce", "fresa"
# Eliminar el ID
# Eliminar todo desde la coma en adelante
fruta <- sub("ID[0-9]+: ?", "", productos)
fruta <- sub(",.*", "", fruta)
fruta

# 3) Extraer el precio y convertirlo a numérico
# Esperado: 1.25 , 0.99 , 3.40 , 2.10
# Eliminar el ID
# Elimina todo lo que no sea dígitos o punto decimal
# Convertir a numerico
precio <- sub("ID[0-9]+: ?", "", productos)
precio <- gsub("[^0-9\\.]", "", precio)
precio <- as.numeric(precio)
precio

# 4) Seleccionar productos cuyo precio sea > 2
# Esperado: los elementos con precio 3.40 y 2.10
productos_caros <- productos[precio > 2]
productos_caros
