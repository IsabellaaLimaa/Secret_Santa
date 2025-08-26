#mysecrete santa
from sends_sms_text_message import send_sms_via_email
import random
import smtplib
from email.message import EmailMessage

def secret_santa(info):
    #while everyone doesnt have a valid match,
        #for each sender
            #while receiver isnt themself or already chosen
                #find receiver by random
                #
    sib = {"Francesca": "Peter", 
           "Peter": "Francesca", 
           "John": {"Sophia", "Jake"}, 
           "Sophia": {"John", "Jake"}, 
           "Jake": {"Sophia", "John"}, 
           "Arianna": "Isabella", 
           "Isabella": "Arianna", 
           "Sabrina": None
    }
    options = list(info.keys())
    redo = True
    while redo == True:
        for sender in info:
            s_op = options[:]
            if sender in s_op:
               s_op.remove(sender)
            sibling = sib[sender]

            # Normalize sibling to a set
            if sibling is not None:
                if isinstance(sibling, str):
                    sibling = {sibling}
                for s in sibling:
                    if s in s_op:
                        s_op.remove(s)

            if len(s_op) != 0:
                receiver = random.choice(s_op)
                options.remove(receiver)
                #print(f'sender: {sender}\nsibling: {sibling}\nreceiver: {receiver}\ns_op: {s_op}\noptions:{options}\n\n')
                main(sender, receiver, info)
                redo = False

def send_email(send_from_email, send_from_password, send_to_email, subject, body):
    msg = EmailMessage()
    msg["From"] = send_from_email
    msg["To"] = send_to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(send_from_email, send_from_password)
        smtp.send_message(msg)

def main(sender, receiver, info):
    number = info[sender]["phone"]
    send_to_email = info[sender]["email"]
    budget = 60
    link = info[receiver]['wishlist']
    provider = "Verizon"

    subject = "Your Secret Santa Assignment"
    message = (
        f'Hello {sender}!\n'
        f'Your secret santa is {receiver}!\n'
        f'Your budget is ${budget}.\n'
        f'Here is the link to their wishlist: \n{link}'
    )
    
    sender_credentials = ('isabellaalimaxp@gmail.com', 'mrnn tdgp kiqt uyts')

    send_sms_via_email(number, message, provider, sender_credentials)
    send_email(sender_credentials[0], sender_credentials[1], send_to_email, subject, message)



if __name__ == '__main__':
    info = {
        'Francesca': {'phone': '5165211870', 'email': None, 'wishlist': None},
        'Peter': {'phone': '5165211870', 'email': None, 'wishlist': None},
        'John': {'phone': '5165211870', 'email': None, 'wishlist': None},
        'Sophia': {'phone': '5165211870', 'email': None, 'wishlist': None},
        'Jake': {'phone': '5165211870', 'email': None, 'wishlist': None},
        'Arianna': {'phone': '5165211870', 'email': None, 'wishlist': 'https://giftful.com/ariannalima'},
        'Isabella': {'phone': '5165211870', 'email': 'isabellaalimaxp@gmail.com' , 'wishlist': 'https://giftful.com/isabella1'},
        'Sabrina': {'phone': '5165211870', 'email': None, 'wishlist': None}
    }
    secret_santa(info)