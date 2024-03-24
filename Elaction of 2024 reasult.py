import streamlit as st
import pandas as pd
import numpy as np
st.title("Asslam-o-Alikum")
Name = st.text_input("Enter your Name : ")
Email = st.text_input("Email")
Password = st.text_input("Password")
adr = st.text_area("Enter you addres : ")
button = st.button("Done")

if button :
    st.markdown(f"""
    Name : {Name}
    Email : {Email}
    Password : {Password}
    Addrea : {adr}
""")
st.title("Hello Every Body how are you?")
st.header("So friend the reasult of election 2024 is redy")
st.header("So friend first we know for the sets of MNA")
st.write(""" 1. PTI has 92 sets  ,  
         2.PML-N has 76 sets  ,  
         3.PPPP has 54 sets  ,  
         4.MQM-P has 17 sets  ,  
         5.JUI-F has 5 sets  ,  
         6.PML-Q has 3 sets  ,  
         7.IPP has 3 sets  ,  
         8.BNP-M has 2 sets  ,  
         9.PML-Z has 1 sets  ,  
         10.MWM has 1 sets  ,  
         11.PMAp has 1 sets  ,  
         12.NP has 1 sets  ,  
         13.BAP has 1 sets  ,  
         14.IND has 8 sets  ,  
""")
