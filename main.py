# -*- coding: utf-8 -*-

# Importing full packages
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import openpyxl
import pandas
import time
import yfinance as yf

# Importing Data
# giving the start and end dates
startDate = '2019-01-01'
endDate = '2024-01-01'

# setting the ticker value
ticker = 'SYK'

# downloading the data of the ticker value between
# the start and end dates
df_syk = yf.download(ticker, startDate, endDate).reset_index()

# Configuring page details
st.set_page_config(page_title='Getting to Know Stryker!',
                   layout='wide',
                   page_icon=':circle:')

# Configuring header
t1, t2 = st.columns((.07, 1))
t1.image('index_1.png', width=100)
t2.title('Getting to know Stryker Corporation')
t2.markdown("To learn more about Stryker, and demonstrate my skillset in Python and data engineering - I built this dashboard! Through my research I learned that Stryker was founded by Dr. Homer Stryker in 1941 in the beautiful Kalmazoo Michigan, I learned that one of Styrker's first products was a mobile hospital bed - allowing for ease of patient movement! I also learned more about company performance and detailed my analysis below!")

# Creating header boxes
m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))

# Filling header boxes in
m1.write('')
m2.metric(label='Founding Year', value='1941')
m3.metric(label='Ticker Symbol', value='SYK')
m4.metric(label='Revenue', value='$17.08 Billion')
m5.write('')

# Creating tabs
tab1, tab2 = st.tabs(['Stock Open Prices', 'Stock Close Prices'])

# Tab 1
with tab1:
    # Organizations worked
    fig = px.line(df_syk,
                  x='Date',
                  y='Open')
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False),
                      plot_bgcolor='white',
                      font=dict(
                          family='Helvetica',
                          size=14,
                          color='Black'
                      ))
    fig.update_traces(line=dict(width=12, color='#fbb201'))
    fig.update_yaxes(title='Stock Open Price')
    fig.update_xaxes(title='')

    st.plotly_chart(fig, use_container_width=True)