import streamlit as st
from base import get_xyz, get_phong

def get_triangulos():
    st.title("Erros podem ocorrer se não setar os vértices corretamente")
    # Pegar pontos
    cols = st.columns(2)
    cols[0].title("Quantos Pontos?")
    qnt_pontos = cols[1].number_input("Quantidade", min_value=0, step=1, key="triangulopontosquantidade")
    
    pontos = []
    with st.expander("Lista de Pontos"):
        for i in range(qnt_pontos):
            ponto = get_xyz(f'ponto{i}')
            pontos.append(ponto)
    
    # Pegar triangulos
    cols = st.columns(2)
    cols[0].title("Quantos Triangulos?")
    qnt_triangulos = cols[1].number_input("Quantidade", min_value=0, step=1, key="trianguloquantidade")

    lugares_pontos = []
    triangulo_phong = []

    for i in range(qnt_triangulos):
        with st.expander(f"Triangulo {i}"):
            pnts = st.multiselect("Pontos", pontos, key=f"selecao{i}", max_selections=3, placeholder="Selecione os vertices")
            phong = get_phong(f"phongtriangulos{i}", line=True)
        lugares_pontos.append(pnts)
        triangulo_phong.append(phong)

    return [pontos, lugares_pontos, triangulo_phong]