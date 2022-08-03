# import imapclient, pyzmail
# #IMAP cheat sheet
# #SSL is an encryption algorithm
# conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)
# conn.login('omarsalloum08@gmail.com', 'password')

# conn.select_folder('INBOX', readonly = True)
# UIDs = conn.search(['SINCE 20-Aug-2015'])

# rawMessage = conn.fetch(['UIDS number'], ['BODY[]', 'FLAGS'])

# pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

# message.get_subject()
# message.get_adresses('from')
# message.text_part.get_payload().decode('UTF-8')