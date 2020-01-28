import threading
import time
from win10toast import ToastNotifier
'''
going to be forking the win10toast github repo to play with for more functionality
'''
def background():
    global reminders
    global reminder_time
    global reminder_text

    i = 0
    while True:
        with open("reminders.txt", "r") as re:
            for x in re.readlines():
                current_time = time.strftime("%H:%M")
                x = x.rstrip()
                if current_time in x:
                    toaster.show_toast("Reminder!", x, duration = None, threaded = True)
                else:
                    continue
            
        
def foreground():
    global reminder_time
    global reminder_text

    while True:
        with open("reminders.txt", "a") as re:
            reminder_time = input("\nEnter reminder time: ")
            reminder_text = input("\nEnter reminder text: ")

            re.write(reminder_time + ";" + reminder_text + "\n")                
        

toaster = ToastNotifier()

b = threading.Thread(name = "background", target = background)
f = threading.Thread(name = "foreground", target = foreground)

f.start()
b.start()
