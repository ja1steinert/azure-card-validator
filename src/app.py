import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Azure Document Validation - Secure File Upload and Credit Card Analysis")
    uploaded_file = st.file_uploader("Select a file", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_name = uploaded_file.name
        st.info("Uploading file...")
        blob_url = upload_blob(uploaded_file, file_name)
        
        if blob_url:
            st.success(f"File '{file_name}' successfully uploaded to Azure Blob Storage.")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error(f"Failed to upload the file '{file_name}' to Azure Blob Storage.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Uploaded Image", use_column_width=True)
    st.subheader("Validation Result:")
    
    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color: green;'>Valid Credit Card</h1>", unsafe_allow_html=True)
        st.write(f"Cardholder Name: {credit_card_info['card_name']}")
        st.write(f"Issuing Bank: {credit_card_info['bank_name']}")
        st.write(f"Expiry Date: {credit_card_info['expiry_date']}")
    else:
        st.markdown("<h1 style='color: red;'>Invalid Credit Card</h1>", unsafe_allow_html=True)
        st.warning("The uploaded image does not contain a valid credit card.")

if __name__ == "__main__":
    configure_interface()
