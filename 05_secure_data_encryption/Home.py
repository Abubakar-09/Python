import streamlit as st

st.set_page_config(
    page_title="🔐 Secure Data Encryption System",
    page_icon="LoL",
)
st.session_state["attempt"] = 3

st.title("🔐 Secure Data Encryption System")
st.subheader("🏠 Welcome to the Secure Vault")
st.markdown("""
    Use this app to:
    - 🔒 **Encrypt and store data** with a unique passkey
    - 🔓 **Retrieve and decrypt** using your passkey
    - 🚫 Lockout after 3 wrong attempts
""")