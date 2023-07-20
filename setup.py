import json
from getpass import getpass
from cryptography.fernet import Fernet
import base64

def get_password():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    token = cipher.encrypt(getpass("Enter your password: ").encode("utf-8"))
    return key, token

configuration = {}
host = input("Provide the hostname: ")
try:
    port = int(input("Provide the port (default 4212): "))
except ValueError:
    port = 4212
key, token = get_password()
configuration['host'] = host
configuration['port'] = port
configuration['key'] = str(key)
configuration['token'] = str(token)

with open("config.json", "w") as config:
    print("Setting host: {0}".format(host))
    print("Setting port: {0}".format(port))
    json.dump(configuration, config)
