import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

# Add title
st.header('Gráficos interativos')

# Creates checkbox with to buttons/options
build_histogram = st.checkbox('Criar um Histograma')
build_scatter = st.checkbox('Criar gráfico de Dispersão')

if build_histogram:  # if histogram option is clicked:
    # Write this message
    st.write('Criando um histograma da quantidade de carros conforme a quilometragem registrada no odômetro.')
    # Generating histogram
    fig = px.histogram(car_data, x='odometer',
                       title='Distribuição da Quantidade de Carros pela Quilometragem (km)')
    # Shows interactive Plotly grafic
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # if scatter option is clicked:
    # Write this message
    st.write('Criando gráfico de dispersão que exibe a relação entre quilometragem vs. preço dos carros.')
    # Generating scatter plot
    fig2 = px.scatter(car_data, x='odometer', y='price',
                      title='Quilometragem vs. Preço dos Carros à Venda')
    # Displays interactive Plotly chart
    st.plotly_chart(fig2, use_container_width=True)
