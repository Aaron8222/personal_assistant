from client_setup import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message(recipient, subject, text_message):
    CLIENT_SECRET_FILE = 'credentials\client_key.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = text_message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = recipient
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

phone_number = '6172857681@vzwpix.com'
subject = 'Amazon Order'
text_message = 'This is an automated message!'
send_message(phone_number, subject, text_message)