import streamlit as st

def get_xyz(key, label = '', phong = False):
    if phong:
        col0, col1, col2, col3 = st.columns([6, 5,5,5], gap='small')
        col0.title(label)
        x = col1.number_input("R", key=key+'r', step=0.01, min_value=0.0, max_value=1.0)
        y = col2.number_input("G", key=key+'g', step=0.01, min_value=0.0, max_value=1.0)
        z = col3.number_input("B", key=key+'b', step=0.01, min_value=0.0, max_value=1.0)
    elif len(label) > 0:
        col0, col1, col2, col3 = st.columns([6,5,5,5], gap='small')
        col0.title(label)
        x = col1.number_input("X", key=key+'x', step=0.1)
        y = col2.number_input("Y", key=key+'y', step=0.1)
        z = col3.number_input("Z", key=key+'z', step=0.1)
    else:
        col1, col2, col3 = st.columns(3, gap='small')
        x = col1.number_input("X", key=key+'x', step=0.1)
        y = col2.number_input("Y", key=key+'y', step=0.1)
        z = col3.number_input("Z", key=key+'z', step=0.1)
    return [x,y,z]

def get_RGB(key, label = ''):
    if len(label) > 0:
        col0, col1, col2, col3 = st.columns(4, gap='small')
        col0.title(label)
        x = col1.number_input("R", key=key+'r', step=1, min_value=0, max_value=255)
        y = col2.number_input("G", key=key+'g', step=1, min_value=0, max_value=255)
        z = col3.number_input("B", key=key+'b', step=1, min_value=0, max_value=255)
    else:
        col1, col2, col3 = st.columns(3, gap='small')
        x = col1.number_input("R", key=key+'r', step=1, min_value=0, max_value=255)
        y = col2.number_input("G", key=key+'g', step=1, min_value=0, max_value=255)
        z = col3.number_input("B", key=key+'b', step=1, min_value=0, max_value=255)
    return [x,y,z]

def get_phong(key, label = '', line = False):
    ka = get_xyz("phong" + key + 'ka',label='ka', phong=True)
    kd = get_xyz("phong" + key + 'kd',label='kd', phong=True)
    ke = get_xyz("phong" + key + 'ke',label='ke', phong=True)
    cols = st.columns(2)
    cols[0].title("Rugosidade")
    N = cols[1].number_input("Rugosidade", min_value=0, step=10, key = key+'N')
    kr = get_xyz("phong" + key + 'kr',label='kr', phong=True)
    kt = get_xyz("phong" + key + 'kt',label='kt', phong=True)
    cols = st.columns(2)
    cols[0].title("IOR")
    IOR = cols[1].number_input("IOR", min_value=0.0, step=0.1, key = key +'IOR')
    return [ka, kd, ke, N, kr, kt, IOR]

def imprimir(vector):
    if len(vector) == 3:
        return f"{vector[0]} {vector[1]} {vector[2]}\n"
    else: #phong
        return f'''{vector[0][0]} {vector[0][1]} {vector[0][2]}
{vector[1][0]} {vector[1][1]} {vector[1][2]}
{vector[2][0]} {vector[2][1]} {vector[2][2]}
{vector[3]}
{vector[4][0]} {vector[4][1]} {vector[4][2]}
{vector[5][0]} {vector[5][1]} {vector[5][2]}
{vector[6]}
'''

