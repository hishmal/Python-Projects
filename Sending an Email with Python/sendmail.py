import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('zahid.tnear@gmail.com', 'pythonPractice')

server.sendmail('zahid.tnear@gmail.com','hishymalik@gmail.com','Hey,\nThis is a test.')
print('Mail Sent')

# Gmail is more secure. Need to use 2FA code to login.