import streamlit as st
import pickle
import numpy as np

# Set page configuration with a cute flower theme
st.set_page_config(
    page_title="Garden Magic Predictor 🌸",
    page_icon="🧚🌱",
    layout="centered"
)

# 3D Cottagecore Flower Cartoon UI Styling
st.markdown("""
    <style>
    /* Vibrant, cute pastel fairy garden gradient background */
    .stApp {
        background: linear-gradient(135deg, #fef08a 0%, #bbf7d0 50%, #a7f3d0 100%);
    }
    
    /* 3D Soft Clay Outer Card Container with thick cartoon borders */
    .garden-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 30px;
        box-shadow: 
            0px 10px 0px #22c55e,
            0px 20px 30px rgba(34, 197, 94, 0.15);
        border: 4px solid #14532d; /* Deep moss green borders for vintage cartoon look */
        margin-bottom: 25px;
    }
    
    /* Cute Botanical Header Bubble */
    .bubble-header {
        background: #f43f5e; /* Vibrant berry pink */
        border: 4px solid #14532d;
        border-radius: 22px;
        padding: 18px;
        text-align: center;
        box-shadow: 5px 5px 0px #14532d;
        margin-bottom: 35px;
    }
    
    .bubble-title {
        color: #ffffff;
        font-size: 30px;
        font-weight: 900;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        margin: 0;
        text-shadow: 3px 3px 0px #14532d;
    }
    
    .bubble-subtitle {
        color: #ffe4e6;
        font-size: 14px;
        font-weight: 700;
        margin-top: 5px;
        letter-spacing: 0.5px;
    }
    
    /* Transforming Input Blocks into 3D Cartoon Panels */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #f0fdf4 !important; /* Soft meadow green tint */
        padding: 18px !important;
        border-radius: 20px !important;
        border: 3px solid #14532d !important;
        box-shadow: 4px 4px 0px #14532d !important;
        margin-bottom: 24px !important;
        transition: transform 0.1s ease !important;
    }
    
    div[data-testid="stNumberInput"]:focus-within, div[data-testid="stSlider"]:focus-within {
        transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px #14532d !important;
        background: #ffffff !important;
    }
    
    /* Chunky 3D Cartoon Magic Button */
    .stButton > button {
        width: 100%;
        background: #ec4899; /* Bright pink */
        color: #ffffff !important;
        border: 4px solid #14532d;
        border-radius: 20px;
        padding: 16px 24px;
        font-size: 20px;
        font-weight: 900;
        font-family: 'Comic Sans MS', sans-serif;
        box-shadow: 0px 6px 0px #14532d;
        transition: all 0.1s ease;
    }
    
    .stButton > button:hover {
        background: #db2777;
        color: #ffffff !important;
        transform: translateY(2px);
        box-shadow: 0px 4px 0px #14532d;
    }
    
    .stButton > button:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #14532d;
    }
    
    /* Aesthetic 3D Result Box */
    .garden-result {
        margin-top: 30px;
        padding: 25px;
        background: #ffffff;
        border-radius: 24px;
        border: 4px solid #14532d;
        box-shadow: 6px 6px 0px #14532d;
        text-align: center;
    }
    
    .garden-badge {
        display: inline-block;
        padding: 8px 18px;
        font-size: 15px;
        font-weight: 900;
        border-radius: 30px;
        border: 3px solid #14532d;
        box-shadow: 2px 2px 0px #14532d;
        margin-bottom: 15px;
        font-family: 'Comic Sans MS', sans-serif;
    }
    
    .garden-score {
        font-size: 48px;
        font-weight: 900;
        color: #14532d;
        font-family: 'Comic Sans MS', sans-serif;
        margin: 5px 0;
    }
    
    .garden-subtext {
        font-size: 13px;
        color: #166534;
        font-weight: 600;
    }
    
    /* Styled Progress Bar to fit the flower aesthetic */
    .stProgress > div > div > div > div {
        background-color: #f43f5e;
        border-radius: 10px;
    }
    .stProgress {
        border: 3px solid #14532d;
        border-radius: 12px;
        height: 22px;
        overflow: hidden;
        background: #f0fdf4;
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
st.markdown('<div class="garden-card">', unsafe_allow_html=True)

# Cute Floral Cartoon Header Bubble
st.markdown("""
    <div class="bubble-header">
        <h1 class="bubble-title">🍀 Study Blossom AI 🌸</h1>
        <div class="bubble-subtitle">Let's watch your future grade bloom! 🌷✨🎈</div>
    </div>
""", unsafe_allow_html=True)

# Vertical Cartoon Inputs
hours_studied = st.number_input(
    "🌻 Nurture Time (Study Hours/Day)", 
    min_value=0.0, 
    max_value=24.0, 
    value=6.0, 
    step=0.5,
    help="Time spent watering your brain daily!"
)

sleep_hours = st.number_input(
    "🍄 Dreaming Time (Sleep Hours)", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.5, 
    step=0.5,
    help="Rest hours under the magic mushroom patch!"
)

attendance_percent = st.slider(
    "🌿 Garden Presence (Attendance %)", 
    min_value=0.0, 
    max_value=100.0, 
    value=90.0, 
    step=1.0,
    help="Percentage of classroom days present!"
)

previous_scores = st.slider(
    "🍇 Last Harvest (Past Exam Score)", 
    min_value=0.0, 
    max_value=100.0, 
    value=78.0, 
    step=1.0,
    help="Your yield from the last test cycle!"
)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# Execution Action State
if st.button("🔮 Cast Prediction Spell! ✨"):
    # Format structural array payload mapping to model parameters
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Process output matrix scalar
    prediction = float(model.predict(features)[0])
    
    # Determine cute custom floral badges dynamically
    if prediction >= 85:
        badge_bg, badge_text = "#dcfce7", "💐 Full Bloom Brilliance! 🏆"
    elif prediction >= 60:
        badge_bg, badge_text = "#fef9c3", "🌿 Healthy Sprout Growing! ✨"
    else:
        badge_bg, badge_text = "#fee2e2", "🌱 Needs More Sunshine! 💪"
        
    # Render cute aesthetic 3D result card
    st.markdown(f"""
        <div class="garden-result">
            <span class="garden-badge" style="background-color: {badge_bg}; color: #14532d;">
                {badge_text}
            </span>
            <div class="garden-score">🌸 {prediction:.1f} / 100</div>
            <p class="garden-subtext">Calculated perfectly by your magical forest helper bot!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Matching progress bar animation
    st.progress(min(max(prediction / 100.0, 0.0), 1.0))

st.markdown('</div>', unsafe_allow_html=True)
