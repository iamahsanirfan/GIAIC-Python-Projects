import re

COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "abc123", "111111", "letmein", "123123",
    "iloveyou", "admin", "welcome", "monkey", "football", "1234", "passw0rd"
}

def checkPasswordStrength(password):
    score = 0  
    feedback = []

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        return "Too Common ❌", ["This password is commonly used. Choose a more secure one."], "red"

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Numbers check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Use special characters like !@#$%^&*.")

    # Determine strength level
    if score == 4:
        strength = "Strong 🔥"
        color = "green"
    elif score == 3:
        strength = "Moderate ⚠️"
        color = "orange"
    else:
        strength = "Weak ❌"
        color = "red"

    return strength, feedback, color

import streamlit as st

st.title("🔑 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, feedback, color = checkPasswordStrength(password)

    st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)

    if feedback:
        st.warning("Suggestions to improve:")
        for tip in feedback:
            st.write("- " + tip)