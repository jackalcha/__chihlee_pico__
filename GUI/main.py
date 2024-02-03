import requests
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000)

st.title('Pico_W 專案')
st.header('雞舍:red[溫度]和:blue[光線]狀態')
st.divider()
st.snow()

url = 'https://blynk.cloud/external/api/get?token=_OgXaLhGv-t1s-Gw8j5I5Sr_5b-2zUov&v1&v0'

response = requests.request("GET",url)
if response.status_code == 200:
    all_data = response.json()
    st.info(f'光線{all_data["v0"]}')
    st.warning(f'可變電阻{all_data["v1"]}')
else:
    st.write("連線失敗,請稍候再試")