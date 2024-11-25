#a = [{'id': 1, 'name': 'chat1'}, {'id': 2, 'name': 'chat2'}, {'id': 3, 'name': 'chat2'}, {'id': 4, 'name': 'chat2'}, {'id': 5, 'name': 'chat2'}]
# a = []
# if len(a) > 0:
#     print(a[0]["name"])

import datetime
import time

#print(time.gmtime())
#print(time.time())
epoch = time.time()
epoch_date_time = datetime.datetime.fromtimestamp(epoch)
print(time.time())
print(datetime.date.today().isoformat() + " " + str(datetime.datetime.now().time()).split(".")[0])