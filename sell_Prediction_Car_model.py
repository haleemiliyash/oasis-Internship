import numpy as np
import pickle
import json
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import datetime as dt

st.set_page_config(page_title='Car Price prediction model', layout="wide")
st.title('Car Resaleprice Prediction Model By Abdul Haleem')


with open("D:/project/.venv/Internship/car_pirce_prediction/car_sell.pkl",'rb') as file:
    price_model = pickle.load(file)
with open("D:/project/.venv/Internship/car_pirce_prediction/Cat_Columns_Encoded.json",'rb') as file:
    encode_file = json.load(file)

def home():
    col1,col2=st.columns(2)
    with col1:
        col1.markdown("# ")
        col1.markdown("# ")
        Original_text='<p style="font-family:Courier; color:White; font-size: 15px;">Build regression model to predict the Car resale price. Dataset which have different Used car. As most vehicle owners are acutely aware, the instant you drive your fresh and cherished vehicle away from the dealership, its value begins to decline. Keeping it in a pristine state and promptly addressing any dents or imperfections can contribute to sustaining its resale value,though it likely that some depreciation will occur. Research findings have consistently demonstrated that Japanese automobile manufacturers uphold their value remarkably well, even after prolonged usage.</p>'
        col1.markdown(Original_text,unsafe_allow_html=True)
        col1.markdown("# ")
        col1.markdown("## :blue[*Technologies used*] : Python, Pandas, Numpy, Pickel, Matplotlib, Seaborn, Scikit-learn, Streamlit.")
        col1.markdown("# ")
        col1.markdown("#")
        col1.markdown("# ")
        col1.markdown("#")
        col1.markdown("# ")
        col1.markdown("# ")
    with col2:
        col2.markdown("# ")
        col2.markdown("# ")
        st.image(Image.open(r'D:/project/.venv/Internship/car_pirce_prediction/car_1.jpeg'),width=400)
        col2.markdown("# ")
        col2.markdown("# ")
        st.image(Image.open(r'D:/project/.venv/Internship/car_pirce_prediction/car.jpeg'),width=400)
        col2.markdown("# ")

#-------------------------------------------------------------------------------Model Prediction------------------------------------------------------------------------------------------------------------------------------------------------------------#
def sell_price():
    st.markdown("# :white[Predicting price based on Trained data and model]")
    with st.form("Regression"):
        col1,col2,col3=st.columns([0.5,0.2,0.5])
        with col1:
            car_name=st.selectbox("Select the **Car Name**",encode_file['Car_Name_initial'])
            year=st.number_input("Select the Year", min_value=2003, max_value=2019, value=2003)
            present_price=st.number_input('Select the **Present Price**',value=10.00,min_value=1.00,max_value=50.00,step=1.0)
            driven_km=st.number_input('Select the **Driven KMS**',value=1000.0,min_value=500.0,max_value=500000.0,step=1000.0)
            
        with col3:
            fuel_type=st.selectbox("Select the **Fuel Type**",encode_file['Fuel_Type_initial'])
            sell_type=st.selectbox("Select the **Sell Type**",encode_file['Selling_type_initial'])
            tranmission=st.selectbox("Select the **Transmission Type**",encode_file['Transmission_initial'])
            owner=st.selectbox("Select the **Number of Owner**",encode_file['Owner_initial'])

        with col2:
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            col2.markdown("# ")
            st.markdown('Click below button to predict')
            button=st.form_submit_button(label='Predict')

    if button:
        car_encode=encode_file['Car_Name_Final'][(encode_file["Car_Name_initial"].index(car_name))]
        sell_encode=encode_file['Selling_type_Final'][(encode_file["Selling_type_initial"].index(sell_type))]
        fuel_encode=encode_file['Fuel_Type_Final'][(encode_file["Fuel_Type_initial"].index(fuel_type))]
        tramission_encode=encode_file['Transmission_Final'][(encode_file["Transmission_initial"].index(tranmission))]
        owner_encode=encode_file['Owner_Final'][(encode_file["Owner_initial"].index(owner))]

        input_ar = np.array([[car_encode, year,present_price,driven_km,fuel_encode,sell_encode, tramission_encode,owner_encode]],dtype=np.float32)
        Y_pred=price_model.predict(input_ar)
        sell_price=round(Y_pred[0][0],2)
        st.header(f'Predicted Resell Price is: {sell_price}')
    
#-----------------------------------------------------------------------Streamlit Part-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

with st.sidebar:
    option = option_menu("Main menu",['Home','Resell Price Prediction'],
                       icons=["house","cloud-upload","list-task","pencil-square"],
                       menu_icon="cast",
                       styles={"nav-link": {"font-size": "15px", "text-align": "left", "margin": "-2px", "--hover-color": "white"},
                                   "nav-link-selected": {"background-color": "Grey"}},
                       default_index=0)
if option=='Home':
    home()
elif option=='Resell Price Prediction':
    sell_price()