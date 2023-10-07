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
    print()
    # print(cmd_list)
    return sender, cmd_list


def current_time() -> str:
    return datetime.now().strftime("%H:%M:%S %d-%m-%Y")


def capture_SS(file_name: str = "Picture.png", overwrite: bool = True) -> str:
    name, ext = file_name.split(".")
    ext = "." + ext
    path = "src\\Screenshots\\"
    index = 1

    namae = name + ext
    while os.path.isfile(path + namae) and not overwrite:
        namae = name + str(index) + ext
        index += 1

    # print(path + namae)
    pyautogui.screenshot(path + namae)
    return path + namae
