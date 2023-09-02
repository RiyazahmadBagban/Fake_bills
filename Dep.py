import streamlit as st
import pandas as pd
import pickle


st.title('Deployemnent on Fake Bills')



st.sidebar.header('User Input Parameters')


def user_input_features():
    DIA = st.sidebar.number_input('diagonal',min_value=171.0,max_value=173.0,step=0.1)
    HL = st.sidebar.number_input('height_left',min_value=103.0,max_value=105.0,step=0.1)
    HR = st.sidebar.number_input('height_right',min_value=102.8,max_value=105.0,step=0.1)
    ML = st.sidebar.number_input('margin_low',min_value=2.95,max_value=7.0,step=0.1)
    
    MU = st.sidebar.number_input("margin_up",min_value=1.8,max_value=4.0,step=0.1)
    Len = st.sidebar.number_input('length',min_value=109.5,max_value=114.5,step=0.1)
   
   
    
    user_input = {
    'diagonal': DIA,
    'height_left': HL,
    'height_right': HR,
    'margin_low': ML,
    'margin_up': MU,
    'length': Len
                    }
    
    

    features = pd.DataFrame(user_input,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)



with open(file="final_model.sav",mode="rb") as f1:
    model = pickle.load(f1)
    
    
prediction = model.predict(df)
#prediction_proba = clf.predict_proba(df)

st.subheader('Predicted Result')
#st.write('Yes' if prediction_proba[0][1] > 0.5 else 'No')

#st.subheader('Prediction Probability')
st.write(prediction[0])

