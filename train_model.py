import pandas as pd
from sklearn.preprocessing import LabelEncoder
from preprocess import clean_text
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load Data
df = pd.read_csv("emails.csv")

# Clean emails
df['cleaned_email'] = df['email'].apply(clean_text)

# Feature Extraction - Count Rejection Phrases
def extract_rejection_features(text):
    rejection_phrases = [
        'regret to inform', 'not selected', 'unfortunately', 
        'we are sorry', 'cannot offer', 'not move forward',
        'not progress', 'declined'
    ]
    rejection_count = sum(1 for phrase in rejection_phrases if phrase in text.lower())
    return rejection_count

df['rejection_score'] = df['cleaned_email'].apply(extract_rejection_features)

# Encode Labels
le = LabelEncoder()
df['label_encoded'] = le.fit_transform(df['label'])  # ✅ Fixed

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    df[["cleaned_email", "rejection_score"]], 
    df["label_encoded"], 
    test_size=0.2, 
    stratify=df["label_encoded"], 
    random_state=42
)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1,3), max_features=5000, stop_words='english')

# Model Pipeline
pipeline = Pipeline([
    ('tfidf', vectorizer),
    ('classifier', MultinomialNB(alpha=1.0))
])  # 

# Train Model
pipeline.fit(X_train["cleaned_email"], y_train)  # Only pass text, not both features

# Predictions
y_pred = pipeline.predict(X_test["cleaned_email"])  # Convert to array

# Enhanced Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

print("\n🔍 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save Model and Encoder
joblib.dump(pipeline, "email_classifier_pipeline.pkl")
joblib.dump(le, "label_encoder.pkl")
print(" Model and Label Encoder saved successfully!")
