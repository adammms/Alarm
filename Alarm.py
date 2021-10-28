import time
import winsound
from win10toast import ToastNotifier

def timer(message, minutes):
    #Windows Notification Instantiator
    notificator = ToastNotifier()
    #Notification Details
    notificator.show_toast("Alarm", f"Aalarm will go off in {1} minutes..",
                           duration=50)
    #Pause Script
    time.sleep(minutes * 60)
    #Alarm Sound
    winsound.Beep(frequency=2500, duration=1000)
    #Show Notification
    notificator.show._toast(f"Alarm", message, duration=50)

if __name__ == "__main__":
    message = "Post on github!"
    minutes = 1
    timer(message, minutes)