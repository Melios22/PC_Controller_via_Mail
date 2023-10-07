from fetchMail import *

import smtplib

def send_mail(sender: str, cmd_list: list):

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(USERNAME, APP_PASS)

    message:str = "Hello, I'm Mail Control. I'm here to help you control your PC via Mail.\n\n"

    smtp.sendmail(USERNAME, [sender], f"Subject: Mail Control\nRe:{message}")

    smtp.quit()



while True:
    sender, cmd_list = fetch_mail()
    if len(cmd_list) == 0:
        continue

    send_mail(sender, cmd_list)
    if ("quit" in cmd_list):
        print("Quit")
        break
    time.sleep(5)

