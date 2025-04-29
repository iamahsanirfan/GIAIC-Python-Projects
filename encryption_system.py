import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Initialize session state variables
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'cipher' not in st.session_state:
    key = Fernet.generate_key()
    st.session_state.cipher = Fernet(key)

# Function to encrypt data
def encrypt_data(text):
    return st.session_state.cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text):
    return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted_text = encrypt_data(user_data)
            hashed_passkey = hash_passkey(passkey)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data stored securely!")
            st.write("**Your encrypted data is:**")
            st.code(encrypted_text)
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            hashed_passkey = hash_passkey(passkey)
            # Check if encrypted text exists and passkey matches
            if encrypted_text in st.session_state.stored_data:
                entry = st.session_state.stored_data[encrypted_text]
                if entry["passkey"] == hashed_passkey:
                    decrypted_text = decrypt_data(encrypted_text)
                    st.session_state.failed_attempts = 0
                    st.success(f"✅ Decrypted Data: {decrypted_text}")
                else:
                    st.session_state.failed_attempts += 1
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {remaining}")
                    if st.session_state.failed_attempts >= 3:
                        st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                        st.session_state.failed_attempts = 0
                        st.experimental_rerun()
            else:
                st.error("❌ Encrypted data not found!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Hardcoded for demo purposes
            st.session_state.failed_attempts = 0
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")