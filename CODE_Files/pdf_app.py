## MULTILANGUAGE DOCUMENT EXTRACTION WITH GEMINIPRO - SMARTINTERNZ PROJECT BY TEJASWI
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Get the API key from the .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Debugging: Check if the API key is loaded
if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY is missing! Please check your .env file.")
    st.stop()  # Stop execution if API key is missing

# Configure the Gemini AI model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from Gemini AI
def get_gemini_response(input_text, image):
    try:
        if input_text and image:
            response = model.generate_content([input_text, image])
        elif input_text:
            response = model.generate_content(input_text)
        elif image:
            response = model.generate_content(image)
        else:
            return "⚠️ Please provide either text input or an image."
        
        return response.text if response else "⚠️ No response from the model."
    
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction")

st.header("📄 GeminiDecode: Multilanguage Document Text Extraction")
input_text = st.text_input("Enter your text:", key="input")

uploaded_file = st.file_uploader("📷 Upload an image of the document:", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📌 Uploaded Image", use_column_width=True)

submit = st.button("🔍 Analyze Document")

input_prompt = """
You are an expert in understanding invoices.
We will upload an image of an invoice, and you will answer questions based on it.
"""

# Initialize Streamlit app description
st.markdown("""
#### 🌍 About GeminiDecode
Utilizing **Gemini Pro AI**, this project extracts vital information from multilingual documents,
transcending language barriers with precision and efficiency for enhanced productivity and decision-making.
""")

# If submit button is clicked
if submit:
    response = get_gemini_response(input_text, image)

    if response:
        st.subheader("📜 Extracted Text:")
        st.write(response)
    else:
        st.error("⚠️ No response received from the API. Please check your input or try again.")
