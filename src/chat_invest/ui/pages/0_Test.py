# stock_page.py
import streamlit as st

st.title("股票詳情頁面")

if "query" in st.session_state:
    st.write(f"當前的 Query：{st.session_state['query']}")
else:
    st.warning("請先在主頁面輸入股票代號")
