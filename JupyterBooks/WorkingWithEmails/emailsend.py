import smtplib, ssl
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "ananya2531997@gmail.com"
password = "Andy@2531997"

# Create a secure SSL context
context = ssl.create_default_context()
email =  EmailMessage()
email['from'] = 'ananya2531997@gmail.com'
email['to'] = 'ananya.s.library@gmail.com'
email['subject'] = 'YOU JUST WON A MILLION DOLLARS'

email.set_content('I am a Lottery Agent.')

# Try to log in to server and send email
try:
    server = smtplib.SMTP('smtp.gmail.com', '587')
    
    server.starttls() # Secure the connection
    server.ehlo() # Can be omitted
    server.connect()# Can be omitted
    server.login(sender_email, password)
    smtp.sendmail(sender_email,'ananya.s.library@gmail.com','I am a Lottery Agent.')
    print('Message Sent')
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
