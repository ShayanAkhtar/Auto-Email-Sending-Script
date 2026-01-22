import smtplib
import time
from email.message import EmailMessage

# ================= CONFIG ================= #
SENDER_EMAIL = "your_gmail"
APP_PASSWORD = "your_app_password"
CV_PATH = "path_to_cv_pdf"

SUBJECT = "your_subject"

EMAIL_BODY = """ Your Email Body """

# ================= List Of Reciver Emails ================= #
RECIPIENTS = [
    "receiver1@gmail.com",
    "receiver2@gmail.com",
    "receiver3@gmail.com",
]


# ============== EMAIL SENDER ============== #
def send_email(to_email):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = SUBJECT
    msg.set_content(EMAIL_BODY)

    with open(CV_PATH, "rb") as cv:
        msg.add_attachment(
            cv.read(), maintype="application", subtype="pdf", filename=CV_PATH
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)


# ============== MAIN LOOP ================= #
for index, email in enumerate(RECIPIENTS, start=1):
    try:
        send_email(email)
        print(f"[{index}] Email sent successfully to {email}")
        time.sleep(10)
    except Exception as e:
        print(f"[ERROR] Failed to send to {email}: {e}")
