import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Cargar el dataframe 'df_ml' desde el archivo CSV
df_ml = pd.read_csv('df_ml.csv')

# Seleccionar características de entrada (X) y variable objetivo (y)
X = df_ml[['day_week', 'Hour', 'location_id']]
y = df_ml['optimization']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de Random Forests
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Guardar el modelo en un archivo local
joblib.dump(model, 'modelo_entrenado.joblib')
