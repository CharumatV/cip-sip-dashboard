import streamlit as st
from datetime import datetime
import time

# Initialize session state
if 'phase_history' not in st.session_state:
    st.session_state.phase_history = []

# Simplified sensor data
PHASE_DATA = {
    "Pre-Rinse": {"flow": 9.2, "temp": 32.0, "conductivity": 25.0},
    "Chemical Wash": {"flow": 7.0, "temp": 75.0, "conductivity": 1500.0},
    "Final Rinse": {"flow": 8.0, "temp": 28.0, "conductivity": 40.0},
    "SIP": {"flow": 0.0, "temp": 100.0, "pressure": 1.2}
}

st.title("🧼 CIP/SIP Monitoring (Simplified)")
if st.button("Start Simulation"):
    placeholder = st.empty()
    for phase, sensor_data in PHASE_DATA.items():
        with placeholder.container():
            st.subheader(f"Phase: {phase}")
            col1, col2 = st.columns(2)
            col1.metric("🌡️ Temp", f"{sensor_data['temp']}°C")
            col2.metric("💧 Flow", f"{sensor_data['flow']} L/min")

            st.session_state.phase_history.append(
                f"{datetime.now().strftime('%H:%M:%S')} - {phase}"
            )
            st.write("History:", *st.session_state.phase_history[-3:])
        time.sleep(3)
      
