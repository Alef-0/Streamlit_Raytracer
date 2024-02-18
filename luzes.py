import streamlit as st
from base import get_RGB, get_xyz

def get_luzes():
    ambiente_rgb = get_RGB("ambiente", "Luz ambiente")
    
    # Setar multiplas
    cols = st.columns(2)
    cols[0].title("Quantas fontes?")
    qnt = cols[1].number_input("Quantidade", min_value=0, step=1, key="LuzQuantidade")
    
    # Colocar
    rgb_luzes = []
    xyz_luzes = []
    for i in range(qnt):
        with st.expander(f'Luzes {i}', expanded=True):
            cols0, cols1 = st.columns(2)
            with cols0: xyz = get_xyz(f'luzesxyz{i}')
            with cols1: rgb = get_RGB(f'luzesrgb{i}')
        rgb_luzes.append(rgb)
        xyz_luzes.append(xyz)
    
    return [ambiente_rgb, xyz_luzes, rgb_luzes]
