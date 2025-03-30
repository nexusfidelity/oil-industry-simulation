import streamlit as st

st.set_page_config(
    page_title="Oil Processing Plant Simulation",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header('gas simulation')



col1, col2, col3 = st.columns([1,1.5,1])    
with col2:
    st.image('photo.png',use_container_width=True)
    

colleft, col1, col2, col3,colright = st.columns(5)

with col1:
    st.header('gas inlet')
    
    st.write('differential pressure')
    st.write('0.5 bar')
    st.write('Range 0=0k 1=Trip')
    
with col2:
    st.header('gas turbine')
    st.write('pressure')
    st.write('10 bar')
    st.write('Range 4=low trip 15=High Trip')
    
    st.divider()
    
    st.write('max vibration')
    st.write('5 mm/s')
    st.write('Range 0=normal 10=Trip')
    
    st.divider()
    
    st.write('temperature')
    st.write('100 celsius')
    st.write('Range 250=Trip')
    
with col3:
    st.header('gas compressor')
    
    st.header('gas turbine')
    st.write('pressure')
    st.write('90 bar')
    st.write('Range 50=low trip 110=High Trip')
    
    st.divider()
    
    st.write('flow')
    st.write('600 mmscfd')
    st.write('Range 100=Trip')
    
    st.divider()
    
    st.write('speed')
    st.write('7,000 rpm')
    st.write('10,000 overspeed')