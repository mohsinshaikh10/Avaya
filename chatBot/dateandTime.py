from datetime import date
from datetime import datetime
from time import sleep

from chatBot.SpeakAndListen import speak
def dateandtimefunc():
    today = date.today()
    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    print(d2)
    # speak(d2)
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print(dt_string)
    # speak(dt_string)

# def myAlarm():
#     print("Enter the time to set")
#     sethr = input("Hrs :")
#     setmin = input("Mins :")
#     alarmtime = f"{sethr}:{setmin}:00"
#     print(alarmtime)
#     now = datetime.now()
#     nowtime = now.strftime("%H:%M:%S")
#     while(1):
#         if nowtime == alarmtime:
#             print("Time to wake up")
#
# while(1):
#     sleep(1)
#     dateandtimefunc()