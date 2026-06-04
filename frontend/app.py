import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Hero Bicycle Pricing Engine",
    layout="wide"
)

st.title("🚲 Hero Bicycle Pricing Engine")

page = st.sidebar.radio(
    "Navigation",
    [
        "Build Bicycle",
        "Saved Configurations"
    ]
)

if page == "Build Bicycle":

    st.header("Build Bicycle")

    try:
        response = requests.get(f"{BASE_URL}/components")

        if response.status_code != 200:
            st.error(f"Failed to load components: {response.text}")
            st.stop()

        components = response.json()

    except Exception as e:
        st.error(f"Backend not running: {e}")
        st.stop()

    frames = [c for c in components if c["category"] == "Frame"]
    gears = [c for c in components if c["category"] == "Gear"]
    tyres = [c for c in components if c["category"] == "Tyre"]
    brakes = [c for c in components if c["category"] == "Brake"]
    seats = [c for c in components if c["category"] == "Seat"]

    if not all([frames, gears, tyres, brakes, seats]):
        st.warning(
            "Please ensure at least one Frame, Gear, Tyre, Brake and Seat exists."
        )
        st.stop()

    st.subheader("Select Components")

    frame = st.selectbox(
        "Frame",
        frames,
        format_func=lambda x: x["name"]
    )

    gear = st.selectbox(
        "Gear",
        gears,
        format_func=lambda x: x["name"]
    )

    tyre = st.selectbox(
        "Tyre",
        tyres,
        format_func=lambda x: x["name"]
    )

    brake = st.selectbox(
        "Brake",
        brakes,
        format_func=lambda x: x["name"]
    )

    seat = st.selectbox(
        "Seat",
        seats,
        format_func=lambda x: x["name"]
    )

    pricing_date = st.date_input(
        "Pricing Date"
    )

    payload = {
        "frame_id": frame["id"],
        "gear_id": gear["id"],
        "tyre_id": tyre["id"],
        "brake_id": brake["id"],
        "seat_id": seat["id"],
        "pricing_date": str(pricing_date)
    }

    col1, col2 = st.columns(2)

    with col1:
        calculate_btn = st.button("Calculate Price")

    with col2:
        save_btn = st.button("Save Configuration")

    if calculate_btn:

        response = requests.post(
            f"{BASE_URL}/calculate-price",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Price Breakdown")

            breakdown_df = pd.DataFrame(
                result["breakdown"]
            )

            st.dataframe(
                breakdown_df,
                use_container_width=True
            )

            st.success(
                f"Total Price: ₹{result['total_price']}"
            )

        else:
            st.error(response.text)

    if save_btn:

        response = requests.post(
            f"{BASE_URL}/save-configuration",
            json=payload
        )

        if response.status_code == 200:
            st.success("Configuration Saved Successfully")
        else:
            st.error(response.text)

elif page == "Saved Configurations":

    st.header("Saved Configurations")

    try:

        response = requests.get(
            f"{BASE_URL}/configurations"
        )

        if response.status_code != 200:
            st.error(response.text)
            st.stop()

        data = response.json()

        if len(data) == 0:
            st.info("No saved configurations found.")
        else:
            st.dataframe(
                pd.DataFrame(data),
                use_container_width=True
            )

    except Exception as e:
        st.error(str(e))