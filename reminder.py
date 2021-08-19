import time
from win10toast import ToastNotifier
from playsound import playsound
print("What shall I remind you about?")
text = str(input())
print("In how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
playsound('song.mp3')
toast = ToastNotifier()
toast.show_toast("Reminder", text ,duration=20,icon_path="icon.ico")

