import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = st.session_state["data2"]
df = df.set_index('name')
st.dataframe(df, use_container_width=True)