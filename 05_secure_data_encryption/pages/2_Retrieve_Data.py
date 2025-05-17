import streamlit as st
import os
import json
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

st.set_page_config(
    page_title="Retreive Data Page",
    page_icon="🧊",
)

st.title("Retrive Data Page")

def derive_fernet_key(passkey: str, salt: bytes, iterations: int = 200_000) -> bytes:
    """
    PBKDF2-HMAC-SHA256 → 32 bytes → base64 urlsafe → valid Fernet key
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    raw_key = kdf.derive(passkey.encode("utf-8"))
    return base64.urlsafe_b64encode(raw_key)


Encrpyt_Mess = st.text_area("Enter Your Encrypted Message Code")
Pass_Key = st.text_input("Enter Your PassKey For The Code")
enter = st.button("Enter")

def Get_Key():
    if os.path.exists(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret.key"):
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret.key", "rb") as key_file:
            return key_file.read()

KEY = Get_Key()
text_Hidder = Fernet(KEY)

def Checker():
    DATA_FILE = 'data.json'
    if os.path.exists(f"{os.path.dirname(os.path.dirname(__file__))}"):
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret_Salt.key", "rb") as f:
            salt = f.read()

    passkey = derive_fernet_key(Pass_Key,salt)
    
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/{DATA_FILE}", "r") as file:
        data = json.load(file)

     # Check for the decrypted message in the data
    found = False
    for record in data:
        if isinstance(record, dict):
            if Encrpyt_Mess in record.values():
                st.success("Decrypted message found in data!")
                found = True
                break

    if not found:
        st.warning("Decrypted message not found in data.")

    derived_key_bytes = derive_fernet_key(Pass_Key, salt)
    derived_key_str = str(derived_key_bytes)

    print(f"Derived Fernet key: {derived_key_str}")

    # Track if a matching passkey is found
    pasfound = False

    for record in data:
        if isinstance(record, dict):
            encrypted_text = record.get("text")
            stored_passkey = record.get("passkey")

            if not encrypted_text or not stored_passkey:
                continue

            if stored_passkey == derived_key_str:
                if st.session_state["attempt"] > 0:
                    st.success("✅ Good — Passkey matched! the Text Description Below!")
                    st.success(text_Hidder.decrypt(Encrpyt_Mess.encode()).decode())
                    pasfound = True
                break  # Exit the loop once matched

    # Show error only if no match was found at all
    if not pasfound:
        if st.session_state["attempt"]>0:
            st.error("❌ Decrypted passkey does not match in the data.")
            st.session_state["attempt"] -= 1
            st.error(f" your Remaining attempt {st.session_state["attempt"]}")
        elif st.session_state["attempt"] <= 0 :
            st.error(f"your Remaining attempt {st.session_state["attempt"]}")
                
        




if enter:
    Checker()

