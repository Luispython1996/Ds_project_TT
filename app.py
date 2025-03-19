import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv("dataset/vehicles_us.csv")  # Ajusta la ruta si es necesario

# Crear la interfaz de la app
st.title("Exploración de Datos de Vehículos en EE.UU.")  # Título principal

# Mostrar el DataFrame
st.subheader("Vista previa de los datos")
st.write(car_data.head())

# Crear opciones para seleccionar variables para histogramas y gráficos de dispersión
st.subheader("Selecciona una variable para visualizar")

column = st.selectbox("Selecciona una columna numérica", ["price", "odometer", "days_listed"])

# Agregar casillas de verificación para seleccionar el tipo de gráfico
build_histogram = st.checkbox("Construir un histograma")
build_scatter = st.checkbox("Construir un gráfico de dispersión")

# Construir histogramas si la casilla está activada
if build_histogram:
    st.write(f"Construyendo histograma para la columna {column}")
    fig = px.histogram(car_data, x=column, title=f"Distribución de {column}")
    st.plotly_chart(fig)

# Construir gráficos de dispersión si la casilla está activada
if build_scatter:
    st.write(f"Construyendo gráfico de dispersión para {column} vs price")
    fig = px.scatter(car_data, x=column, y="price", title=f"Relación entre {column} y price")
    st.plotly_chart(fig)
