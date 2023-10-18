from classMail import *
from loading import *

def main():
    mail = Mail()
    mail.loop()


def test_main():
    mail = Mail()
    mail.cmd_list = ['listApp']
    mail.process_command()
    mail.sender = "17mels22@gmail.com"
    mail.send_mail()
    mail.log()


if __name__ == "__main__":
    try:
        # test_main()
        main()
    except KeyboardInterrupt:
        print("\rQuit                             ")
        
