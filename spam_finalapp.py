import numpy as np 
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline    
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

#------------------------------------------------------------------Pickle Model--------------------------------------------------------------------------------------------------------#
with open("D:/project/.venv/Internship/spam_mail/model_1.pkl",'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title='Spam Mail Model', layout="wide")
st.title(':yellow[*Spam Mail Predicting Model By Abdul Haleem*]')
#-----------------------------------------------------------------Model deployement-----------------------------------------------------------------------------------------------------------------------------------------#
def home():
    st.markdown("# :orange[Predicting Message Type based on Trained data and model]")
    col1,col2=st.columns(2)
    with col1:
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("## :white[*Overview*] : Build theClassification model to predict the Mail Spam or not.")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("## :blue[*Technologies used*] : Python, Pandas, Numpy, Pickel, Matplotlib, Seaborn, Scikit-learn, Streamlit.")
    with col2:
        col2.markdown("# ")
        col2.markdown("# ")
        st.image(Image.open(r'D:/project/.venv/Internship/spam_mail/message_1.jpeg'),width=400)
        col2.markdown("# ")
        col2.markdown("# ")
        col2.markdown("# ")
        st.image(Image.open(r'D:/project/.venv/Internship/spam_mail/message_2.jpeg'),width=400)

def prediction():
    st.markdown("# :orange[Predicting Message Type based on Trained data and model]")
    with st.form("Input Message"):
        col1,col2=st.columns([1.0,1.0])
        with col1:
            text=st.text_area('Type the message')
            submit=st.form_submit_button(label='Submit')
        with col2:
            if submit:
                vec_text = [''.join(map(str,text)) ]
                Y_pred=model.predict(vec_text)
                col2.markdown("# ")
                
                if Y_pred[0]==0:
                    st.error("This message is Spam Message")
                else:
                    st.success("This message is Not spam Message")
#-------------------------------------------------------------------Streamlit part--------------------------------------------------------------------------------------------------------#
with st.sidebar:
    option = option_menu("Main menu",['Home','Prediction'],
                       icons=["house","cloud-upload","list-task","pencil-square"],
                       menu_icon="cast",
                       styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "blank"},
                                   "nav-link-selected": {"background-color": "yellow"}},
                       default_index=0)
if option=='Home':
    home()
elif option=='Prediction':
    prediction()