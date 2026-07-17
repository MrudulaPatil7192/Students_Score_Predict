import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>

.main{
background: linear-gradient(135deg,#f5f7fa,#c3cfe2);
}

.title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#1f3b73;
}

.sub{
text-align:center;
font-size:20px;
color:gray;
margin-bottom:30px;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#4CAF50,#2196F3);
color:white;
font-size:20px;
border-radius:12px;
height:3.2em;
border:none;
}

.stButton>button:hover{
background:linear-gradient(90deg,#2196F3,#4CAF50);
}

.prediction{
padding:25px;
border-radius:15px;
background:#ffffff;
box-shadow:0px 0px 20px rgba(0,0,0,0.2);
text-align:center;
font-size:28px;
font-weight:bold;
color:#1b5e20;
}

.footer{
text-align:center;
color:gray;
padding-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load Model
# ---------------------------
@st.cache_resource
def load_model():
    with open("model.pkl","rb") as file:
        model=pickle.load(file)
    return model

model=load_model()

# ---------------------------
# Header
# ---------------------------

st.markdown("<div class='title'>🎓 Student Performance Predictor</div>",unsafe_allow_html=True)

st.markdown("<div class='sub'>Predict Student Performance using Machine Learning</div>",unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png",width=120)

st.sidebar.title("About")

st.sidebar.info("""
This application predicts the student's expected score based on:

✔ Hours Studied

✔ Sleep Hours

✔ Attendance %

✔ Previous Scores

Model Used:
KNeighborsRegressor
""")

# ---------------------------
# Layout
# ---------------------------

col1,col2=st.columns(2)

with col1:

    hours=st.slider(
        "📚 Hours Studied",
        0.0,
        15.0,
        5.0,
        0.5)

    sleep=st.slider(
        "😴 Sleep Hours",
        0.0,
        12.0,
        7.0,
        0.5)

with col2:

    attendance=st.slider(
        "🏫 Attendance %",
        0,
        100,
        75)

    previous=st.slider(
        "📝 Previous Scores",
        0,
        100,
        70)

st.write("")

if st.button("🚀 Predict Performance"):

    features=np.array([[hours,sleep,attendance,previous]])

    prediction=model.predict(features)[0]

    st.balloons()

    st.markdown(
        f"""
        <div class='prediction'>
        Predicted Score<br><br>
        {prediction:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>",unsafe_allow_html=True)
