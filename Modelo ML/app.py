import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado desde un archivo local
model = joblib.load('modelo_entrenado.joblib')

# Cargar el dataframe 'df_ml' desde el archivo CSV
df_ml = pd.read_csv('df_ml.csv')

# Función para obtener los 5 mejores location_id
def get_top_5_location_id(date, hour, model, df_ml):
    # Convertir la fecha a day_week
    date = pd.to_datetime(date)
    day_week = date.dayofweek

    # Crear un DataFrame con todas las combinaciones de location_id, day_week, y Hour
    unique_locations = df_ml['location_id'].unique()
    test_data = pd.DataFrame({
        'location_id': unique_locations,
        'day_week': [day_week] * len(unique_locations),
        'Hour': [hour] * len(unique_locations)
    })

    # Reordenar las columnas de test_data para coincidir con el orden de características utilizado durante el entrenamiento
    test_data = test_data[['day_week', 'Hour', 'location_id']]

    # Predecir el valor de optimization para todas las combinaciones
    predictions = model.predict(test_data)

    # Añadir las predicciones al DataFrame
    test_data['optimization'] = predictions

    # Ordenar el DataFrame por la columna optimization en orden descendente
    test_data_sorted = test_data.sort_values(by='optimization', ascending=False)

    # Seleccionar los 5 mejores location_id
    top_5_locations = test_data_sorted.head(5)['location_id']

    # Retornar los 5 mejores location_id
    return list(top_5_locations)

# Configurar Streamlit
st.title('Aplicación Streamlit de NYC Taxis y Optimización')

# Ingreso de datos para realizar predicciones
st.subheader('Predicción de los 5 mejores location_id')
date_input = st.date_input('Selecciona una fecha:')
hour_input = st.number_input('Introduce una hora (0-23):', min_value=0, max_value=23, step=1)

# Agregar un botón 'Predecir'
if st.button('Predecir'):
    # Si el botón se presiona, realizar la predicción
    top_5_locations = get_top_5_location_id(date_input, hour_input, model, df_ml)
    st.write('Los 5 mejores location_id son:')
    st.write(top_5_locations)
