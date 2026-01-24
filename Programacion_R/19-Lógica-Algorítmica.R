# Creamos la función clasificar_temperatura()
clasificar_temperatura <- function(t) {
  
  # Si la temperatura es menor que 0 → congelación
  if (t < 0) {
    return("congelación")
    
    # Si t es mayor o igual a 0 Y menor que 20 → fría
  } else if (t >= 0 & t < 20) {
    return("fría")
    
    # Si t es mayor o igual a 20 Y menor que 30 → templada
  } else if (t >= 20 & t < 30) {
    return("templada")
    
    # Si t es mayor o igual a 30 → caliente
  } else {
    return("caliente")
  }
}

clasificar_temperatura(-5)
clasificar_temperatura(12)
clasificar_temperatura(25)
clasificar_temperatura(31)