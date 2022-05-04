import pandas as pd  
import streamlit as st
import plotly.express as px


# Samenstelling activa en pasiva boekjaar [TAART DIAGRAM]
# filter row on column value
def create_pie(df, name_value, title_value,title_pie):
    fig = px.pie(df, 
            values=name_value, 
            names=title_value,
            title=title_pie            
            )
    fig.update_traces(textfont_size=20, pull=[0, 0.2], marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(legend = dict(font = dict(size = 20)),
        title = dict(font = dict(size = 30)))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))    
    return fig

#Klant-en leverenancierskrediet [BAR]
def create_bar(df, x, y, orientation, title, range_x, labels):
    fig = px.bar(df, x=x, y=y, 
        orientation=orientation,
        barmode='group',
        title=title,
        range_x=range_x,
        labels=labels,
        text_auto=True)
    fig.update_traces()
    #fig.update_layout(xaxis_title="X Axis Title", yaxis_title="Y Axis Title")
    fig.update_traces(textfont_size=20,  marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(legend = dict(font = dict(size = 20)), title = dict(font = dict(size = 30)))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    return fig

#Liquiditeit [LINE CHART]
def create_line(df, x, y, color):
    fig = px.line(df, x = x, y = y, color = color)
    fig.update_traces(textfont_size=20,  marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(legend = dict(font = dict(size = 20)), title = dict(font = dict(size = 30)))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    return fig