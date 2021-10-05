import smtplib
from email.message import EmailMessage

email = EmailMessage() # object of email
email['from'] = "Ankit Gupta" 
email['to'] = "ankitkg006@gmail.com" # Sending to
email['subject'] = "Testing SMTPLIB"
email.set_content("Hi, world!")
send_email = smtplib.SMTP(host='smtp.gmail.com', port=587)
send_email.starttls()
send_email.login("ankitkumargupta008@gmail.com", "Seven@123")  # login id and password of gmail


s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)



