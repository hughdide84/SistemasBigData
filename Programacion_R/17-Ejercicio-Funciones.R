# Creamos la función clasificar_numeros()
clasificar_numeros <- function(x) {
  
  # Creamos un vector vacío donde guardaremos los resultados
  resultado <- character(length(x))
  
  # Recorremos cada elemento del vector con un bucle for
  for (i in 1:length(x)) {
    
    # Si el número es negativo
    if (x[i] < 0) {
      resultado[i] <- "negativo"
      
      # Si el número es igual a cero
    } else if (x[i] == 0) {
      resultado[i] <- "cero"
      
      # Si es mayor que cero
    } else {
      resultado[i] <- "positivo"
    }
  }
  
  # Devolvemos el vector con las clasificaciones
  return(resultado)
}

clasificar_numeros(c(-5, 0, 20))
