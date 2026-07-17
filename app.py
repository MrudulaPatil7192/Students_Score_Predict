import streamlit as st
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for a beautiful, shadow-dense vertical layout
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f4f6f9;
    }
    
    /* Global container for the app */
    .main-container {
        background: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
    }
    
    /* Header styling */
    .header-title {
        color: #1e1b4b;
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .header-subtitle {
        color: #4b5563;
        font-size: 16px;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Custom input card styling (wrapping around Streamlit elements) */
    div[data-testid="stFormSubmitButton"] > button, .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #4338ca 0%, #2e2685 100%);
    }

    /* Target widget blocks to give them a card feel */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #ffffff;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }
    
    /* Result card styling */
    .result-card {
        padding: 24px;
        background: #ffffff;
        border-left: 6px solid #10b981;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        text-align: center;
        margin-top: 25px;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    .result-score {
        font-size: 36px;
        font-weight: 800;
        color: #065f46;
        margin-top: 8px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10s); }
        to { opacity: 1; transform: translateY(0); }
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

# Header Section wrapped in clean HTML formatting
st.markdown('<div class="header-title">🎓 Student Performance Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">Enter metrics sequentially to forecast final evaluation grades.</div>', unsafe_allow_html=True)

# Sequential Vertical Input Layout
hours_studied = st.number_input(
    "📚 Hours Studied", 
    min_value=0.0, 
    max_value=24.0, 
    value=5.0, 
    step=0.5,
    help="Number of hours spent studying per day."
)

sleep_hours = st.number_input(
    "😴 Sleep Hours", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.0, 
    step=0.5,
    help="Average hours of sleep per night."
)

attendance_percent = st.slider(
    "🏫 Attendance Percentage", 
    min_value=0.0, 
    max_value=100.0, 
    value=85.0, 
    step=1.0,
    help="Percentage of classes attended."
)

previous_scores = st.slider(
    "📊 Previous Evaluation Scores", 
    min_value=0.0, 
    max_value=100.0, 
    value=75.0, 
    step=1.0,
    help="Score achieved in the previous evaluation."
)

# Centered Action Area
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

if st.button("Generate Performance Prediction"):
    # Arrange features in the direct sequence expected by the model
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Predict using the loaded KNN model
    prediction = model.predict(features)[0]
    
    # Premium green-accented result card container with deep shadow effects
    st.markdown(
        f"""
        <div class="result-card">
            <span style="color: #4b5563; font-size: 14px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">
                Estimated Outcome
            </span>
            <div class="result-score">🎯 {prediction:.2f} / 100</div>
        </div>
        """, 
        unsafe_allow_html=True
    )
