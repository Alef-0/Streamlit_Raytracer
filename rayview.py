import streamlit as st
from base import get_xyz

def get_camera():
    origem = get_xyz('camera_origin', "Origem")
    direcao = get_xyz('camera_direction', 'Direção')
    up = get_xyz('Cima', 'Cima')
    
    cols = st.columns(4) # Individuais 
    cols[0].title("Propriedades")
    distancia = cols[1].number_input("Distancia", key='camera_distancia', min_value=0, step=1)
    altura = cols[2].number_input("Altura", key='camera_altura', min_value=50, step=1)
    largura = cols[3].number_input("Largura", key='camera_largura', min_value=50, step=1)
    
    return [origem, direcao, up, distancia, altura, largura]