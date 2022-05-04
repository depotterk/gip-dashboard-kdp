import pandas as pd  
import streamlit as st



# ---- READ EXCEL ACTIVA ----
@st.cache
def get_activa_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=100,
        header=2
    )

    # filter row on column value
    activa = ["VASTE ACTIVA","VLOTTENDE ACTIVA"]
    df = df[df['ACTIVA'].isin(activa)]

    return df

# ---- READ EXCEL PASIVA ----
@st.cache
def get_pasiva_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=100,
        header=50
    )

    # filter row on column value
    passiva = ["EIGEN VERMOGEN","VOORZIENINGEN EN UITGESTELDE BELASTINGEN","SCHULDEN"]
    df = df[df['PASSIVA'].isin(passiva)]

    return df

# ---- READ EXCEL KlantLevKrediet ----
@st.cache
def get_klantlev_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="KlantLevKrediet",
        usecols="A:D",
        nrows=40
    )
    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    
    # filter row on column value
    krediet = ["Klantenkrediet","Leverancierskrediet","Totaal aantal dagen voorraad+klantenkrediet"]
    df = df[df["Type"].isin(krediet)]
    

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"0","Boekjaar 2":"1",
                    "Boekjaar 3":"2"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Klantenkrediet","Leverancierskrediet","Totaal aantal dagen voorraad+klantenkrediet"] # change column names
    df = df.astype({'Klantenkrediet': 'float64','Leverancierskrediet': 'float64','Totaal aantal dagen voorraad+klantenkrediet':'float64'})
    df = df.round({"Klantenkrediet":2, "Leverancierskrediet":2,"Totaal aantal dagen voorraad+klantenkrediet":2})
    
    
    
    return df

# ---- READ EXCEL LIQUIDITEIT ----
@st.cache
def get_liquiditeit_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="Liquiditeit",
        usecols="A:D",
        nrows=20,
        skiprows=1
    )

    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    liquiditeit = ["Liquiditeit in ruime zin","Liquiditeit in enge zin"]
    df = df[df["Type"].isin(liquiditeit)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.insert(1,"Liquiditeit",["Liquiditeit in ruime zin","Liquiditeit in ruime zin",
                    "Liquiditeit in ruime zin"],True)                
    df.columns = ["Boekjaar","Liquiditeit","Liquiditeit in ruime zin","Liquiditeit in enge zin"] # change column names

    for i in range(3):
        df = df.append({'Boekjaar':df['Boekjaar'][i],
            'Liquiditeit':'Liquiditeit in enge zin',
            'Liquiditeit in ruime zin':df['Liquiditeit in enge zin'][i], 
            'Liquiditeit in enge zin':''}, 
            ignore_index = True)        
    # Remove columns as index base
    df.drop(df.columns[[3]], axis = 1, inplace = True)
    df.columns = ["Boekjaar","Type","Liquiditeit"] # change column names
    df = df.astype({'Boekjaar':'string','Type':'string','Liquiditeit': 'float64'})
        
    return df

# ---- READ EXCEL SOLVABILITEIT ----
@st.cache
def get_solvabiliteit_from_excel():
    df = pd.read_excel(
        io="data/Jules Destrooper oplossing.xlsx",
        engine="openpyxl",
        sheet_name="Solvabiliteit",
        usecols="A:K",
        nrows=4
    )
    vreemdv = {'Unnamed: 0': df['Unnamed: 7'][0], 'Boekjaar1': df['Boekjaar1.1'][0], 'Boekjaar2': df['Boekjaar2.1'][0],
        'Boekjaar3': df['Boekjaar3.1'][0], 'Unnamed: 4':'', 'Unnamed: 5':'', 'Unnamed: 6':'', 'Unnamed: 7':'', 'Boekjaar1.1':'', 'Boekjaar2.1':'', 'Boekjaar3.1':''}
    df = df.append(vreemdv, ignore_index = True)
    solvav = {'Unnamed: 0': 'Solvabiliteit vreemd vermogen', 'Boekjaar1': df['Boekjaar1.1'][2], 'Boekjaar2': df['Boekjaar2.1'][2],
        'Boekjaar3': df['Boekjaar3.1'][2], 'Unnamed: 4':'', 'Unnamed: 5':'', 'Unnamed: 6':'', 'Unnamed: 7':'', 'Boekjaar1.1':'', 'Boekjaar2.1':'', 'Boekjaar3.1':''}
    df = df.append(solvav, ignore_index = True)
    df['Unnamed: 0'][2]='Solvabiliteit eigen vermogen'

    # Remove columns as index base
    df.drop(df.columns[[4,5,6,7,8,9,10]], axis = 1, inplace = True)
    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    # change column names
    df.columns = ["Boekjaar","Eigen vermogen","Totaal vermogen","Solvabiliteit eigen vermogen","Vreemd vermogen (incl. voorzieningen)","Solvabiliteit vreemd vermogen"]
    df = df.astype({'Totaal vermogen': 'float64','Solvabiliteit eigen vermogen': 'float64','Vreemd vermogen (incl. voorzieningen)':'float64','Solvabiliteit vreemd vermogen':'float64'})   
    return df