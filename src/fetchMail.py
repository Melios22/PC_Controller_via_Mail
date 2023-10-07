from constant import *
import imaplib, email, time

#! import: constant, lib

def decode_mail(msg: str):
    cmd_list = ""
    
    print('-----------------------------')
    sender = email.utils.parseaddr(msg.get("From"))[1]
    print('From:', sender)
    print('Content:', end = " ")
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            content = part.get_payload(decode=True).decode('utf-8')
            print(content, end = "\t")
            cmd_list += content
    
    cmd_list = cmd_list.replace('\n', ' ').replace('\r', ' ').split()
    print()
    # print(cmd_list)
    return sender, cmd_list


def fetch_mail():
    cmd_list:list = []
    sender:str = ""

    #? Login to the mail server and select the inbox
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(USERNAME, APP_PASS)
    mail.select("inbox")

    #! Get all the mail with subject "Mail Control"
    *_, message = mail.search(None, '(UNSEEN SUBJECT "Mail Control")')
    ids = message[0].split()

    #? Get the body of the mail
    for id in ids:
        *_, msg_data =  mail.fetch(id, "(RFC822)")
        email_body = email.message_from_bytes(msg_data[0][1])
        sender, cmd_list = decode_mail(email_body)
    
    mail.logout()
    return sender, cmd_list

# while True:
#     sender, cmd_list = fetch_mail()
#     if len(cmd_list) != 0:
#         if ("quit" in cmd_list):
#             print("Quit")
#             break
#         time.sleep(5)