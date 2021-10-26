import webbrowser
import threading
import time

def youtube():
    while True:
        webbrowser.open("youtube.com")
        time.sleep(0.1)

def instagram():
    while True:
        webbrowser.open("wikipedia.com")
        time.sleep(0.1)
def twitch():
    while True:
        webbrowser.open("twitch.tv")
        time.sleep(0.1)

t1 = threading.Thread(target=youtube)
t2 = threading.Thread(target=instagram)
t3 = threading.Thread(target=twitch)

t1.start()
t2.start()
t3.start()