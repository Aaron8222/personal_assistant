from client_setup import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import os

def send_message(recipient, subject, text_message, attachments):
    CLIENT_SECRET_FILE = 'credentials\client_key.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = text_message
    mime_message = MIMEMultipart()
    mime_message['to'] = recipient
    mime_message['subject'] = subject
    mime_message.attach(MIMEText(emailMsg, 'plain'))
    # https://stackoverflow.com/questions/1633109/creating-a-mime-email-template-with-images-to-send-with-python-django/1633493#1633493


    for attachment in attachments:
        #content_type, encoding = mimetypes.guess_type(attachment)
        #main_type, sub_type = content_type.split('/', 1)
        file_name = os.path.basename(attachment)
    
        with open(attachment, 'rb') as f:
            file_attachment = MIMEBase('image','png',filename=file_name)
            file_attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
            file_attachment.add_header('X-Attachment-Id', '0')
            file_attachment.add_header('Content-ID', '<0>')
            # read attachment file content into the MIMEBase object
            file_attachment.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(file_attachment)
            # add MIMEBase object to MIMEMultipart object
            mime_message.attach(file_attachment)
    

    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

#phone_number = ''
#subject = 'Hi'
#text_message = ""
#send_message(phone_number, subject, text_message)