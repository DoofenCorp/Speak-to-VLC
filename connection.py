import telnetlib3
import asyncio
from getpass import getpass

async def main():
    # Telnet host and port
    host = 'localhost'
    port = 4212

    # Connect to the Telnet host
    reader, writer = await telnetlib3.open_connection(host, port)

    # Read the password prompt
    print(await reader.readuntil(b"Password: "))

    # Send the password
    password = '1234'
    writer.write(password+"\n")

    # Send a command
    command = 'play'
    writer.write(command+"\n")

    # Read the command output
    output = await reader.readuntil()
    print(output.decode('ascii'))

    # Close the connection
    writer.close()

# Run the main function
asyncio.run(main())
