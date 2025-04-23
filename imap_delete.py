import imaplib
import email
from email.header import decode_header
from preprocess import clean_text
from train_model import pipeline
import time

# Email credentials (Use App Password for Gmail for security)
EMAIL_USER = "whyarewehere1010@gmail.com"
EMAIL_PASS = "7538mary"

# Connect to Gmail IMAP Server
def connect_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")
    return mail

# Get emails and check for rejection
def fetch_rejection_emails(mail):
    _, messages = mail.search(None, "ALL")  # Fetch all emails
    email_ids = messages[0].split()

    rejection_emails = []

    for email_id in email_ids:
        _, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                # Get email body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                else:
                    body = msg.get_payload(decode=True).decode()

                # Clean and predict
                cleaned_text = clean_text(body)
                prediction = pipeline.predict([cleaned_text])[0]

                if prediction == 1:  # If it's a rejection email
                    rejection_emails.append(email_id)

    return rejection_emails

# Delete rejection emails
def delete_emails(mail, email_ids):
    for email_id in email_ids:
        mail.store(email_id, "+FLAGS", "\\Deleted")
    mail.expunge()  # Permanently delete

# Main function
if __name__ == "__main__":
    mail = connect_email()
    rejection_emails = fetch_rejection_emails(mail)

    if rejection_emails:
        print(f"Deleting {len(rejection_emails)} rejection emails...")
        delete_emails(mail, rejection_emails)
    else:
        print("No rejection emails found.")

    mail.logout()
