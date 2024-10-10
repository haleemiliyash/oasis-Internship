import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
#--------------------------------------------------Data Retrival Part------------------------------------------------------------------------------------------------------#
def data():
    df=pd.read_csv('D:/project/.venv/Internship/covid_Unemployement_visulization/modified_data_1.csv')
    return df
DF=data()

#--------------------------------------------------- streamlit part---------------------------------------------------------------------------------------------------------#
st.set_page_config(page_title='Unemployment Analysis',page_icon=":1234:",layout="wide")
st.title('Covid 19 Unemployment Analysis')

with st.sidebar:
    select= option_menu('Main Menu',['Home','About','Visualization & Analysis'],icons=["house","list-task","pencil-square"],menu_icon="cast", default_index=0)

if select=='Home':
    col1,col2 = st.columns(2)
    with col1:
        st.write("""A lockdown to curb the spread of coronavirus has seen 122 million Indians lose their jobs in April alone, new data from a private research agency has shown.
                India's unemployment rate is now at a record high of 27.1%, according to the Centre for Monitoring the Indian Economy (CMIE).The new data shows India's unemployment figures are four times that of the US.
                India doesn’t release official jobs data, but CMIE data is widely accepted.The country has been in lockdown since 25 March to curb Covid-19 infections, causing mass layoffs and heavy job losses.
                India currently has close to 50,000 reported infections.Unemployment hit 23.5% in April, a sharp spike from 8.7% in March. This is attributed to the lockdown, which brought most economic activity - except essential services such as hospitals, pharmacies and food supplies - to a standstill.
                India's bailout may not be enough to save economy""")
        st.image(Image.open(r"D:/project/.venv/Internship/covid_Unemployement_visulization/covid.jpg"),width=400)
        
        
    with col2:
        st.write("""Scenes of desperate migrant workers, particularly daily-wage earners, fleeing cities on foot to return to their villages, filled TV screens and newspapers for most of April. Their informal jobs, which employ 90% of the population, were the first to be hit as construction stopped, and cities suspended public transport.
                But protracted curfews and the continued closure of businesses - and the uncertainty of when the lockdown will end - hasn’t spared formal, permanent jobs either.
                Large companies across various sectors - media, aviation, retail, hospitality, automobiles - have announced massive layoffs in recent weeks. And experts predict that many small and medium businesses are likely to shut shop altogether.
                A closer look at CMIE’s data shows the devastating effect the lockdown has had on India's organised economy.
                Of the 122 million who have lost their jobs, 91.3 millions were small traders and labourers. But a fairly significant number of salaried workers - 17.8 million - and self-employed people - 18.2 million - have also lost work.""")
        st.image(Image.open(r"D:/project/.venv/Internship/covid_Unemployement_visulization/unemployment.jpeg"),width=400)

if select=='About':
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open(r"D:/project/.venv/Internship/covid_Unemployement_visulization/home_jpg.jpeg"),width=400)
    with col2:
            st.image(Image.open(r"D:/project/.venv/Internship/covid_Unemployement_visulization/home_1.png"),width=400)

if select=='Visualization & Analysis':
    tab1,tab2,tab3,tab4,tab5=st.tabs(['Unemployement Over the Period','Employed Data analysis','States Based Analysis','Area and states wise Visualization','Area wise charts'])
    with tab1:
        Mean_unemployement_2020=DF.groupby('Date')['Unemployment Rate'].mean()
        plt.figure(figsize=(4,2))
        fig=plt.plot(Mean_unemployement_2020.index,Mean_unemployement_2020.values,marker='*')
        plt.xticks(rotation=90,fontsize=8)
        plt.xlabel("Date")
        plt.ylabel("Unemployment rate")
        plt.title("Unemployment Over the period")
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
    with tab2:
        plot_3=px.bar(DF,x='Month',y='Employed',title="Employed data based on Months",color='Employed')
        st.plotly_chart(plot_3)
    with tab3:
        sns.barplot(data=DF,x='States',y='Unemployment Rate',label='States',color='#3377FF')
        plt.xlabel("States")
        plt.ylabel("Unemployment rate")
        plt.title("Unemployment Over the States wise")
        plt.xticks(rotation='vertical',fontsize=8)
        st.pyplot()
    with tab4:
        plot_2=px.sunburst(DF,path=['Area','States'],values='Unemployment Rate',title='Unemployment rate By States and Area',color_continuous_scale='Reds')
        st.plotly_chart(plot_2,width=1000,height=600)
    with tab5:
        fig, ax = plt.subplots(figsize=(2,2))
        mean_unemployement=DF.groupby('Area')['Unemployment Rate'].mean()
        ax.pie(mean_unemployement, labels=mean_unemployement.index, autopct='%1.1f%%', shadow=True)
        ax.set_title('Percentage of Unemployment in Different Areas')
        st.pyplot(fig)

