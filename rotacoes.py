import streamlit as st
from base import get_xyz

def get_rotacoes():
    cols = st.columns(2)
    cols[0].title("Quantas rotações")
    qnt = cols[1].number_input("Quantidade", min_value=0, step=1, key="QuantidadeRotacoes")

    escolhas = []
    parametros = []

    for i in range(qnt):
        with st.expander(f"Rotação {i}"):
            cols = st.columns([1,1, 5])
            escolha = cols[0].radio("Tipo de Rotação", ["Translação", "Rotação"], key=f"TipodeRotacao{i}")
            escolhas.append(escolha)
            if (escolha == "Translação"): 
                with cols[2]: distancias = get_xyz(key=f"distancias{i}")
                parametros.append(distancias)
            else:
                eixo = cols[1].radio("Eixo", ["X", "Y", "Z"], horizontal=True, key=f"eixo{i}")
                graus = cols[2].number_input("Graus (0->360°)", min_value=0, max_value=360, step=1, key=f'rotacaovalue{i}')
                parametros.append([eixo, graus])

    return [escolhas, parametros]