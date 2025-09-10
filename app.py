import pandas as pd
import streamlit as st

url = 'https://github.com/CamiloRtt-eng/BugCamp/raw/refs/heads/main/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding= 'utf-8')

st.title('Datos Generales Ficticios')
st.dataframe(df)

#Crear la tabla con las columnas seleccionadas y fecha
seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
#Extraer la fecha sin hora
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

st.dataframe(df)

#Analisis de datos

df_serie_tiempo = df.copy()

#Calculo de municipios con mas delitos
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CONSTRUIR LA PAGINA
st.set_page_config(page_title="Dasboard de Delitos - Fiscalia", layout="centered")
# St.header("Dashboard de Delitos - Fiscalia")
st.header("Dasborard de Delitos  - Fiscalia")
# st.markdown(f'<center><h2>Dashboard de Delitos - Fiscalia</h2></center>', unsafe_allow_html)
st.dataframe(df)

#st.markdown(f"<h3>Municipios con más delitos: {max_municipio}</h3>", unsafe_allow_html=True)
#st.markdown(f"<h3>Cantidad de Delitos: {max_cantidad_delitos}</h3>", unsafe_allow_html=True)

st.subheader("Tipo de Delito")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)