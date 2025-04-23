import joblib
from preprocess import clean_text

# Load trained model and label encoder
pipeline = joblib.load("email_classifier_pipeline.pkl")  # ✅ Fixed filename
label_encoder = joblib.load("label_encoder.pkl")

def predict_email(email_text):
    """
    Predicts whether an email is a rejection letter or not.
    
    Args:
        email_text (str): The email content
    Returns:
        str: "Rejection Email" or "Normal Email"
    """
    cleaned_text = clean_text(email_text)
    prediction = pipeline.predict([cleaned_text])[0]
    
    # Decode label
    label = label_encoder.inverse_transform([prediction])[0]
    return "Rejection Email" if label == "rejection" else "Normal Email"

# Test Sample Email
sample_email = "Dear Applicant, you passed"
result = predict_email(sample_email)
print(f"Prediction: {result}")
