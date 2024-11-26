from chat.models import Rooms


def create_room_for_name(name):
    room = Rooms()
    try:
        if len(Rooms.objects.filter(name=name).values()) == 0:
            room.name = name
            room.save()
            return Rooms.objects.filter(name=name).values()[0]
        else:
            return None
    except:
        return None


def delete_room_for_name(name):
    try:
        if len(Rooms.objects.filter(name=name).values()) != 0:
            room = Rooms.objects.filter(name=name).values()[0]
            Rooms.objects.get(name=name).delete()
            return room
        else:
            return None
    except:
        return None


def give_rooms():
    return {"rooms": list(Rooms.objects.all().values())}

