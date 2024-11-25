from django.db import models


# class Rooms():
#     name = ""
#     group = []
#
#     def add_to_group(self, message_to_add):
#         self.group.append(message_to_add.get())

class Rooms(models.Model):
    name = models.CharField(max_length=30)
    group = []


class Message(Rooms):
    username: str
    message = ''
    date = 0.0

    def get(self):
        return {"username": self.username, "message": self.message, "date": self.date}