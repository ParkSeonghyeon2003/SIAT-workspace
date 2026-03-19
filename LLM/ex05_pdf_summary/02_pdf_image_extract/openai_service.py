# openai_service.py

import streamlit as st
from openai import OpenAI


# ---------------------------
# OpenAI 클라이언트
# ---------------------------
@st.cache_resource
def create_openai_client(api_key):
    return OpenAI(api_key=api_key)