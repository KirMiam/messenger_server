a = [{'id': 1, 'name': 'chat1'}, {'id': 2, 'name': 'chat2'}, {'id': 3, 'name': 'chat2'}, {'id': 4, 'name': 'chat2'}, {'id': 5, 'name': 'chat2'}]
b = "chat1"
for i in a:
    if b in i["name"]:
