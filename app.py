import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv') # lendo os dados

# criar checkbox para o histograma
if st.checkbox('Mostrar histograma do odômetro'):
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar checkbox para o gráfico de dispersão
if st.checkbox('Mostrar gráfico de dispersão (preço vs odômetro)'):
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão: preço vs odômetro')
    
    # criar o gráfico de dispersão
    fig2 = px.scatter(car_data, x="odometer", y="price", color="condition")
    
    # exibir o gráfico Plotly interativo
    st.plotly_chart(fig2, use_container_width=True)