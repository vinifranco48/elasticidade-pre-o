import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

if 'data1' not in st.session_state:
    df_data1 = pd.read_csv('dados/priceelastic.csv')  
    st.session_state['data1'] = df_data1

if 'data2' not in st.session_state:
    df_data2 = pd.read_csv('dados/crossprice.csv')  
    st.session_state['data2'] = df_data2

if 'data3' not in st.session_state:
    df_data3 = pd.read_csv('dados/order_price.csv')  
    st.session_state['data3'] = df_data3

if 'data4' not in st.session_state:
    df_data4 = pd.read_csv('dados/test.csv')  
    st.session_state['data4'] = df_data4


st.sidebar.markdown('Desenvolvido por [Vinicius](https://www.linkedin.com/in/vinicius-franco-720558228/)')

tab1, tab2 = st.tabs(['Elasticidade de preço', 'Grafico de elasticidade'])
def divergent_plot(df, values_column, ylabel, xlabel):
    # Divergent plot
    df['ranking'] = df[values_column].rank(ascending=True).astype(int)
    df.sort_values(values_column, ascending=False, inplace=True)
    
    fig, ax = plt.subplots(figsize=(12, 5), dpi=80)
    ax.set_facecolor('none')  

    # Plot das linhas com cor cinza e maior nitidez
    ax.hlines(y=df['ranking'], xmin=0, xmax=df[values_column], color='gray', linewidth=3)
    
    # Adicionar rótulos de elasticidade
    for x, y, tex in zip(df[values_column], df['ranking'], df[values_column]):
        ax.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':10})
    
    # Adicionar linhas pontilhadas no fundo do gráfico
    ax.xaxis.grid(True, linestyle='--', alpha=0.5)  # Linhas pontilhadas verticais
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)  # Linhas pontilhadas horizontais
    
    # Configurações dos eixos e título
    ax.set(ylabel=ylabel, xlabel=xlabel)
    ax.yaxis.set_tick_params(width=2)  # Aumentar a nitidez dos ticks no eixo y
    plt.title(values_column, fontdict={'size':13})

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

with tab1:
    df_data1
with tab2:
    divergent_plot(df_data1,'price_elastic','Ranking Number', 'Price Elasticity' )