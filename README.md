
# **Rejection Email Filter & Auto-Delete Project** 

This project builds an email classification system that uses a machine learning model to detect and filter rejection emails from Gmail or Outlook. Upon detecting a rejection email, the system can automatically delete the email using IMAP or the Gmail API. The project is split into three main components: **Model Training**, **Email Classification**, and **Automatic Deletion**.

---

## **Table of Contents** 
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation Instructions](#installation-instructions)
5. [Training the Model](#training-the-model)
6. [Email Prediction](#email-prediction)
7. [Auto-Delete Email Feature](#auto-delete-email-feature)
8. [File Structure](#file-structure)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Project Overview** 
The Rejection Filter system is designed to classify incoming emails as either **"Rejection Emails"** or **"Normal Emails"**. It uses Natural Language Processing (NLP) techniques to clean, process, and analyze the email content, using a pre-trained machine learning model to make predictions. When the model detects a rejection email, it can trigger the automatic deletion of the email from Gmail or Outlook accounts.

---

## **Features** 
- **Email Classification**: Classifies emails as either **Rejection Email** or **Normal Email** using a machine learning model.
- **Automatic Deletion**: Automatically deletes rejection emails from Gmail or Outlook inboxes via IMAP or Gmail API.
- **Customizable**: The system can be extended to detect different types of emails based on specific keywords or phrases.
- **Email Data Preprocessing**: Text data is cleaned, and rejection-specific phrases are used to enhance model accuracy.
- **Saved Model & Label Encoder**: Saves the trained model and label encoder for easy reuse.

---

## **Requirements** ⚙️
To run this project, you will need:
- **Python 3.7+**
- **Libraries**: `pandas`, `sklearn`, `joblib`, `numpy`, `imaplib`, `gmail-api`, `email`, `re`, `tensorflow` (optional depending on models used).
- **A Gmail/Outlook account** (with IMAP enabled).
- **2-Step Verification enabled for Gmail** (required to generate App Passwords for Gmail).

---

## **Installation Instructions** 

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/rejection-filter.git
cd rejection-filter
```

### Step 2: Create and Activate a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up Gmail API or IMAP Access
- **For Gmail**: Enable [Gmail API](https://developers.google.com/gmail/api/quickstart/python) and create a `credentials.json` file. Follow the instructions to set up OAuth and obtain your credentials.
- **For IMAP Access**: Enable IMAP in your Gmail settings and ensure you have an App Password if 2FA is enabled.

---

## **Training the Model** 
1. **Preprocess Email Data**: The script `train_model.py` cleans and preprocesses the email data by removing unnecessary characters, normalizing the text, and adding rejection-related features.
2. **Train the Model**: 
    - The model is trained using the **Naive Bayes** classifier to predict rejection emails.
    - It uses **TF-IDF Vectorizer** to convert email text into numerical features.
3. **Model Saving**: The trained model and label encoder are saved using **joblib** in files `email_classifier_pipeline.pkl` and `label_encoder.pkl` respectively.

### Run the Training Script:
```bash
python train_model.py
```
This will:
- Preprocess the email data.
- Train the model using the provided dataset (`emails.csv`).
- Save the trained model and encoder for later use.

---

## **Email Prediction** 
Once the model is trained, you can use the trained model to classify incoming emails. The `predict.py` script loads the model and label encoder, and provides an interface to predict whether an email is a rejection or normal.

### Run the Prediction Script:
```bash
python predict.py
```
You will need to provide the email content, and the script will output:
- **"Rejection Email"** or **"Normal Email"** based on the prediction.

---

## **Auto-Delete Email Feature** 

The `imap_delete.py` script connects to your Gmail or Outlook account via IMAP, reads incoming emails, classifies them, and deletes the rejection emails.

### **IMAP Email Deletion:**
- **IMAP**: This approach connects to your email account via IMAP, fetches the emails, classifies them using the model, and deletes rejection emails automatically.
- **Authentication**: You will need to generate an **App Password** (for Gmail) or provide your login credentials (for IMAP).
  
### Run the Auto-Delete Script:
```bash
python imap_delete.py
```
This will:
- Connect to your email account.
- Fetch and classify the latest emails.
- Delete the rejection emails based on the model's prediction.

---

## **File Structure** 

```
rejection-filter/
├── imap_delete.py            # Script for deleting rejection emails from Gmail/Outlook
├── train_model.py            # Script for training the classification model
├── predict.py                # Script for predicting whether an email is rejection or normal
├── preprocess.py             # Data preprocessing and feature extraction (text cleaning, etc.)
├── emails.csv                # Dataset of emails for training
├── requirements.txt          # Python dependencies
├── email_classifier_pipeline.pkl # Trained machine learning model
├── label_encoder.pkl         # Saved label encoder
└── README.md                 # This file
```

---

## **Contributing** 
If you would like to contribute to this project:
1. Fork the repository.
2. Clone your forked repository locally.
3. Create a new branch for your feature or bug fix.
4. Write tests to verify your changes.
5. Submit a pull request.

---

## **License** 

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## **Acknowledgments** 

- **sklearn** for the machine learning tools.
- **Google API** for enabling Gmail interaction.
- **IMAP** protocol for seamless email processing.

---

### Need Help? 

If you encounter any issues, feel free to open an issue in the repository, and I’ll get back to you ASAP!

---
