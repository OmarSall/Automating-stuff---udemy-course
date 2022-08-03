import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)   #587 is a port

#calling a function ehlo to start the connection

conn.ehlo()

#starting the tls encryption
# print(conn.starttls())
conn.starttls()
conn.login('omarsalloum08@gmail.com', '608.798.218.sS')
# print(conn.login('omarsalloum08@gmail.com', 'password'))c

conn.sendmail('omarsalloum08@gmail.com', 'omarsalloum08@gmail.com','Subject: So long...\n\nDear Omar, \n this is the \
                                            body paragraph that you created\n\n Best Regards\n Omar S')

#the output is a dictionary - if it s empty it means that every mail was sent correctly

conn.quit()