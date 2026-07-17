import streamlit as st
import pickle
import numpy as np

# Set page configuration with a cute emoji
st.set_page_config(
    page_title="Study Buddy AI",
    page_icon="✨",
    layout="centered"
)

# 3D Claymorphism / Cute Cartoon UI Styling
st.markdown("""
    <style>
    /* Playful pastel gradient background */
    .stApp {
        background: linear-gradient(135deg, #fef08a 0%, #d9f99d 50%, #a7f3d0 100%);
    }
    
    /* 3D Soft Clay Outer Card Container */
    .cute-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 28px;
        box-shadow: 
            0px 10px 0px #e2e8f0,
            0px 20px 30px rgba(100, 116, 139, 0.15);
        border: 4px solid #000000;
        margin-bottom: 25px;
    }
    
    /* Cartoon Header Bubble */
    .bubble-header {
        background: #818cf8;
        border: 4px solid #000000;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        box-shadow: 4px 4px 0px #000000;
        margin-bottom: 30px;
    }
    
    .bubble-title {
        color: #ffffff;
        font-size: 28px;
        font-weight: 900;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        margin: 0;
    }
    
    .bubble-subtitle {
        color: #e0e7ff;
        font-size: 13px;
        font-weight: 700;
        margin-top: 4px;
        letter-spacing: 0.5px;
    }
    
    /* Transforming Input Blocks into 3D Cartoon Cards */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #f8fafc !important;
        padding: 18px !important;
        border-radius: 18px !important;
        border: 3px solid #000000 !important;
        box-shadow: 4px 4px 0px #000000 !important;
        margin-bottom: 24px !important;
        transition: transform 0.1s ease !important;
    }
    
    div[data-testid="stNumberInput"]:focus-within, div[data-testid="stSlider"]:focus-within {
        transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px #000000 !important;
        background: #fff !important;
    }
    
    /* Chunky 3D Cartoon Button */
    .stButton > button {
        width: 100%;
        background: #fb923c;
        color: #ffffff !important;
        border: 4px solid #000000;
        border-radius: 18px;
        padding: 15px 24px;
        font-size: 18px;
        font-weight: 900;
        font-family: 'Comic Sans MS', sans-serif;
        box-shadow: 0px 6px 0px #000000;
        transition: all 0.1s ease;
    }
    
    .stButton > button:hover {
        background: #f97316;
        color: #ffffff !important;
        transform: translateY(2px);
        box-shadow: 0px 4px 0px #000000;
    }
    
    .stButton > button:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #000000;
    }
    
    /* Aesthetic 3D Result Viewport */
    .cute-result {
        margin-top: 30px;
        padding: 25px;
        background: #ffffff;
        border-radius: 22px;
        border: 4px solid #000000;
        box-shadow: 6px 6px 0px #000000;
        text-align: center;
    }
    
    .cute-badge {
        display: inline-block;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 900;
        border-radius: 30px;
        border: 3px solid #000000;
        box-shadow: 2px 2px 0px #000000;
        margin-bottom: 15px;
        font-family: 'Comic Sans MS', sans-serif;
    }
    
    .cute-score {
        font-size: 46px;
        font-weight: 900;
        color: #000000;
        font-family: 'Comic Sans MS', sans-serif;
        margin: 5px 0;
    }
    
    .cute-subtext {
        font-size: 13px;
        color: #64748b;
        font-weight: 600;
    }
    
    /* Custom Stylings for Progress Bar to fit aesthetic */
    .stProgress > div > div > div > div {
        background-color: #4ade80;
        border-radius: 10px;
    }
    .stProgress {
        border: 3px solid #000000;
        border-radius: 12px;
        height: 20px;
        overflow: hidden;
        background: #f1f5f9;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model pipeline 
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

# Wrap whole UI inside a centralized cute container block
st.markdown('<div class="cute-card">', unsafe_allow_html=True)

# Cartoon Header Bubble
st.markdown("""
    <div class="bubble-header">
        <h1 class="bubble-title">✨ Study Buddy AI ✨</h1>
        <div class="bubble-subtitle">Let's guess your next score! 🧠🎈</div>
    </div>
""", unsafe_allow_html=True)

# Vertical Cartoon Inputs
hours_studied = st.number_input(
    "📖 Daily Study Time (Hours)", 
    min_value=0.0, 
    max_value=24.0, 
    value=6.0, 
    step=0.5,
    help="Hours hitting the books each day!"
)

sleep_hours = st.number_input(
    "😴 Cozy Sleep Time (Hours)", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.5, 
    step=0.5,
    help="How long you rest your brain every night."
)

attendance_percent = st.slider(
    "🎒 Class Attendance (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=90.0, 
    step=1.0,
    help="Percentage of days you made it to class!"
)

previous_scores = st.slider(
    "🌈 Last Exam Score", 
    min_value=0.0, 
    max_value=100.0, 
    value=78.0, 
    step=1.0,
    help="What did you get on your previous test?"
)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# Execution Action State
if st.button("🔮 Calculate Magic Score! 🔮"):
    # Format structural payload matching model
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Process output matrix scalar
    prediction = float(model.predict(features)[0])
    
    # Determine cartoon badges dynamically
    if prediction >= 85:
        badge_bg, badge_text = "#bbf7d0", "🌟 Superstar Student! 🌟"
    elif prediction >= 60:
        badge_bg, badge_text = "#bfdbfe", "⭐ Doing Great! ⭐"
    else:
        badge_bg, badge_text = "#fecdd3", "🌱 You Got This! Keep Going 🌱"
        
    # Render cute aesthetic 3D result card
    st.markdown(f"""
        <div class="cute-result">
            <span class="cute-badge" style="background-color: {badge_bg};">
                {badge_text}
            </span>
            <div class="cute-score">🎉 {prediction:.1f} / 100</div>
            <p class="cute-subtext">Calculated perfectly by your friendly AI neighborhood predictor bot!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Matching cute progress bar animation
    st.progress(min(max(prediction / 100.0, 0.0), 1.0))

st.markdown('</div>', unsafe_allow_html=True)
