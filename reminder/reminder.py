import time 
from win10toast import ToastNotifier
toast = ToastNotifier()
try:
    print("Title of reminder")
    title = input()
    print("Message of reminder")
    message = input()
    print("In how many minutes?")
    time_min = input()
    time_min = float(time_min)
except:
    title = input("Title of reminder\n")
    message = input("Message of reminder\n")
    time_min = float(input("In how many minutes?\n"))
time_min = time_min * 60
print("Setting up reminder..")
time.sleep(2)
print("all set!")
time.sleep(time_min)
toast.show_toast(f"{title}",
                   f"{message}",
                   duration=10,
                   threaded=True)
while toast.notification_active():
    time.sleep(0.005)
