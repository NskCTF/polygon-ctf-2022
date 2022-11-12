import asyncio
import os

MACHINE_ID = os.getenv('MACHINE_ID')


async def shell_run(cmd, wr):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    wr.write(f'[{cmd!r} exited with {proc.returncode}]'.encode())
    if stdout:
        wr.write(b'[stdout]\n' + stdout)
    if stderr:
        wr.write(b'[stderr]\n' + stderr)


async def handle_client(reader, writer):
    writer.write(b'Machine [' + MACHINE_ID.encode() + b'/3] - flag.txt is on third machine. ')
    writer.write(b'Enter command to execute (for example, ls): ')
    await writer.drain()
    request = (await reader.read(255)).decode('utf8')
    await shell_run(request, writer)
    await writer.drain()
    writer.close()


async def run_server():
    server = await asyncio.start_server(handle_client, '0.0.0.0', int(os.getenv('LPORT')))
    async with server:
        await server.serve_forever()


asyncio.run(run_server())
