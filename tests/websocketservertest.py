import asyncio
import websockets
import ssl
import pathlib
import json
import datetime

import storinghashes as sh


def ws_message_enum(type: str):
    types = {"connect", "authorization", "login_success", "login_fail", "ready_to_work", "hash_to_sign", "signed_hash",
             "no_hash_to_sign"}

    if type in types:
        return type
    else:
        raise TypeError("Name of type is incorrect")


wsMessageDefault = {"type": ws_message_enum("connect"), \
                    "contents": str(), \
                    "date": str(datetime.datetime.now())}


async def send_to_client(server_message, websocket):
    server_message = json.dumps(server_message)
    await websocket.send(server_message)
    print(f'Server Sent: {server_message}')


async def greet_client(client_message, websocket):
    server_message = wsMessageDefault.copy()
    server_message["type"] = ws_message_enum("authorization")
    server_message["contents"] = f'Hello {client_message["contents"]}!'
    server_message["date"] = str(datetime.datetime.now())

    await send_to_client(server_message, websocket)


async def authorize_client(client_message, websocket):
    recvUsername = client_message["contents"]["username"]
    recvPassword = client_message["contents"]["password"]

    with open("tests/user_data.json", "r") as read_file:
        savedData = json.load(read_file)

    server_message = wsMessageDefault.copy()
    server_message["date"] = str(datetime.datetime.now())

    if savedData["username"] == recvUsername and savedData["password"] == recvPassword:
        server_message["type"] = ws_message_enum("login_success")
        server_message["contents"] = f'This is correct! You are authorized!'
    else:
        server_message["type"] = ws_message_enum("login_fail")
        server_message["contents"] = f'Sorry, this is not correct. Try again.'

    await send_to_client(server_message, websocket)


async def send_hash_to_sign(websocket):
    server_message = wsMessageDefault.copy()
    server_message["type"] = ws_message_enum("hash_to_sign")
    hash_to_sign = sh.read_first_line("to sign")

    if hash_to_sign != "file is empty":
        server_message["contents"] = {"hash_to_sign": sh.read_first_line("to sign")}
        sh.remove_hash_from_file("to sign")
    else:
        server_message["type"] = ws_message_enum("no_hash_to_sign")
        server_message["contents"] = {"message": "That's all per now. Now wait for new ones."}

    server_message["date"] = str(datetime.datetime.now())

    await send_to_client(server_message, websocket)


async def handle_messages(websocket):
    async for clientMessage in websocket:
        clientMessage = json.loads(clientMessage)
        print(f'Server Received: {clientMessage}')

        if clientMessage["type"] == ws_message_enum("connect"):
            await greet_client(clientMessage, websocket)
        if clientMessage["type"] == ws_message_enum("authorization"):
            await authorize_client(clientMessage, websocket)

        if clientMessage["type"] == ws_message_enum("ready_to_work"):
            await send_hash_to_sign(websocket)

        if clientMessage["type"] == ws_message_enum("signed_hash"):
            sh.save_hash_to_file(clientMessage["contents"]["signed_hash"], "signed")
            await send_hash_to_sign(websocket)


async def start_server():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
    ssl_context.load_cert_chain(localhost_pem)

    async with websockets.serve(handle_messages, "localhost", 8765, ssl=ssl_context):
        await asyncio.Future()


asyncio.run(start_server())
