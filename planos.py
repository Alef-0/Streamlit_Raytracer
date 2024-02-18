import streamlit as st
from base import get_phong, get_xyz

def get_planos():
    cols = st.columns(2)
    cols[0].title("Quantos planos?")
    qnt = cols[1].number_input("Quantidade", min_value=0, step=1, key='planosquantidade')
    # Alinhar
    planos_pontos = []
    planos_normais = []
    planos_phong = []

    for i in range(qnt):
        with st.expander(f"Plano {i}", expanded=False):
            ponto = get_xyz(f"planoponto{i}", "Ponto")
            normal = get_xyz(f'planonormal{i}', "Normal")
            phong = get_phong(f"panophong{i}")
        planos_pontos.append(ponto)
        planos_normais.append(normal)
        planos_phong.append(phong)

    return [planos_pontos, planos_normais, planos_phong]