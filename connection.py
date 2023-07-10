import telnetlib3
import asyncio
from getpass import getpass
import logging

logging.basicConfig(filename="connection.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)


async def main():
    # Telnet host and port
    host, port = '', 0

    with open("config.ini", "r") as config:
        configuration = config.readlines()
        host, port = configuration[8].split("=")[1].replace(
            "\n", ""), int(configuration[9].split("=")[1])
        print(host, port)

    # Connect to the Telnet host
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
    except ConnectionRefusedError as CRE:
        logger.error(CRE)

    # Read the password prompt
    print(await reader.readuntil(b"Password: "))

    # Send the password
    password = '1234'
    writer.write(password+"\n")

    # Send a command
    command = 'pause'
    writer.write(command+"\n")

    # Read the command output
    output = await reader.readuntil()
    print(output.decode('ascii'))

    # Close the connection
    writer.close()

# Run the main function
asyncio.run(main())
