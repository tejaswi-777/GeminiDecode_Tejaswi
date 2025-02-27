#SmartInternz Project
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()##load all the environtment variables
genai.configure(api_key="enter your api key. not posting here as it is confidential.")

model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input, image):
    if input!="":
       response=model.generate_content([input, image])
    else:
        response=model.generatie_content(image)   
    return response.text

st.set_page_config(page_title="GeminiDecode:Multilanguage Document Extraction using GeminiPro by Tejaswi")

st.header("GeminiDecode: Multilanguage Document Text Extraction by Tejaswi Tripuraneni")
input = st.text_input("Input : ", key = "input")

uploaded_file=st.file_uploader("choose an image of the document:", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_container_width=True)
submit=st.button("SUBMIT")   

input_prompt="""
You are expert in understanding invoices.
We will upload a image as invoice and you will have to answer any questions based on the uploaded invoice image.
""" 

#initialize streamlit app
st.header("GeminiDecode: Multilanguage Document Extraction Project")
text="Utilizing Gemini Pro AI,this project effortlessly extracts vital information + \
from diverse multilingual documents, transcending language barriers with \nprecision and + \
efficiency for enchanced  productivity and decision making."
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)


## If submit button is clicked
if submit:
    response = get_gemini_response(input, image)
    
    # Check if response is valid before displaying
    if response:
        st.subheader("The Output Is:")
        st.write(response)
    else:
        st.error("No response received from the API. Please check your input or try again.")
