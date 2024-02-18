import streamlit as st

from rayview import get_camera
from luzes import get_luzes
from esferas import get_esferas
from planos import get_planos
from triangulos import get_triangulos
from rotacoes import get_rotacoes

from base import imprimir

st.set_page_config(layout='wide',)


tabs =  st.tabs(['Camera', 'Luzes', 'Esferas', 'Planos', "Triangulos", "Rotações", "Input"])

with tabs[0]: origem, direcao, up, distancia, altura, largura = get_camera()
with tabs[1]: ambiente_rgb, xyz_luzes, rgb_luzes = get_luzes()
with tabs[2]: esferas_centros, esferas_raios, esferas_phong = get_esferas()
with tabs[3]: planos_pontos, planos_normais, planos_phong = get_planos()
with tabs[4]: pontos, lugares_pontos, triangulo_phong = get_triangulos()
with tabs[5]: escolhas, parametros = get_rotacoes()

# Onde fica o input
in_file = ""
with tabs[6]: 
    in_file = ""
    #Camera
    in_file += f"""{imprimir(origem)}{imprimir(direcao)}{imprimir(up)}{distancia}
{altura} {largura}\n
"""
    # Luzes
    in_file += f"""
{imprimir(ambiente_rgb)}{len(xyz_luzes)}
"""
    for i in range(len(xyz_luzes)):
        in_file += f"{imprimir(xyz_luzes[i])}"
        in_file += f"{imprimir(rgb_luzes[i])}"
    in_file+='\n'
    # Esferas
    in_file += f"{len(esferas_centros)}\n"
    for i in range(len(esferas_centros)):
        in_file += f'{imprimir(esferas_centros[i])}'
        in_file += f'{esferas_raios[i]}\n'
        in_file += f'{imprimir(esferas_phong[i])}'
    in_file += '\n'
    # Planos
    in_file += f'{len(planos_normais)}\n'
    for i in range(len(planos_normais)):
        in_file += f'{imprimir(planos_pontos[i])}'
        in_file += f'{imprimir(planos_normais[i])}'
        in_file += f'{imprimir(planos_phong[i])}'
    in_file += '\n'
    # triangulos
    in_file += f'{len(lugares_pontos)}\n'
    if (len(lugares_pontos)): in_file += f'{len(pontos)}\n'
    for i in range(len(pontos)):
        in_file += f'{imprimir(pontos[i])}'
    for i in range(len(lugares_pontos)):
        in_file += f'{pontos.index(lugares_pontos[i][0])} {pontos.index(lugares_pontos[i][1])} {pontos.index(lugares_pontos[i][2])}\n'
        in_file += f'{imprimir(triangulo_phong[i])}'
    in_file += '\n'
    # Rotações
    for i in range(len(escolhas)):
        in_file += 'Y\n'
        if len(parametros[i]) == 3:
            in_file += f'T {parametros[i][0]} {parametros[i][1]} {parametros[i][2]}\n'
        else:
            in_file += f'R {parametros[i][0]} {parametros[i][1]}\n'
    in_file += 'N'

    st.code(in_file)