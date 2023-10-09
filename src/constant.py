USERNAME = "emailcontrolmmt@gmail.com"
PASSWORD = "mmt10diem"
APP_PASS = "yntx ansy zonv gwcj"

import imaplib, smtplib, email
import os, pyautogui

from time import sleep
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

from pynput.keyboard import Listener
import logging
