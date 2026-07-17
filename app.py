import streamlit as st
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for a polished look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: white;
    }
    .result-box {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #4f46e5;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model.pkl: {e}")
    st.stop()

# Header App section
st.title("🎓 Student Performance Predictor")
st.markdown("Enter the student details below to predict their performance score using the trained KNN model.")
st.divider() # Fixed the st.hr() error here

# Input layout using columns
col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "📚 Hours Studied", 
        min_value=0.0, 
        max_value=24.0, 
        value=5.0, 
        step=0.5,
        help="Number of hours spent studying per day."
    )
    
    attendance_percent = st.slider(
        "🏫 Attendance (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=85.0, 
        step=1.0,
        help="Percentage of classes attended."
    )

with col2:
    sleep_hours = st.number_input(
        "😴 Sleep Hours", 
        min_value=0.0, 
        max_value=24.0, 
        value=7.0, 
        step=0.5,
        help="Average hours of sleep per night."
    )
    
    previous_scores = st.slider(
        "📊 Previous Scores", 
        min_value=0.0, 
        max_value=100.0, 
        value=75.0, 
        step=1.0,
        help="Score achieved in the previous evaluation."
    )

st.divider()

# Prediction logic
if st.button("Predict Score"):
    # Arrange features exactly as required by the model
    # ['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores']
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    # Display the result beautifully
    st.markdown("### Predicted Result:")
    st.markdown(
        f'<div class="result-box">🎯 Predicted Score: {prediction:.2f}</div>', 
        unsafe_allow_html=True
    )
