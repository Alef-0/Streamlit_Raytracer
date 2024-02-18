import streamlit as st
from base import get_xyz,get_phong

def get_esferas():
    cols = st.columns(2)
    cols[0].title("Quantas Esferas?")
    qnt = cols[1].number_input("Quantidade", min_value=0, step=1, key="esferasQuantidade")

    esferas_centros = []
    esferas_raios = []
    esferas_phong = []

    for i in range(qnt):
        with st.expander(f'Esferas {i}', expanded=False):
            centro = get_xyz(f"Centroesfera{i}", 'Centro')
            colunas = st.columns([1, 3])
            colunas[0].title("Raio")
            raio = colunas[1].number_input("Raio", key=f"Raioesfera{i}", min_value=0)
            phong = get_phong(f"Phongesfera{i}")
        esferas_centros.append(centro)
        esferas_raios.append(raio)
        esferas_phong.append(phong)
    
    return [esferas_centros, esferas_raios, esferas_phong]
    