from fetchMail import *

#! import: fetchMail, other command


def send_mail(sender: str, cmd_list: list):

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, APP_PASS)

        subject = "Re: Mail Control"  # Add 'Re:' to the original subject
        body = "Hello, I'm Mail Control.\nI'm here to help you control your PC via Mail.\n\nYour command(s):"
        email_content = f"Subject: {subject}\n\n{body}"

        for cmd in cmd_list:
            email_content += "\n" + cmd

        smtp.sendmail(USERNAME, sender, email_content)

#? Turn on when runnign the program
# while True:
#     sender, cmd_list = fetch_mail()
#     if len(cmd_list) != 0:
#         # Command()
#
#         send_mail(sender, cmd_list)
#         if ("quit" in cmd_list):
#             print("Quit")
#             break
#         time.sleep(5)


