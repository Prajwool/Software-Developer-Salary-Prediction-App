import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page



# Comment out the page config for now to avoid the error
# st.set_page_config(
#     page_title="Salary Prediction App",
#     page_icon="💼",
#     layout="centered"
# )

# Custom CSS to set background colors and styles
st.markdown(
    """
    <style>
    body {
        background-color: #F5F5DC; /* Beige background */
        color: #ADD8E6; /* Baby blue text */
    }
    .welcome-section {
        background: url('path/to/your/image1.jpg') no-repeat center center; /* Image 1 as background */
        background-size: cover;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .option-section {
        background-color: rgba(255, 255, 255, 0.8); /* Light background for option section */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app in a section
st.markdown('<div class="welcome-section"><h1>Welcome to the Salary Prediction App</h1></div>', unsafe_allow_html=True)

# Sidebar for navigation
st.markdown('<div class="option-section">', unsafe_allow_html=True)
page = st.sidebar.selectbox("Choose an option", ("Predict", "Explore"))  # Added "Insert Excel"
st.markdown('</div>', unsafe_allow_html=True)

# Show corresponding page based on selection
if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
