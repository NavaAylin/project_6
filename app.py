import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('C:\\Users\\aylin\\OneDrive\\Documentos\\Proyectos_VS_Python_Jupyter\\project_6\\dataset\\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
#la siguiente línea la cree YO
scatter_button=st.button('Construir diagrama de dispersión')
        
if hist_button: # al hacer clic en el botón
    st.header('Histograma principal', divider='blue')        # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scatter_button:
    st.header('Diagrama de dispersion principal', divider='red')        # escribir un mensaje
    st.write('Creación de un Diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig1 = px.scatter(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)