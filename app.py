import streamlit as st
import pickle
import numpy as np

# Set page configuration with a cute kitty emoji
st.set_page_config(
    page_title="Kitty Score Tracker 🐾",
    page_icon="🌸",
    layout="centered"
)

# 3D Kawaii Kitty Pink / Cartoon UI Styling
st.markdown("""
    <style>
    /* Soft pastel pink gradient background with a subtle playful touch */
    .stApp {
        background: linear-gradient(135deg, #ffe4e6 0%, #fbcfe8 50%, #f472b6 100%);
    }
    
    /* 3D Soft Clay Outer Card Container */
    .kitty-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 30px;
        box-shadow: 
            0px 10px 0px #f472b6,
            0px 20px 30px rgba(244, 114, 182, 0.2);
        border: 4px solid #4c1d95; /* Deep purple borders for high-contrast cartoon styling */
        margin-bottom: 25px;
    }
    
    /* Kawaii Kitty Header Bubble */
    .bubble-header {
        background: #f472b6;
        border: 4px solid #4c1d95;
        border-radius: 22px;
        padding: 18px;
        text-align: center;
        box-shadow: 5px 5px 0px #4c1d95;
        margin-bottom: 35px;
        position: relative;
    }
    
    .bubble-title {
        color: #ffffff;
        font-size: 30px;
        font-weight: 900;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        margin: 0;
        text-shadow: 3px 3px 0px #4c1d95;
    }
    
    .bubble-subtitle {
        color: #ffe4e6;
        font-size: 14px;
        font-weight: 700;
        margin-top: 5px;
        letter-spacing: 0.5px;
    }
    
    /* Transforming Input Blocks into 3D Cartoon Pink Panels */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #fff5f7 !important;
        padding: 18px !important;
        border-radius: 20px !important;
        border: 3px solid #4c1d95 !important;
        box-shadow: 4px 4px 0px #4c1d95 !important;
        margin-bottom: 24px !important;
        transition: transform 0.1s ease !important;
    }
    
    div[data-testid="stNumberInput"]:focus-within, div[data-testid="stSlider"]:focus-within {
        transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px #4c1d95 !important;
        background: #ffffff !important;
    }
    
    /* Chunky 3D Cartoon Kitty Button */
    .stButton > button {
        width: 100%;
        background: #ff85a2;
        color: #ffffff !important;
        border: 4px solid #4c1d95;
        border-radius: 20px;
        padding: 16px 24px;
        font-size: 20px;
        font-weight: 900;
        font-family: 'Comic Sans MS', sans-serif;
        box-shadow: 0px 6px 0px #4c1d95;
        transition: all 0.1s ease;
    }
    
    .stButton > button:hover {
        background: #ff6584;
        color: #ffffff !important;
        transform: translateY(2px);
        box-shadow: 0px 4px 0px #4c1d95;
    }
    
    .stButton > button:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #4c1d95;
    }
    
    /* Aesthetic 3D Result Viewport */
    .kitty-result {
        margin-top: 30px;
        padding: 25px;
        background: #ffffff;
        border-radius: 24px;
        border: 4px solid #4c1d95;
        box-shadow: 6px 6px 0px #4c1d95;
        text-align: center;
    }
    
    .kitty-badge {
        display: inline-block;
        padding: 8px 18px;
        font-size: 15px;
        font-weight: 900;
        border-radius: 30px;
        border: 3px solid #4c1d95;
        box-shadow: 2px 2px 0px #4c1d95;
        margin-bottom: 15px;
        font-family: 'Comic Sans MS', sans-serif;
    }
    
    .kitty-score {
        font-size: 48px;
        font-weight: 900;
        color: #4c1d95;
        font-family: 'Comic Sans MS', sans-serif;
        margin: 5px 0;
    }
    
    .kitty-subtext {
        font-size: 13px;
        color: #701a75;
        font-weight: 600;
    }
    
    /* Custom Styling for Progress Bar to fit the theme */
    .stProgress > div > div > div > div {
        background-color: #ff85a2;
        border-radius: 10px;
    }
    .stProgress {
        border: 3px solid #4c1d95;
        border-radius: 12px;
        height: 22px;
        overflow: hidden;
        background: #fff5f7;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model pipeline securely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model binary: {e}")
    st.stop()

# Wrap whole UI inside a centralized card container block
st.markdown('<div class="kitty-card">', unsafe_allow_html=True)

# Kawaii Kitty Header Bubble
st.markdown("""
    <div class="bubble-header">
        <h1 class="bubble-title">🐾 Kitty Score Predictor 🐾</h1>
        <div class="bubble-subtitle">Let's check your magic score nyaa~! 💕🧁</div>
    </div>
""", unsafe_allow_html=True)

# Vertical Cartoon Inputs
hours_studied = st.number_input(
    "🌸 Study Time (Hours/Day)", 
    min_value=0.0, 
    max_value=24.0, 
    value=6.0, 
    step=0.5,
    help="Time spent working hard every day!"
)

sleep_hours = st.number_input(
    "🎀 Nap Time (Sleep Hours)", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.5, 
    step=0.5,
    help="How long you rest your brain to recharge!"
)

attendance_percent = st.slider(
    "🎒 School Attendance (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=90.0, 
    step=1.0,
    help="Percentage of school days attended!"
)

previous_scores = st.slider(
    "🍭 Past Exam Score", 
    min_value=0.0, 
    max_value=100.0, 
    value=78.0, 
    step=1.0,
    help="Your score from your last test!"
)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# Execution Action State
if st.button("🐾 Calculate Prediction! ✨"):
    # Format structural array payload mapping to model parameters
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Process output matrix scalar
    prediction = float(model.predict(features)[0])
    
    # Determine cute custom kitty badges dynamically
    if prediction >= 85:
        badge_bg, badge_text = "#ffe4e6", "🐱 Pure Purr-fection! 🏆"
    elif prediction >= 60:
        badge_bg, badge_text = "#fce7f3", "😸 Happy Kitty Doing Great! ✨"
    else:
        badge_bg, badge_text = "#fee2e2", "😿 Sweet Kitty Can Do Better! 💪"
        
    # Render cute aesthetic 3D kitty result card
    st.markdown(f"""
        <div class="kitty-result">
            <span class="kitty-badge" style="background-color: {badge_bg}; color: #4c1d95;">
                {badge_text}
            </span>
            <div class="kitty-score">💖 {prediction:.1f} / 100</div>
            <p class="kitty-subtext">Calculated perfectly by your sweet AI companion bot!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Matching pink progress bar animation
    st.progress(min(max(prediction / 100.0, 0.0), 1.0))

st.markdown('</div>', unsafe_allow_html=True)
