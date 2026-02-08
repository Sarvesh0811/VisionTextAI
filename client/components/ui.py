import streamlit as st


def page_header():
    st.set_page_config(
        page_title="OCR System",
        layout="centered"
    )

    st.title("📄 AI OCR & Translation System")
    st.markdown("Upload an image to extract and translate text.")


def show_result(result):

    st.subheader("🔹 Raw OCR")
    st.code(result["raw_ocr"])

    st.subheader("🔹 English Translation")
    st.code(result["english_translation"])
