import telnetlib3
import asyncio
import logging
import json
from helpers import LoopBreakException
from helpers import send_password

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
    #Login to interface

    print(await reader.readuntil(b"Password:"))
    writer.write(send_password(key, token)+"\n")
    del key
    del token
    await reader.readuntil(b">")

    async def send_command():
        command = input("VLC> ")
        if command in ("quit", "shutdown"):
            writer.write(command + "\n")  
            print(await (reader.readuntil()))
            raise LoopBreakException("Exit command sent to VLC. Closing connection.")
        writer.write(command + "\n")
        buffer = await reader.readuntil(b">")
        buffer = buffer.decode("ascii")
        print(buffer)
        if buffer == "Connection to host lost.":
            # Close the connection
            writer.close()
            raise LoopBreakException("Unexpected termination of VLC. Connection lost. Exiting...")

    while True:
        try:
            await send_command()
        except LoopBreakException:
            break


# Run the main function
if __name__=="__main__":
    try:
        asyncio.run(main())
    except RuntimeError as RE:
        if "Event loop is closed" not in str(RE):
            print("Raising exception from except statement")
            raise RE
