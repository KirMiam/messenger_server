import json
import requests
import asyncio
import websockets


async def send(websocket, data):
    if websocket:
        await websocket.send(json.dumps(data))


async def receive(websocket):
    if websocket:
        recv = await websocket.recv()
        print(recv)


async def connect_to_server():
    print("1 or 2")
    a = input()
    if a == "1":
        print("kirill")
        token = "1889e406e6db506b4259a0329655e7de336ab2a0"
    else:
        print("valya")
        token = 'afdfbe8e066b594f8a74debfee299e5dee01f334'
    async with websockets.connect("ws://localhost:8000/ws/chat/6/",
                                  extra_headers={"Authorization": ("Token " + token)}) as websocket:
        #async with websockets.connect("ws://localhost:8000/ws/chat/chat1/",
        #                              extra_headers={"Authorization": ("Token " + token)}) as websocket:

        f = True
        while f:
            try:
                if a == "1":
                    await send(websocket, {"message": input()})
                    await receive(websocket)
                    await receive(websocket)
                else:
                    await receive(websocket)
                    await send(websocket, {"message": input()})
                    await receive(websocket)
            except websockets.ConnectionClosed:
                websocket.close()


def http_get():
    token = "3025c21685462614d97d8ea01d4f20447ffad083"
    req = requests.get("http://localhost:8000/get_rooms", headers={"Authorization": ("Token " + token)})
    #req = requests.get("http://localhost:8000/get_rooms", headers={"Authorization": ("Token " + token)})
    try:
        print(req.json())
    except:
        print(req)


def http_post():
    #req = requests.post("http://localhost:8000/login", json={'username': 'newUser', 'password': 'dfjsdfsdf'})
    where = input("login, registration, create_room\n")

    #kirill 1234567890 '1889e406e6db506b4259a0329655e7de336ab2a0'
    #valya 0987654321qqq 'afdfbe8e066b594f8a74debfee299e5dee01f334'

    if where == "login":
        json = {"username": "valya", 'password': "0987654321qqq"}
        req = requests.post(("http://localhost:8000/" + where), json=json)
    elif where == "registration":
        json = {"username": "valya", 'password': "0987654321qqq"}
        req = requests.post(("http://localhost:8000/" + where), json=json)
    else:
        token = "3025c21685462614d97d8ea01d4f20447ffad083"
        json = {"name": "chat3"}
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
