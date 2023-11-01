# PC Controller via Mail

## Set environment

First, you need to clone the repository at: https://github.com/Melios22/PC_Controller_via_Mail.git

Language: Python
Required module: opencv-python, pillow, pynput

Consider installing the modules with pip:
```bash
pip install opencv-python
pip install pillow
pip install pynput
```

## How to use
Redirect to the `src` folder and locate the `main.py` file. Run the file with python:
```bash
python main.py
```

## How it works
The program will wait for new email sent from any user to `emailcontrolmmt@gmail.com` with the subject of *Mail Control*
The included body is the command to be executed. The program will execute the command and reply the user with the result of the command.