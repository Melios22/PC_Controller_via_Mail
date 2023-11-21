from threading import Thread

from constant import *
from GUI import *
from loading import *
from utilities import *

#! cmd_list: 2d list
#! attachmnt: 1d list


class Mail:
    def __init__(self):
        self.sender: str = ""
        self.command: list = []
        self.cmd_list: list = []
        self.attachment: list = []

        self.body: str = ""  # Reply message
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

    def screenshot(self, lst: list = []):
        self.attachment.append(capture_SS(lst))

        # self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment[-1], "rb") as picture_file:
            picture_attachment = MIMEImage(
                picture_file.read(), name=os.path.basename(self.attachment[-1])
            )
            self.email_message.attach(picture_attachment)

    def webcam(self, lst: list = []):
        tmp_path, tmp_mes = capture_webcam(lst)
        self.body += tmp_mes
        self.attachment.append(tmp_path)
        # self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment[-1], "rb") as picture_file:
            picture_attachment = MIMEImage(
                picture_file.read(), name=os.path.basename(self.attachment[-1])
            )
            self.email_message.attach(picture_attachment)

    def keylogger(self, lst: list = []):
        self.attachment.append(key_logger(lst))

        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment[-1], "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= Keylogger.txt"
            )
            self.email_message.attach(text_attachment)

    #! Add log to logout shutdown
    def logout(self, lst: list = []):
        self.body += "Logging out of your PC.\n"
        self.email_message.attach(MIMEText(self.body, "plain"))

        self.send_mail()
        os.system("shutdown -l")

    def shutdown(self, lst: list = []):
        time = lst[1] if len(lst) > 1 else 10

        self.body += "Shutting down your PC in " + str(time) + " seconds.\n"
        self.email_message.attach(MIMEText(self.body, "plain"))

        self.send_mail()  #! only shutdown process has the send_mail inside
        sleep(2)
        os.system("shutdown /s /t now")

    def list_app(self, lst: list = []):
        self.attachment.append(list_running_application())

        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment[-1], "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= RunningApplications.txt"
            )
            self.email_message.attach(text_attachment)

    def list_process(self, lst: list = []):
        self.attachment.append(list_running_process())

        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(self.attachment[-1], "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= RunningProcesses.txt"
            )
            self.email_message.attach(text_attachment)

    def terminate_process(self, lst: list = []):
        try:
            self.body += kill_process(lst[1]) + "\n"
        except IndexError:
            self.body += "ERROR: Terminate process command misses an argument.\n"
        self.email_message.attach(MIMEText(self.body, "plain"))

    def send_log(self, lst=[]):
        file_path = "Files\\mail.log"
        self.attachment.append(file_path)

        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(file_path, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= mail.log"
            )
            self.email_message.attach(text_attachment)

    def help(self, lst: list = []):
        writeHelp(file_path := "Files\\help.txt")

        self.attachment.append(file_path)
        self.email_message.attach(MIMEText(self.body, "plain"))

        with open(file_path, "r") as text_file:
            text_attachment = MIMEText(text_file.read())
            text_attachment.add_header(
                "Content-Disposition", "attachment; filename= mail.log"
            )
            self.email_message.attach(text_attachment)

    def process_command(self):
        self.set_info()

        command = {
            "screenshot": [self.screenshot, "perform capturing screenshot"],
            "webcam": [self.webcam, "perform capturing from webcam"],
            "keylog": [self.keylogger, "perform keylogging"],
            "logout": [self.logout, "logout from your PC"],
            "shutdown": [self.shutdown, "shutdown your PC"],
            "listapp": [self.list_app, "list running applications"],
            "listprocess": [self.list_process, "list running processes"],
            "terminateprocess": [self.terminate_process, "terminate a process"],
            "log": [self.send_log, "get the log file of your PC"],
            "help": [self.help, "get the list of commands"],
        }
        for i in range(len(self.cmd_list)):
            self.cmd_list[i][0] = self.cmd_list[i][0].lower()
        if ["logout"] in self.cmd_list:
            self.cmd_list.remove(["logout"])
            self.cmd_list.append(["logout"])
        elif ["shutdown"] in self.cmd_list:
            self.cmd_list.remove(["shutdown"])
            self.cmd_list.append(["shutdown"])

        check: bool = False
        for comd in self.cmd_list:
            if comd[0] in command:
                try:
                    command[comd[0]][0](comd)
                except Exception:
                    self.body += f"ERROR: Cannot {command[comd[0]][1]}\n"
            else:
                check = True
        
        if check:
            self.body += "ERROR: Invalid command. Review the help.txt file for more information.\n"
            self.help()         

    def write_log(self):
        note2log(self.sender, self.cmd_list, self.attachment, self.body)

    def set_info(self):
        self.email_message = MIMEMultipart()
        self.email_message["From"] = USERNAME
        self.email_message["To"] = self.sender
        self.email_message["Subject"] = "Re: Mail Control"

    def refresh(self):
        self.sender = ""
        self.cmd_list = []
        self.command = []
        self.attachment = []

        self.body = ""
        self.email_message = None

    def run(self, app):
        self.fetch_mail()
        if self.cmd_list:
            self.command = self.cmd_list.copy()
            self.process_command()
            self.write_log()

            print(self.body, self.attachment)
            
            for i in range(len(self.command)):
                self.command[i] = " ".join(self.command[i])
            
            app.add_new_mail(
                self.sender, self.command, current_time(), self.body, self.attachment
            )
            # Thread(target=self.send_mail_async, args=(app, command)).start()

            self.send_mail()
            self.refresh()

        app.after(2000, lambda: self.run(app))
