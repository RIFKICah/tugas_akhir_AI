import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah')

area = st.number_input('Input Area')
bedrooms = st.number_input('Input Bedrooms')
bathrooms = st.number_input('Input Bathrooms')
parking = st.number_input('Input Parking')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[area, bedrooms, bathrooms, parking]]
    )
    st.write('Estimasi harga rumah : ', predict)