import streamlit as st
from ledger_agent import run_ledger_analysis  # <-- Uncomment this!

st.set_page_config(page_title="Ledger Agent")

st.title("Ledger Analysis Agent 📒")
st.write("Click the button below to analyze the ledger.")

if st.button("Analyze Ledger"):               
    df, result = run_ledger_analysis()        
    st.subheader("🧾 Ledger Data")            
    st.dataframe(df)                          
    st.subheader("🔍 Analysis Result")        
    st.write(result)                          