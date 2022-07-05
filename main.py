import streamlit as st
import numpy as np
import pprint
import pandas as pd
import time


st.title('User behaviour analytics')
st.write('')

st.image('front_image.png', use_column_width= True)

#st.sidebar.title("Features")
st.write('')
st.subheader('Input the details of the user action')


placeholder_c = st.empty()
placeholder_s = st.empty()
placeholder_e = st.empty()
placeholder_g = st.empty()
placeholder_p = st.empty()
placeholder_u = st.empty()

val1 = placeholder_c.number_input('Hotspot1', min_value= 0)
val2 = placeholder_s.number_input('Hotspot2', min_value= 0)
val3 = placeholder_e.number_input('Hotspot3', min_value= 0)
val4 = placeholder_g.number_input('video play', min_value= 0)
val5 = placeholder_p.number_input('AR', min_value= 0)
val6 = placeholder_u.number_input('VR',min_value=0)

final_score = 0.0

final_score = 0.1*val1 + 0.1*val2 + 0.1*val3 + 0.2*val4 + 0.25*val5 + 0.25*val6

#final_score = round(final_score)
col1, col2, col3 = st.columns([1,1,.5])
click_clear = col3.button('Calculate score')


if click_clear:
    st.subheader(f'Affinity score for the user is {final_score:,f}.')

st.write('')

st.subheader('User behaviour')

if final_score == 0.0:
    st.write('')
elif final_score <= 0.3:
    st.write('The user has least affinity for the product.')
elif final_score > 0.3 and final_score <= 0.5 :
    st.write('The user has moderate affinity for the product.')
elif final_score > 0.5:
    st.write("The user has the most affinity for the product.")

col1, col2, col3 = st.columns([1,1,.5])
click_clear = col3.button('Reset values')
# set fields back to 0 when clicking button
if click_clear:

    val1 = placeholder_c.number_input('Hotspot1', 
                                               min_value= 0, value= 0, max_value = 1,key= 'redo')
    val2 = placeholder_s.number_input('Hotspot2', 
                                               min_value= 0, value= 0, max_value = 1,key= 'redo1')
    val3 = placeholder_e.number_input('Hotspot3', 
                                                 min_value= 0, value= 0, max_value = 1,key= 'redo2')
    val4 = placeholder_g.number_input('Video play', 
                                             min_value= 0, value= 0, max_value = 1,key= 'redo3')
    val5 = placeholder_p.number_input('AR', 
                                               min_value= 0, value= 0, max_value = 1,key= 'redo4')
    val6 = placeholder_u.number_input('VR', 
                                               min_value= 0, value= 0,max_value = 1, key= 'redo5')
    col3.write('The values have been reset')
