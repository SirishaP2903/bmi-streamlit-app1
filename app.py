import streamlit as st
import pandas as pd
import os

# ---------- Function to calculate BMI ----------
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# ---------- Function to get BMI Category ----------
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# ---------- Meal & Exercise Suggestions ----------
def suggestions(category):
    if category == "Underweight":
        meal = "High-protein meals, nuts, milk, eggs, peanut butter"
        exercise = "Light strength training, yoga"
    elif category == "Normal":
        meal = "Balanced diet with vegetables, fruits, proteins"
        exercise = "Brisk walking, jogging, cycling"
    elif category == "Overweight":
        meal = "Low-carb meals, more vegetables, lean protein"
        exercise = "Walking, swimming, light cardio"
    else:
        meal = "Low-calorie diet, avoid sugar & processed food"
        exercise = "Cardio exercises, light strength training"
    return meal, exercise

# ---------- Streamlit UI ----------
st.title("BMI Calculator App")

name = st.text_input("Enter your Name")
age = st.number_input("Enter your Age", min_value=1, max_value=120)
gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
height = st.number_input("Enter your Height (cm)", min_value=1.0)
weight = st.number_input("Enter your Weight (kg)", min_value=1.0)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    meal, exercise = suggestions(category)

    st.success(f"Your BMI is {bmi}")
    st.info(f"Category: {category}")
    st.write("### Meal Suggestion")
    st.write(meal)
    st.write("### Exercise Suggestion")
    st.write(exercise)

    # Save Data
    data = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Height": height,
        "Weight": weight,
        "BMI": bmi,
        "Category": category
    }

    df = pd.DataFrame([data])

    if os.path.exists("bmi_data.csv"):
        df.to_csv("bmi_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("bmi_data.csv", index=False)

    st.success("Data saved successfully!")