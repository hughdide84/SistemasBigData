from sklearn.ensemble import IsolationForest
import pandas as pd

# Datos de ejemplo: ventas diarias
datos = {
    "ventas": [100, 105, 98, 102, 110, 108, 500, 103, 99, 95, 20]
}

df = pd.DataFrame(datos)

# Crear modelo
modelo = IsolationForest(
    n_estimators=100,      # número de árboles (más árboles, más lento pero más preciso)
    contamination=0.2,     # proporción esperada de anomalías
    random_state=1
)

# Entrenar y predecir
df["prediccion"] = modelo.fit_predict(df[["ventas"]])

# Interpretación:
#  1  = normal
# -1 = anomalía

print(df)