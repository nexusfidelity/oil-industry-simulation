import streamlit as st
import numpy as np
import pandas as pd
import time
import random
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="Oil Processing Plant Simulation",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Oil Processing Plant Simulation")
    
    tabs = st.tabs(["Oil Processing",  "Oil Production Time Series", "Gas Pump Failure Prediction"])
    
    with tabs[0]:
        simulate_process()
    
    with tabs[1]:
        simulate_oil_production_time_series()
    
    with tabs[2]:
        simulate_gas_pump_failure()

def simulate_process():
    st.header("Oil Processing Simulation")
    
    st.sidebar.header("Simulation Settings")
    processing_speed = st.sidebar.slider("Processing Speed (seconds per step)", 0.1, 2.0, 0.5)
    
    stages = [
        "Crude Oil Intake",
        "Desalting",
        "Distillation",
        "Conversion",
        "Blending & Treatment",
        "Storage & Distribution"
    ]
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    process_data = []
    
    for i, stage in enumerate(stages):
        time.sleep(processing_speed)
        efficiency = round(random.uniform(85, 99), 2)
        output = round(random.uniform(95, 100), 2)
        process_data.append([stage, efficiency, output])
        progress_bar.progress((i + 1) / len(stages))
        status_text.text(f"Processing: {stage}...")
    
    df = pd.DataFrame(process_data, columns=["Stage", "Efficiency (%)", "Output (%)"])
    st.success("Processing Complete!")
    st.write(df)
    
    st.bar_chart(df.set_index("Stage"))


def simulate_oil_production_time_series():
    st.header("Oil Production Time Series Simulation and Prediction")
    
    num_days = st.sidebar.slider("Number of Days", 50, 500, 100)
    
    np.random.seed(42)
    base_production = 1000  # Initial production level
    volatility = np.random.normal(0, 50, num_days)  # Introduce volatility
    trend = np.linspace(0, num_days * 2, num_days)  # Upward trend
    production = base_production + trend + volatility
    
    df_time_series = pd.DataFrame({
        "Day": np.arange(1, num_days + 1),
        "Oil Production (barrels)": production
    })
    
    st.line_chart(df_time_series.set_index("Day"))
    st.write(df_time_series)
    
    # Predict next day's production
    model = RandomForestRegressor()
    X = df_time_series["Day"].values.reshape(-1, 1)
    y = df_time_series["Oil Production (barrels)"].values
    model.fit(X, y)
    
    next_day = num_days + 1
    predicted_output = model.predict([[next_day]])[0]
    
    st.write(f"Predicted oil production for day {next_day}: {predicted_output:.2f} barrels")


def simulate_gas_pump_failure():
    st.header("Gas Pump Failure Prediction")
    
    data = np.array([
        [1000, 70, 200, 0], [1200, 75, 210, 0], [1500, 80, 220, 1],
        [1700, 85, 230, 1], [2000, 90, 240, 1], [900, 65, 190, 0]
    ])
    
    X = data[:, :-1]
    y = data[:, -1]
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    usage_hours = st.sidebar.slider("Usage Hours", 500, 2500, 1500)
    temperature = st.sidebar.slider("Temperature (°F)", 60, 100, 80)
    pressure = st.sidebar.slider("Pressure (psi)", 180, 260, 220)
    
    prediction = model.predict([[usage_hours, temperature, pressure]])[0]
    
    if prediction >= 0.5:
        st.error("Warning: High risk of gas pump failure!")
    else:
        st.success("Gas pump is operating normally.")

if __name__ == "__main__":
    main()