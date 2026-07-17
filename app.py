import streamlit as st
import pickle
import numpy as np

# Set premium page configuration
st.set_page_config(
    page_title="Performance Analytics AI",
    page_icon="⚡",
    layout="centered"
)

# Advanced CSS for Glassmorphism, structural card shadows, and smooth micro-interactions
st.markdown("""
    <style>
    /* Global background gradient */
    .stApp {
        background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%);
    }
    
    /* Core app shell card */
    .app-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.8);
        margin-bottom: 25px;
    }
    
    /* Glassmorphic Title Header */
    .glass-header {
        background: rgba(79, 70, 229, 0.06);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(79, 70, 229, 0.15);
        text-align: center;
        margin-bottom: 30px;
    }
    
    .glass-title {
        color: #1e1b4b;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
    }
    
    .glass-subtitle {
        color: #6366f1;
        font-size: 14px;
        font-weight: 600;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Interactive Hover Styling for Input Wrappers */
    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        background: #ffffff !important;
        padding: 20px !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02) !important;
        border: 1px solid #e2e8f0 !important;
        margin-bottom: 22px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-testid="stNumberInput"]:focus-within, div[data-testid="stSlider"]:focus-within {
        transform: translateY(-2px);
        border-color: #6366f1 !important;
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.08) !important;
    }
    
    /* High-fidelity interactive button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 14px 24px;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.25);
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.35);
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
    }
    
    .stButton > button:active {
        transform: scale(0.99);
    }
    
    /* Premium Interactive Result Display */
    .result-container {
        margin-top: 30px;
        padding: 25px;
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    
    .metric-badge {
        display: inline-block;
        padding: 6px 14px;
        background: #ecfdf5;
        color: #059669;
        font-size: 12px;
        font-weight: 700;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }
    
    .score-output {
        font-size: 42px;
        font-weight: 900;
        color: #1e1b4b;
        margin: 5px 0;
    }
    
    .status-text {
        font-size: 14px;
        color: #6b7280;
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

# Wrap whole UI inside a centralized, structurally clean container block
st.markdown('<div class="app-card">', unsafe_allow_html=True)

# Glassmorphic Banner Header 
st.markdown("""
    <div class="glass-header">
        <h1 class="glass-title">Predictive Student Analytics</h1>
        <div class="glass-subtitle">Machine Learning Engine v1.6</div>
    </div>
""", unsafe_allow_html=True)

# Sequential Input Fields with interactive placeholder helpers
hours_studied = st.number_input(
    "📚 Daily Study Commitment", 
    min_value=0.0, 
    max_value=24.0, 
    value=6.0, 
    step=0.5,
    help="How many hours does the student allocate strictly to studying per day?"
)

sleep_hours = st.number_input(
    "😴 Nightly Rest Duration", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.5, 
    step=0.5,
    help="Average duration of sleep recorded nightly."
)

attendance_percent = st.slider(
    "🏫 Institutional Attendance Profile", 
    min_value=0.0, 
    max_value=100.0, 
    value=90.0, 
    step=1.0,
    help="Overall class attendance percentage recorded over the current semester."
)

previous_scores = st.slider(
    "📊 Prior Academic Standing", 
    min_value=0.0, 
    max_value=100.0, 
    value=78.0, 
    step=1.0,
    help="The target student's absolute score in their immediate past evaluation cycle."
)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# Execution Action State
if st.button("Analyze & Compute Grade"):
    # Format structural array payload mapping to ['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores']
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    # Process output matrix scalar
    prediction = float(model.predict(features)[0])
    
    # Determine visual category metrics based on predicted output value dynamically
    if prediction >= 85:
        badge_color, badge_text = "#ecfdf5", "#059669", "Excellent Standing"
    elif prediction >= 60:
        badge_color, badge_text = "#eff6ff", "#2563eb", "Good Standing"
    else:
        badge_color, badge_text = "#fef2f2", "#dc2626", "Needs Focus"
        
    # Render new dynamic analytics viewport card complete with shadow and color transitions
    st.markdown(f"""
        <div class="result-container">
            <span class="metric-badge" style="background-color: {badge_color}; color: {badge_text[1]};">
                {badge_text[2]}
            </span>
            <div class="score-output">{prediction:.1f} / 100</div>
            <p class="status-text">Based on KNN algorithmic mapping of local variance and study metrics.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Fully interactive companion widget (Streamlit native progress bar reacting directly to prediction metrics)
    st.progress(min(max(prediction / 100.0, 0.0), 1.0))

st.markdown('</div>', unsafe_allow_html=True)
