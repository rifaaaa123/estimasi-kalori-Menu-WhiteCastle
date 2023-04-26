import pickle
import streamlit as st

model = pickle.load(open('estimasi_WhiteCastle.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Kalori Menu Makanan di WhiteCastle')

FatCalories = st.number_input('Input Fat Calories')
Fat = st.number_input('Input Fat(g)')
SatFat = st.number_input('Input SatFat(g)')
TransFat = st.number_input('Input TransFat(g)')
Cholesterol = st.number_input('Input Cholesterol(mg)')
Sodium = st.number_input('Input Sodium(g)')
TotalCarb = st.number_input('Input TotalCarb(g)')
DietaryFiber = st.number_input('Input DietaryFiber(g)')
Sugars = st.number_input('Input Sugars(g)')
Protein = st.number_input('Input Protein(g)')
WeightWatchers = st.number_input('Input WeightWatchers')


predict = ''

if st.button('Cek Kalori'):
    predict = model.predict(
        [[FatCalories,Fat,SatFat,TransFat,Cholesterol,Sodium,TotalCarb,DietaryFiber,Sugars,Protein,WeightWatchers]]
    )
    st.write ('Estimasi jumlah kalori makanan di Menu White Castle (kCal) : ', predict)