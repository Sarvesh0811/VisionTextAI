import streamlit as st
from services.api import send_image
from components.ui import page_header, show_result

page_header()

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    with st.spinner("Processing OCR..."):
        result = send_image(uploaded_file)

    if result["success"]:
        show_result(result["data"])
    else:
        st.error(result["error"])
