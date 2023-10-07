from fetchMail import *

#! import: fetchMail, other command
import os, pyautogui, smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def current_time():
    return datetime.now().strftime("%H:%M:%S %d-%m-%Y")

def capture_SS(file_name: str = "Picture.png", overwrite:bool = False):
    name, ext = file_name.split('.')
    ext = '.' + ext
    path = 'src\\Screenshots\\'
    index = 1
    
    namae = name + ext
    while os.path.isfile(path + namae) and not overwrite:
        namae = name + str(index) + ext
        index += 1

    pyautogui.screenshot(path + namae)
    return path + namae


def take_screenshot(sender:str, file_name = "Picture.png", overwrite:bool = False):
    file_path = capture_SS(file_name, overwrite)  

    subject = "Re: Mail Control: Screenshot" # Add 'Re:' to the original subject
    body = "Please find the attached screenshot taken at " + current_time() + ".\n\n"

    email_message = MIMEMultipart()
    email_message.attach(MIMEText(body, "plain"))
    email_message['From'] = USERNAME
    email_message['To'] = sender
    email_message['Subject'] = subject

    
    with open(file_path, "rb") as picture_file:
        picture_attachment = MIMEImage(picture_file.read(), name=os.path.basename(file_path))
        email_message.attach(picture_attachment)

    send_mail(sender, email_message)


def send_mail(sender: str, email_message):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, APP_PASS)

        smtp.sendmail(USERNAME, sender, email_message.as_string())
        print("Mail sent to", sender)
 

def process_command(sender:str, cmd_list: list):
    if (cmd_list[0] == 'screenshot'):
        try:
            take_screenshot(sender, cmd_list[1])
        except IndexError:
            take_screenshot(sender)

def main():
    while True:
        sender, cmd_list = fetch_mail()
        if len(cmd_list) != 0:
            process_command(sender, cmd_list)
        
        time.sleep(5)


if __name__ == "__main__":
    main()