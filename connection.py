import sys
import telnetlib3
import asyncio
import logging
import json
from cryptography.fernet import Fernet


def send_password(key, token):
    cipher = Fernet(key)
    return cipher.decrypt(token).decode('utf-8')


logging.basicConfig(filename="connection.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)


async def main():

    try:
        with open("config.json") as config:
            try:
                configuration = json.loads(config.read())
                # Telnet host, port and password
                host, port, key, token = configuration["host"], configuration[
                    "port"], configuration['key'].encode("utf-8"), configuration['token'].encode("utf-8")
            except json.JSONDecodeError as JDE:
                logger.error(JDE)
                return 0
    except FileNotFoundError as FNFE:
        logger.error(FNFE)
        return 0

    # Connect to the Telnet host
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
    except ConnectionRefusedError as CRE:
        logger.error(CRE)
        return 0

    async def send_command():
        command = input("Telnet> ")
        if command == "exit":
            sys.exit(0)
        buffer = await reader.readuntil()
        buffer = buffer.decode("ascii")
        print(buffer)
        if buffer == "Password: ":
            writer.write(send_password(key, token)+"\n")
            return
        elif buffer == "Connection to host lost.":
            # Close the connection
            writer.close()
            sys.exit(0)
        writer.write(command + "\n")

    while True:
        await send_command()


# Run the main function
asyncio.run(main())
