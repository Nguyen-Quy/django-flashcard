import os
import sys
from threading import Thread
import webview


def start_webview():
    window = webview.create_window(
        "Test", "http://localhost:8000/", confirm_close=True, width=900, height=600
    )
    webview.start()
    window.confirm_close = os._exit(0)


def start_django():
    if sys.platform in ["win32", "win64"]:
        os.system("python -m venv venv")
        os.system("venv\Scripts\activate")
        os.system("pip install -r requirements.txt")
        os.system("python manage.py runserver 127.0.0.1:8000")
    else:
        os.system("python -m venv venv")
        os.system("source venv/bin/activate")
        os.system("pip install -r requirements.txt")
        os.system("python3 manage.py runserver 127.0.0.1:8000")


if __name__ == "__main__":
    Thread(target=start_django).start()
    start_webview()
