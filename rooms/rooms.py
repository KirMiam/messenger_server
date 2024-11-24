from chat.models import Rooms


def create_room_for_name(name):
    room = Rooms()
    try:
        if name not in list(Rooms.objects.filter(name=name).values())[0]["name"]:
            room.name = name
            room.save()
            return list(Rooms.objects.filter(name=name).values())[0]
        else:
            return None
    except:
        return None


def give_rooms():
    return {"rooms" : list(Rooms.objects.all().values())}

