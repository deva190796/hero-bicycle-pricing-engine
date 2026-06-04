# frontend/app.py

import streamlit as st

st.set_page_config(
    page_title="Hero Bicycle Pricing Engine",
    layout="wide"
)

st.title("🚲 Hero Bicycle Pricing Engine")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Build Bicycle"
    ]
)

if page == "Dashboard":

    st.header("Dashboard")

    st.info(
        "Bicycle Pricing System"
    )

elif page == "Build Bicycle":

    st.header("Build Bicycle")

    st.write(
        "Frontend Integration Coming Next"
    )