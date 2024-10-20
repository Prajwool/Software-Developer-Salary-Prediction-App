import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# Load the Model and Encoders
@st.cache_resource
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Define the Prediction Function
def predict_salary(country, education, years_experience):
    input_data = pd.DataFrame({
        'Country': [country],
        'EdLevel': [education],
        'YearsCodePro': [years_experience]
    })
    
    try:
        input_data['Country'] = le_country.transform(input_data['Country'])
        input_data['EdLevel'] = le_education.transform(input_data['EdLevel'])
    except ValueError as e:
        st.error(f"Error in transforming input data: {e}")
        return None
    
    input_data = input_data.astype(float)
    prediction = regressor.predict(input_data)
    return prediction[0]

# Design the Predict Page
def show_predict_page():
    try:
        image = Image.open('header_image.png')  # Ensure this image exists in your directory
        st.image(image, use_column_width=True)
    except FileNotFoundError:
        st.write("")  # If image not found, skip

    st.title("💼 Software Developer Salary Prediction")
    st.markdown("""### Enter the details below to predict the estimated salary of a software developer.""")

    with st.form(key='salary_prediction_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            countries = (
                "United States",
                "India",
                "United Kingdom",
                "Germany",
                "Canada",
                "Brazil",
                "France",
                "Spain",
                "Australia",
                "Netherlands",
                "Poland",
                "Italy",
                "Russian Federation",
                "Sweden",
            )
            country = st.selectbox("🌍 Country", countries, help="Select the country of employment.")
        
        with col2:
            education_levels = (
                "Less than a Bachelors",
                "Bachelor’s degree",
                "Master’s degree",
                "Post grad",
            )
            education = st.selectbox("🎓 Education Level", education_levels, help="Select your highest education level.")
        
        years_experience = st.slider(
            "🧑‍💻 Years of Professional Experience",
            min_value=0,
            max_value=50,
            value=3,
            step=1,
            help="Select the number of years you have been working professionally."
        )
        
        submit_button = st.form_submit_button(label='🚀 Predict Salary')

    if submit_button:
        with st.spinner('Predicting...'):
            salary = predict_salary(country, education, years_experience)
        
        if salary:
            st.success(f"### The estimated salary is **${salary:,.2f}** 💰")
        else:
            st.error("Unable to make a prediction. Please check your inputs.")

    st.markdown("""---""")
    st.markdown("© 2024 Salary Prediction App")

# Main Execution
def main():
    show_predict_page()

if __name__ == "__main__":
    main()
