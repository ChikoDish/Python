from datetime import datetime
from playsound import playsound

alarm = input("Enter the alarm time HH:MM:SS\n")
alarm_hr = alarm[0:2]
alarm_mm = alarm[3:5]
alarm_ss = alarm[6:8]
alarm_period = alarm[9:11].upper()
print("Good Night!")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hr == current_hour):
            if(alarm_mm == current_minute):
                if(alarm_ss == current_seconds):
                    print("Wake Up!")
                    playsound('alarm.mp3')
                    break
