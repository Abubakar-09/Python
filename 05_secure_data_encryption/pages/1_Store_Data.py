import streamlit as st
import os
import json
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

st.set_page_config(
    page_title="Store Data Page",
    page_icon="🧊",
)

st.title("Store Data Page")

DATA_FILE = "data.json"

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


def Get_Key():
    if os.path.exists(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret.key"):
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret.key", "rb") as key_file:
            return key_file.read()


KEY = Get_Key()
text_Hidder = Fernet(KEY)       

def encrypt_data(Mess, Passkey):
    inp = text_Hidder.encrypt(Mess.encode()).decode()

    if os.path.exists(f"{os.path.dirname(os.path.dirname(__file__))}"):
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/National_Secret_Salt.key", "rb") as f:
            salt = f.read()

    inp1 = derive_fernet_key(PassKey,salt)

    if not os.path.exists(f"{os.path.dirname(os.path.dirname(__file__))}/{DATA_FILE}"):
        with open(f"{os.path.dirname(os.path.dirname(__file__))}/{DATA_FILE}", "w") as f:
            json.dump([], f,indent=2)

    with open(f"{os.path.dirname(os.path.dirname(__file__))}/{DATA_FILE}", "r") as f:
        data = json.load(f)

    data.append({"text":f'{inp}',"passkey":f"{inp1}"})
    
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/{DATA_FILE}", "w") as f:
        json.dump(data, f, indent=2)

    st.success(f"Your Message encrypt Form Is = {inp}")        
    

Message = st.text_area("Enter Your Message")
PassKey = st.text_input("Enter Your PassKey")
submit = st.button("Submit It!")

if submit:
    encrypt_data(Message,PassKey)