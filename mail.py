import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "xyz@gmail.com"
passowrd = "abc123"
receiver_email = "abc@gmail.com"
message = "Best accuracy achieved"

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
    #print "Sent"
except Exception as e:
    print(e)
finally:
    server.quit()