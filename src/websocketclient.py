import asyncio
import websockets
import ssl
import pathlib
import json
import PyQt6.QtCore as qtcore
#import QThread, pyqtSignal
import time

import storingfiles as sf
import hashes.storinghashes as sth
import hashes.signinghashes as signh
import codelogging as log
from loginstorage import *
from websocketmessage import ws_message_enum, wsMessageDefault


class WebsocketClient():
    def __init__(self) -> None:
        super().__init__()

        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
        self.ssl_context.load_verify_locations(localhost_pem)

        self.file_with_url = "data/url_service.json"
        url_dict = sf.load_json_file(self.file_with_url)
        url_service = url_dict["URL service"]
        self.url_service = f"wss://{url_service}"
        self.websocket = None
    
    async def send_to_server(self, clientMessage):
        clientMessage = json.dumps(clientMessage)
        await self.websocket.send(clientMessage)
        print(f'Client send: {clientMessage}')

    async def greet_server(self):
        clientMessage = wsMessageDefault.copy()
        clientMessage["contents"] = "AutoESignature"

        await self.send_to_server(clientMessage)

    async def authorize_to_server(self):
        clientMessage = wsMessageDefault.copy()
        clientMessage["type"] = ws_message_enum("authorization")

        service_url = sf.load_json_file("data/url_service.json")["URL service"]
        clientMessage["contents"] = {"username": "AutoESignature", \
                                        "password": keyring.get_password(FOLDER_FOR_LOGINS, service_url)}
        
        await self.send_to_server(clientMessage)

    async def ask_for_hash(self):
        clientMessage = wsMessageDefault.copy()
        clientMessage["type"] = ws_message_enum("ready_to_work")
        clientMessage["contents"] = f'Horray! Give me hash to sign.'

        await self.send_to_server(clientMessage)

    async def sign_hash(self, serverMessage):
        clientMessage = wsMessageDefault.copy()
        original_hash = serverMessage["contents"]["hash_to_sign"]
        signed_hash = signh.sign_hash(original_hash)

        clientMessage["type"] = ws_message_enum("signed_hash")
        clientMessage["contents"] = {"original_hash": original_hash, "signed_hash": signed_hash}
        
        await self.send_to_server(clientMessage)
    
    async def connect_to_server(self, stop_event) -> None:
            async with websockets.connect(self.url_service, ssl=self.ssl_context) as self.websocket:
                print('Websocket received!')
                await self.greet_server()

                timeout = 0.5
                while not stop_event.is_set():
                    try:
                        serverMessage = await asyncio.wait_for(self.websocket.recv(), timeout)
                    except asyncio.TimeoutError:
                        # If timeout was over, then continue cycle for checking
                        continue    
                    except websockets.exceptions.ConnectionClosedError as e:
                        log.logging.error("Connection closed: %e")

                    serverMessage = json.loads(serverMessage)
                    print(f'Client received: {serverMessage}')

                    if (serverMessage["type"] == ws_message_enum("authorization")):
                        await self.authorize_to_server()

                    if (serverMessage["type"] == ws_message_enum("login_fail")):
                        await self.authorize_to_server()

                    if (serverMessage["type"] == ws_message_enum("login_success")):
                        self.isConnected = True
                        await self.ask_for_hash()

                    if (serverMessage["type"] == ws_message_enum("hash_to_sign")):
                        await self.sign_hash(serverMessage)

    def start_client(self, stop_event):
        logger = log.logging.getLogger(__name__)

        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.connect_to_server(stop_event))
        loop.stop()
