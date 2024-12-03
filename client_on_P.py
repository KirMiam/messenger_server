import json
from websocket import create_connection
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
        token = "783f985d0d85eeca545dad3d4ec0a3987b8448ce"
    else:
        print("valya")
        token = 'bb96262770aaeab7186f89ad6b22ddce9b3a72c0'
    async with websockets.connect("ws://176.124.204.174:8000/ws/chat/15/",
                                  extra_headers={"Authorization": ("Token " + token)}) as websocket:
        f = True
        await receive(websocket)
        while f:
            try:
                if a == "1":
                    await send(websocket, {"message": input()})
                    await receive(websocket)
                    #await receive(websocket)

                    # await send(websocket, {"message": input()})
                    # await receive(websocket)
                    # await receive(websocket)
                else:
                    await receive(websocket)
                    await send(websocket, {"message": input()})
                    await receive(websocket)
            except websockets.ConnectionClosed:
                await websocket.close()


def http_get():
    print("rooms, users")
    token = "14e08ecae920a80b982e61125d68787391b2ec53"
    where = input()
    req = requests.get(("http://176.124.204.174:8000/get_" + where), headers={"Authorization": ("Token " + token)})
    try:
        print(req.json())
    except:
        print(req)



def http_post():
    #req = requests.post("http://localhost:8000/login", json={'username': 'newUser', 'password': 'dfjsdfsdf'})
    where = input("login, registration, create_room, delete_room\n")

    #privet dfgdfgfffdfgdfg
    #privet11 dfgdfgfffdfgdfg

    if where == "login":
        json = {"username": "privet11", 'password': "dfgdfgfffdfgdfg"}
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json)
    elif where == "registration":
        json = {"username": "privet11", 'password': "dfgdfgfffdfgdfg"}
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json)
    elif where == "delete_room":
        token = "783f985d0d85eeca545dad3d4ec0a3987b8448ce"
        json = {"name": "chat1"}
        headers = {"Authorization": ("Token " + token)}
        # req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
    else:
        token = "783f985d0d85eeca545dad3d4ec0a3987b8448ce"
        json = {"name": "chat1"}
        headers = {"Authorization": ("Token " + token)}
        #req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
        req = requests.post(("http://176.124.204.174:8000/" + where), json=json, headers=headers)
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
