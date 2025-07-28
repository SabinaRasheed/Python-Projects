import time
from pync import Notifier #pip3 install pync
#from plyer import notification pip3 install plyer for windows

while True:
    print("Please drink some water!")
    Notifier.notify("It's time to hydrate your body!", title="Drink Water Reminder")
    time.sleep(3600) # Remind every hour
