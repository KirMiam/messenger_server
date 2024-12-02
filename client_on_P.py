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


async def connect_to_server(ip):
    print("1 or 2")
    a = input()
    if a == "1":
        print("Ivan")
        token = "c2eeef6e8d787060553f30d8428c597e9607799a"
    else:
        print("valya")
        token = 'f7d2fc0402bb871d628c54d3832fb1a07b9e3398'
    print("1)get messages store\n2)not get message store")
    check_MS = input()
    print("1)solo\n2)duo")
    check_group_mess = input()
    print("id of room")
    id_of_room = input()
    async with websockets.connect("ws://" + ip + ":8000/ws/chat/" + id_of_room + "/",
                                  extra_headers={"Authorization": ("Token " + token)}) as websocket:
        f = True
        if check_MS == "1":
            await receive(websocket)
        while f:
            try:
                if a == "1":
                    await send(websocket, {"message": input()})
                    await receive(websocket)
                    if check_group_mess == "2":
                        await receive(websocket)
                else:
                    await receive(websocket)
                    await send(websocket, {"message": input()})
                    await receive(websocket)
            except websockets.ConnectionClosed:
                websocket.close()


def http_get(ip):
    print("1)create_rooms\n2)delete_rooms\n3)get_rooms\n4)get_users\n5)get_superusers")
    where = input()
    print("1)user\n2)superuser")
    who = input()
    if who == "1":
        token = "c2eeef6e8d787060553f30d8428c597e9607799a"
    else:
        token = "e688a52e76df58f69f7ca16ff94caa64f04a7508"
    if where == "1":
        where = "create_rooms"
        print("name")
        name_or_id = "?name=" + input()
    elif where == "2":
        where = "delete_rooms"
        print("id")
        name_or_id = "?id=" + input()
    elif where == "3":
        where = "get_rooms"
        name_or_id = ""
    elif where == "4":
        where = "get_users?id="
        print("id")
        name_or_id = "?id=" + input()
    else:
        where = "get_superusers"
        name_or_id = ""
    req = requests.get(("http://" + ip + ":8000/" + where + name_or_id), headers={"Authorization": ("Token " + token)})
    try:
        print(req.json())
    except:
        print(req)


def http_post(ip):
    print("1)login\n2)registration")
    where = input()

    # kirill 1234567890 '80d2d77f1fe88d96a92ca51a1935bb6882a53f34'
    # valya 0987654321qqq 'f7d2fc0402bb871d628c54d3832fb1a07b9e3398'

    if where == "1":
        where = 'login'
        json = {{"username": "Ivan", 'password': "0987654321qqq"}}
    else:
        where = "registration"
        json = {"username": "Ivan", 'password': "0987654321qqq"}

    req = requests.post(("http://" + ip + ":8000/" + where), json=json)
    try:
        print(req.json())
    except:
        print(req)


print("1)server\n2)localhost")
ip = input()
if ip == "1":
    ip = "176.124.204.174"
else:
    ip = "localhost"
print("1)ws\n2)get\n3)post")
what_do = input()
if what_do == '1':
    asyncio.get_event_loop().run_until_complete(connect_to_server(ip))
elif what_do == '2':
    http_get(ip)
elif what_do == '3':
    http_post(ip)
else:
    print("try again")
