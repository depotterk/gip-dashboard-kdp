# Liquiditeit
# Solvabiliteit
# REV
# Omloopsnelheid van de voorraad
# Klant-en leverancierskrediet
# ACTIVA en PASIVA

import pandas as pd  
import plotly.express as px
import streamlit as st
import excel_jaarrekening as ej
import chart_jaarrekening as cj
boekjaar = ''
# ---- Set Page ----
st.set_page_config(
    page_title="GIP Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"}
    )

# ---- READ EXCEL ACTIVA ----
df_activa = ej.get_activa_from_excel()

# ---- READ EXCEL PASIVA ----
df_pasiva = ej.get_pasiva_from_excel()

# ---- READ EXCEL KlantLevKrediet ----
df_klantlev = ej.get_klantlev_from_excel()

# ---- READ EXCEL LIQUIDITEIT ----
df_liquiditeit = ej.get_liquiditeit_from_excel()

# ---- READ EXCEL SOLVABILITEIT ----
df_solvabiliteit = ej.get_solvabiliteit_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Gelieve hier te filteren:")

charts = st.sidebar.multiselect(
     'Welke grafiek(en) wens je te zien:',
     ['Activa', 'Pasiva', 'Klant-en leverenancierskrediet', 'Liquiditeit', 'Solvabiliteit'],
     ['Activa'])

rawdata = st.sidebar.checkbox('See raw data')
st.sidebar.text('')
# ---- MAINPAGE ----
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.write("")

with col2:
    st.image("data/logo-jules-destrooper-background.png")
    st.write("")
    st.title(":bar_chart: Jaarrekening Dashboard")
    st.markdown("##")
with col3:
    st.write("") 
st.write("")
st.write("")

#----- DRAW CHARTS ----
for chart in charts:
    # ---- SIDEBAR ----
    if (chart in ('Activa','Pasiva') and boekjaar ==''):
        boekjaar = st.sidebar.radio(
            "Selecteer boekjaar:",
            ("Boekjaar 1","Boekjaar 2","Boekjaar 3"),
            index=0
        )
    if chart == 'Activa':
        # Samenstelling activa boekjaar [TAART DIAGRAM]
        fig_activa = cj.create_pie(df_activa, boekjaar, 'ACTIVA', f'Samenstelling activa {boekjaar}')
        st.plotly_chart(fig_activa, use_container_width=True)
        if rawdata:
            st.write(df_activa)

    elif chart == 'Pasiva':     
        # Samenstelling pasiva boekjaar [TAART DIAGRAM]
        fig_pasiva = cj.create_pie(df_pasiva, boekjaar, 'PASSIVA', f'Samenstelling passiva {boekjaar}')
        st.plotly_chart(fig_pasiva, use_container_width=True)
        if rawdata:
            st.write(fig_pasiva)

    elif chart == 'Klant-en leverenancierskrediet':
        # Samenstelling klant- en leverancierskrediet boekjaar [BAR DIAGRAM]
        st.subheader(f'Samenstelling klant- en leverancierskrediet')
        fig_klant_lev = cj.create_bar(df_klantlev, 
            ['Klantenkrediet','Leverancierskrediet','Totaal aantal dagen voorraad+klantenkrediet'],
            'Boekjaar', 'h', 'Klant-en leverenacierskrediet', [0,100], {'value':'Aantal dagen'})
        st.plotly_chart(fig_klant_lev, use_container_width=True)
        if rawdata:
            st.write(fig_klant_lev)

    elif chart == 'Liquiditeit':
        # Samenstelling Liquiditeit boekjaar [AREA CHART]
        st.subheader(f'Samenstelling Liquiditeit')
        fig_liquiditeit = cj.create_line(df_liquiditeit, 'Boekjaar','Liquiditeit','Type') 
        st.plotly_chart(fig_liquiditeit, use_container_width=True)
        if rawdata:
            st.write(df_liquiditeit)
            
    elif chart == 'Solvabiliteit':
        st.subheader(f'Samenstelling Solvabiliteit')
        if rawdata:
            st.write(df_solvabiliteit)
    
#FOOTER

    
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)