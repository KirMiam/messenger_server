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
        token = "8362a91bbf6a5e1bc14ba4df356529eaa0b5dfab"
    else:
        print("valya")
        token = 'f7d2fc0402bb871d628c54d3832fb1a07b9e3398'
    async with websockets.connect("ws://localhost:8000/ws/chat/13/",
                                  extra_headers={"Authorization": ("Token " + token)}) as websocket:
        #async with websockets.connect("ws://localhost:8000/ws/chat/chat1/",
        #                              extra_headers={"Authorization": ("Token " + token)}) as websocket:

        f = True
        #await receive(websocket)
        while f:
            try:
                if a == "1":
                    await send(websocket, {"message": input()})
                    await receive(websocket)
                    #await receive(websocket)
                else:
                    await receive(websocket)
                    await send(websocket, {"message": input()})
                    await receive(websocket)
            except websockets.ConnectionClosed:
                websocket.close()


def http_get():
    print("rooms, users")
    token = "a527ef1c2d680b8b7e0828e4fdd11d661506aff3"
    where = input()
    req = requests.get(("http://localhost:8000/get_" + where), headers={"Authorization": ("Token " + token)})
    try:
        print(req.json())
    except:
        print(req)


def http_post():
    #req = requests.post("http://localhost:8000/login", json={'username': 'newUser', 'password': 'dfjsdfsdf'})
    where = input("login, registration, create_room, delete_room\n")

    #kirill 1234567890 '8362a91bbf6a5e1bc14ba4df356529eaa0b5dfab'
    #valya 0987654321qqq 'f7d2fc0402bb871d628c54d3832fb1a07b9e3398'

    if where == "login":
        json = {"username": "valya", 'password': "0987654321qqq"}
        req = requests.post(("http://localhost:8000/" + where), json=json)
    elif where == "registration":
        json = {"username": "valya", 'password': "0987654321qqq"}
        req = requests.post(("http://localhost:8000/" + where), json=json)
    elif where == "delete_room":
        token = "8362a91bbf6a5e1bc14ba4df356529eaa0b5dfab"
        json = {"name": "testroom1"}
        headers = {"Authorization": ("Token " + token)}
        # req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
        req = requests.post(("http://localhost:8000/" + where), json=json, headers=headers)
    else:
        token = "8362a91bbf6a5e1bc14ba4df356529eaa0b5dfab"
        json = {"name": ""}
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
