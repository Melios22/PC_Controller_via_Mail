from constant import *
from utilities import *


class Mail:
    def __init__(self):
        self.sender: str = ""
        self.cmd_list: list = []

        self.subject: str = "Re: Mail Control: "
        self.body: str = ""
        self.email_message: MIMEMultipart

    def fetch_mail(self):
        # ? Login to the mail server and select the inbox
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(USERNAME, APP_PASS)
        mail.select("inbox")

        #! Get all the mail with subject "Mail Control"
        *_, message = mail.search(None, '(UNSEEN SUBJECT "Mail Control")')
        ids = message[0].split()

        # ? Get the body of the mail
        for id in ids:
            *_, msg_data = mail.fetch(id, "(RFC822)")
            email_body = email.message_from_bytes(msg_data[0][1])
            self.sender, self.cmd_list = decode_mail(email_body)

        mail.logout()

    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(USERNAME, APP_PASS)

            smtp.sendmail(USERNAME, self.sender, self.email_message.as_string())
            print("Mail sent to", self.sender)

    def take_screenshot(self):
        file_name: str = "Picture.png"
        overwrite: bool = True

        if len(self.cmd_list) > 1:
            file_name = self.cmd_list[1]
        if len(self.cmd_list) > 2:
            overwrite = not (self.cmd_list[2] == "False")

        file_path = capture_SS(file_name, overwrite)

        self.email_message = MIMEMultipart()

        self.body = "A screenshot of your PC taken at " + current_time() + "."

        self.email_message.attach(MIMEText(self.body, "plain"))
        self.email_message["From"] = USERNAME
        self.email_message["To"] = self.sender
        self.email_message["Subject"] = self.subject + "Screenshot"

        with open(file_path, "rb") as picture_file:
            picture_attachment = MIMEImage(
                picture_file.read(), name=os.path.basename(file_path)
            )
            self.email_message.attach(picture_attachment)

    def shut_down(self):
        time: int = 10
        if len(self.cmd_list) > 1:
            time = int(self.cmd_list[1])

        self.email_message = MIMEMultipart()

        self.body = "Shutting down your PC in " + str(time) + " seconds."

        self.email_message.attach(MIMEText(self.body, "plain"))
        self.email_message["From"] = USERNAME
        self.email_message["To"] = self.sender
        self.email_message["Subject"] = self.subject + "Shutdown"

        self.send_mail()

        while time > 0:
            print(f"{time} seconds left until shutdown")
            time -= 1
            sleep(1)

        os.system("shutdown /s /t 0")

    def process_command(self):
        if self.cmd_list[0] == "screenshot":
            self.take_screenshot()
        elif self.cmd_list[0] == "shutdown":
            self.shut_down()
        else:
            pass

    def refresh(self):
        self.sender = ""
        self.cmd_list = []

        self.body = ""
        self.email_message = None

    def loop(self):
        while True:
            self.fetch_mail()
            if len(self.cmd_list) != 0:
                self.process_command()
                self.send_mail()
                self.refresh()

            sleep(2)
            print("Waiting for new mail...")
