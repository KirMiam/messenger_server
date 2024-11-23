import json

from websocket import create_connection
import requests
import asyncio
import websockets
import sys


# def ws():
#     token = "3025c21685462614d97d8ea01d4f20447ffad083"
#     ws = create_connection("ws://localhost:8000/ws/23",  header={"Authorization": ("Token " + token)})
#     #ws = create_connection("ws://localhost:8000/ws/23")
#     #ws = create_connection("ws://localhost:8000/ws/1")
#     while True:
#         msg = input('Enter a message: ')
#         if msg == 'quit':
#             ws.close()
#             break
#         ws.send(msg)
#         result =  ws.recv()
#         print ('> ', result)
async def send(websocket, data):
    if websocket:
        await websocket.send(json.dumps(data))


async def receive(websocket):
    if websocket:
        await websocket.recv()


async def connect_to_server():
    print("1 or 2")
    if input() == "1":
        token = "3025c21685462614d97d8ea01d4f20447ffad083"
    else:
        token = '739ab8196b5b6cf4b2012f3f75f7d98d42ca9bc5'
    async with websockets.connect("ws://176.124.204.174:8000/ws/chat/chat1/",
                                  extra_headers={"Authorization": ("Token " + token)}) as websocket:
        #async with websockets.connect("ws://localhost:8000/ws/chat/chat1/",
        #                              extra_headers={"Authorization": ("Token " + token)}) as websocket:

        f = True
        while f:
            message = input()
            if message == "exit":
                await websocket.close()
                f = False
            word = {"message": message}
            try:
                await send(websocket, word)
                await receive(websocket)
            except websockets.ConnectionClosed:
                print("i try")


def http_get():
    token = "3025c21685462614d97d8ea01d4f20447ffad083"
    req = requests.get("http://176.124.204.174:8000/get_rooms", headers={"Authorization": ("Token " + token)})
    #req = requests.get("http://localhost:8000/get_rooms", headers={"Authorization": ("Token " + token)})
    try:
        print(req.json())
    except:
        print(req)


def http_post():
    #req = requests.post("http://localhost:8000/login", json={'username': 'newUser', 'password': 'dfjsdfsdf'})
    where = input("login, registration, create_room\n")

    if where == "login":
        json = {"username": "privet", 'password': "dfgdfgfffdfgdfg"}
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json)
    elif where == "registration":
        json = {"username": "privet11", 'password': "dfgdfgfffdfgdfg"}
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json)
    else:
        token = "3025c21685462614d97d8ea01d4f20447ffad083"
        json = {"name": "chat2"}
        headers = {"Authorization": ("Token " + token)}
        #req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
        req = requests.post(("http://localhost:8000/" + where), json=json, headers=headers)
    try:
        print(req.json())
    except:
        print(req)


if input("ws, http\n") == 'ws':
    asyncio.get_event_loop().run_until_complete(connect_to_server())
elif input('get\n') == 'get':
    http_get()
elif input('post\n') == 'post':
    http_post()
else:
    req = requests.get('http://localhost:8000/test')
    try:
        print(req.json())
    except:
        print(req)
