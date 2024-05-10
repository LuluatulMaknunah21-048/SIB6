import streamlit as st
import pandas as pd
selected_columns = [
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
df= pd.DataFrame(columns=selected_columns)


featureA = st.number_input('featureA')
featureB = st.number_input('featureB')
featureC = st.number_input('featureC')
featureD = st.number_input('featureD')
featureE = st.number_input('featureE')
featureF = st.number_input('featureF')
featureG = st.number_input('featureG')
featureH = st.number_input('featureH')
featureI = st.number_input('featureI')
compositionA = st.number_input('compositionA')
compositionB = st.number_input('compositionB')
compositionC = st.number_input('compositionC')
compositionD = st.number_input('compositionD')
compositionE = st.number_input('compositionE')
compositionF = st.number_input('compositionF')
compositionG = st.number_input('compositionG')
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

unit=['Silahkan Pilih','0','1','3']
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
