from classMail import *
from loading import *
import GUI


def main():
    mail = Mail()
    app = App()
    app.after(0, lambda: mail.run(app))
    app.mainloop()


def test_main():
    mail = Mail()
    mail.cmd_list = ["screenshot a"]
    mail.process_command()
    mail.sender = "17mels22@gmail.com"
    mail.write_log()
    # mail.send_mail()


def testmain2():
    mail = Mail()
    GUI.Splash_Screen()
    app = GUI.App()
    app.after(0, lambda: mail.run(app))
    app.mainloop()

if __name__ == "__main__":
    picture = "Files\\Pictures"  # Guarantee the Files folder
    if not os.path.exists(picture):
        os.makedirs(picture)

    try:
        # test_main()
        # main()
        testmain2()
    except KeyboardInterrupt:
        print("\rQuit                             ")
