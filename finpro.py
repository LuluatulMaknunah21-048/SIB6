import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
import pickle
kolom = [
'featureA', 'featureB', 'featureC', 'featureD', 'featureE', 'featureF', 'featureG', 'featureH', 'featureI',
'compositionA', 'compositionB', 'compositionC', 'compositionD', 'compositionE', 'compositionF', 'compositionG',
'compositionH', 'compositionI', 'compositionJ',
'categoryB_catB_0', 'categoryB_catB_1',
'categoryD_catD_0', 'categoryD_catD_1', 'categoryD_catD_2',
'categoryF_catF_0', 'categoryF_catF_1', 'categoryF_catF_2',
'unit_unit_0', 'unit_unit_1', 'unit_unit_10', 'unit_unit_11', 'unit_unit_12', 'unit_unit_13', 'unit_unit_14',
'unit_unit_15', 'unit_unit_16', 'unit_unit_17', 'unit_unit_18', 'unit_unit_2', 'unit_unit_3', 'unit_unit_4',
'unit_unit_5', 'unit_unit_6', 'unit_unit_7', 'unit_unit_8', 'unit_unit_9'
]
df= pd.DataFrame(data=[[0]*len(kolom)], columns=kolom)
st.write(df)
with st.sidebar:
    selected=option_menu('Water Quality Predict',['Artikel','Start Prediksi','About Us'])
st.title('PREDIKSI KUALITAS AIR')
if selected=='Artikel':
    image_path = "airr.jpeg"
    st.image(image_path, caption="water", use_column_width=True, output_format="auto")

    st.write('Selamat datang, di web prediksi kualitas air.')
    st.write('Tujuan dari penelitian ini sebagai berikut :')
    st.markdown('''
    <b>Menjaga Kualitas Air untuk Masa Depan yang Berkelanjutan: Membangun Prediksi yang Berkelanjutan dengan Pendekatan ESG</b>
    <br>
    Dalam era di mana keberlanjutan menjadi fokus utama dalam segala aspek kehidupan, termasuk manajemen lingkungan dan sumber daya alam, menjaga kualitas air menjadi tantangan yang semakin mendesak. Di tengah kekhawatiran akan perubahan iklim, polusi, dan eksploitasi sumber daya alam, prediksi kualitas air menjadi instrumen penting dalam menghadapi tantangan ini dengan pendekatan yang berkelanjutan.
''', unsafe_allow_html=True)
    st.markdown('''
    <b>Mengapa Kualitas Air Menjadi Issu ESG?</b><br>
    Pentingnya kualitas air tidak hanya terbatas pada aspek kesehatan masyarakat, tetapi juga berkaitan dengan tanggung jawab sosial dan lingkungan perusahaan (ESG). Secara global, perusahaan semakin menyadari bahwa pemeliharaan lingkungan hidup adalah bagian integral dari operasi mereka, serta memiliki dampak langsung terhadap reputasi, risiko hukum, dan stabilitas keuangan. Oleh karena itu, masalah kualitas air telah menjadi salah satu fokus utama dalam agenda ESG.
''', unsafe_allow_html=True)

if selected=='Start Prediksi':
    col1,col2,col3=st.columns(3)
    with col1:
        featureA = st.number_input('featureA')
        featureB = st.number_input('featureB')
        featureC = st.number_input('featureC')
        featureD = st.number_input('featureD')
        featureE = st.number_input('featureE')
        featureF = st.number_input('featureF')
        featureG = st.number_input('featureG')
        featureH = st.number_input('featureH')
    with col2:
        featureI = st.number_input('featureI')
        compositionA = st.number_input('compositionA')
        compositionB = st.number_input('compositionB')
        compositionC = st.number_input('compositionC')
        compositionD = st.number_input('compositionD')
        compositionE = st.number_input('compositionE')
        compositionF = st.number_input('compositionF')
        compositionG = st.number_input('compositionG')
    with col3:
        compositionH = st.number_input('compositionH')
        compositionI = st.number_input('compositionI')
        compositionJ = st.number_input('compositionJ')
        catb=['Silahkan Pilih','0','1']
        catbp=st.selectbox('PILIH Category B',catb)
        if catb =='0':
            df['categoryB_catB_0']=1
        if catb =='1':
            df['categoryB_catB_1']=1
              
        catd=['Silahkan Pilih','0','1','2']
        catdp=st.selectbox('PILIH Category D',catd)
        if catd =='0':
            df['categoryD_catD_0']=1
        if catd =='1':
            df['categoryD_catD_1']=1
        if catd =='2':
            df['categoryD_catD_1']=1

        catf=['Silahkan Pilih','0','1','2']
        catfp=st.selectbox('PILIH Category F',catf)
        if catf =='0':
            df['categoryD_catF_0']=1
        if catf =='1':
            df['categoryF_catF_1']=1
        if catf =='2':
            df['categoryF_catF_1']=1

        unit=['Silahkan Pilih','0','1','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
        unitp=st.selectbox('PILIH UNIT',unit)
        if unit =='0':
            df['unit_unit_0']=1
        if unit =='1':
            df['unit_unit_1']=1
        if unit =='2':
            df['unit_unit_2']=1
        if unit =='3':
            df['unit_unit_3']=1
        if unit =='4':
            df['unit_unit_4']=1
        if unit =='5':
            df['unit_unit_5']=1
        if unit =='6':
            df['unit_unit_6']=1
        if unit =='7':
            df['unit_unit_7']=1
        if unit =='8':
            df['unit_unit_8']=1
        if unit =='9':
            df['unit_unit_9']=1
        if unit =='10':
            df['unit_unit_10']=1
        if unit =='11':
            df['unit_unit_11']=1
        if unit =='12':
            df['unit_unit_12']=1
        if unit =='13':
            df['unit_unit_13']=1
        if unit =='14':
            df['unit_unit_14']=1
        if unit =='15':
            df['unit_unit_15']=1
        if unit =='16':
            df['unit_unit_16']=1
        if unit =='17':
            df['unit_unit_17']=1
        if unit =='18':
            df['unit_unit_18']=1
    button=st.button('PREDIKSI',use_container_width=1000,type='primary')
    if button:
        if catb !='Silahkan Pilih'and catd !='Silahkan Pilih'and catd !='Silahkan Pilih'and unit !='Silahkan Pilih':
            with open('norm.pkl', 'rb') as file:
                normalisasi=pickle.load(file)
            norm_data = normalisasi.transform(df)
            st.write(norm_data)
            with open('ridge_model.pkl', 'rb') as f:
                loaded_model= pickle.load(f) 
            prediction=loaded_model.predict(norm_data)
            for i in prediction:
                st.write('kualitas air = ',i)
    else:
        st.write('Mohon Isi semua Kolom Pertanyaan')
if selected=='About Us':
    st.write('kelompok 2 - Data Science SIB cycle 6 GreatEdu')
