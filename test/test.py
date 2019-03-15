from datetime import datetime

from khayyam3 import JalaliDatetime



datetime1=datetime.now()
print(datetime1)
# payment_j_datetime = JalaliDatetime().strftime('%C')
# print(payment_j_datetime)

print(JalaliDatetime.from_datetime(datetime1).strftime('%C'))