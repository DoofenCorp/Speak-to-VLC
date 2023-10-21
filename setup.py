import json
from os import getcwd
from helpers import get_password

configuration = {}

host = input("Provide the hostname (default localhost): ")
if host == "":
    host = "localhost"
try:
    port = int(input("Provide the port (default 4212): "))
except ValueError:
    port = 4212
noise = input("Adjust microphone input for noise (set to no by default) (y/n): ")

noise  = True if "y" in noise else False


key, token = get_password()
configuration['host'] = host
configuration['port'] = port
configuration['noise'] = noise
configuration['key'] = str(key.decode('utf-8'))
configuration['token'] = str(token.decode('utf-8'))

with open("config.json", "w") as config:
    print("\nSetting host: {0}".format(host))
    print("Setting port: {0}".format(port))
    print("Adjust for noise: {0}".format(noise))
    json.dump(configuration, config)
    print("Written config.json to", getcwd())
