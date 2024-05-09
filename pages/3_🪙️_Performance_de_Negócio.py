import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = st.session_state["data3"]
df_test = st.session_state["data4"]

x_price = df_test.pivot(index='Week_Number', columns='name', values='disc_price')
x_price = pd.DataFrame(x_price.to_records())



def calcular_desempenho(df, produto, percentual_desconto):
    for index, row in df.iterrows():
        if row['name'] == produto:
            preco_atual_medio = x_price[row['name']].mean()
            demanda_atual = x_price[row['name']].sum()

            preco_redu = preco_atual_medio * (1 - percentual_desconto / 100)
            demanda_aumento = row['price_elastic'] * (percentual_desconto / 100)
            demanda_nova = demanda_aumento * demanda_atual
            faturamento_atual = round(preco_atual_medio * demanda_atual, 2)
            novo_faturamento = round(preco_redu * demanda_nova, 2)

            faturamento_reduzido = round(faturamento_atual * (1 - percentual_desconto / 100), 2)
            perda_faturamento = round(faturamento_atual - faturamento_reduzido, 2)
            variacao_faturamento = round(novo_faturamento - faturamento_atual, 2)
            variacao_percentual = round(((novo_faturamento - faturamento_atual) / faturamento_atual), 2)

            st.write(f'O faturamento atual para o produto "{produto}" é R$ {round(faturamento_atual, 2)}, com a redução de {percentual_desconto}% sugerida seria R$ {round(faturamento_reduzido, 2)}, portanto diminuiria R$ {round(perda_faturamento, 2)}.')
            st.write(f'Mas com o aumento da demanda devido à redução, o faturamento seria R$ {round(novo_faturamento, 2)}, gerando um incremento de R$ {round(variacao_faturamento, 2)} ou {round(variacao_percentual * 100, 2)}% no faturamento.')

# Interface do Streamlit
st.sidebar.title("Configurações")
produtos = df['name'].tolist()
produto_escolhido = st.sidebar.selectbox("Escolha um Produto", produtos)
percentual_desconto = st.sidebar.slider("Porcentagem de Desconto", min_value=0, max_value=100, value=10, step=1)
# Calcular desempenho com base no produto e desconto escolhidos pelo usuário
calcular_desempenho(df, produto_escolhido, percentual_desconto)