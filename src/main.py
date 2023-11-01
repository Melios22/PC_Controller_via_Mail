from classMail import *
from loading import *


def main():
    mail = Mail()
    mail.loop()


def test_main():
    mail = Mail()
    mail.cmd_list = ["screenshot a"]
    mail.process_command()
    mail.sender = "17mels22@gmail.com"
    mail.write_log()
    # mail.send_mail()


if __name__ == "__main__":
    picture = "Files\\Pictures" # Guarantee the Files folder
    if not os.path.exists(picture):
        os.makedirs(picture)
    
    try:
        test_main()
        # main()
    except KeyboardInterrupt:
        print("\rQuit                             ")
