from cryptography.fernet import Fernet
from getpass import getpass

class LoopBreakException(Exception):
    def __init__(self, message = "Exit trigger received. Closing main loop."):
        self.message = message
        super().__init__(self.message)


def get_password():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    token = cipher.encrypt(getpass("Enter your password: ").encode("utf-8"))
    return key, token

def send_password(key, token):
    cipher = Fernet(key)
    return cipher.decrypt(token).decode('utf-8')

def speak():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("VLC>", end = " ")
        spoken = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(spoken)
        print(command)
    except:
        return "Didn't quite get what you just said."
    return command