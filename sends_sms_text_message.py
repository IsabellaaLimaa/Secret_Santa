#sends_sms_text_message

#athentification = mrnn tdgp kiqt uyts
import email, smtplib, ssl
from providers import PROVIDERS

def send_sms_via_email(
    number: str, 
    message: str, 
    provider: str, 
    sender_credentials: tuple, 
    #subject: str = "sent using Python", 
    smtp_server: str = "smtp.gmail.com", 
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    #email_message = f'Subject: {subject}\nTo: {receiver_email}\n{message}'
    email_message = f'To: {receiver_email}\n{message}'

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():
    number = '5165211870'
    message = "Mom"
    provider = "Verizon"

    sender_credentials = ('isabellaalimaxp@gmail.com', 'mrnn tdgp kiqt uyts')

    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == "__main__":
    main()
    print('sending...')
