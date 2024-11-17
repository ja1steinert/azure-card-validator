# Credit Card Validator
A Streamlit-based application that integrates with Azure AI Document Intelligence and Blob Storage to securely upload files, validate credit card information from images, and display results in an intuitive interface.

## Installation and Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/ja1steinert/azure-card-validator.git
   ```
2. Navigate to directory:
   ```bash
   cd azure-card-validator
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your credentials in the .env file:
   ```bash
    ENDPOINT = "YOUR_ENDPOINT"
    SUBSCRIPTION_KEY = "YOUR_SUBSCRIPTION_KEY"
    AZURE_STORAGE_CONNECTION_STRING = "YOUR_CONNECTION_STRING"
    CONTAINER_NAME = "YOUR_CONTAINER_NAME"
   ```
5. Run the program:
   ```bash
   python src/app.py
   ```
