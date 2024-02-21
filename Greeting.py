from datetime import datetime
import pytz

class Greeting():
    def __init__(self,timezone):
        self.timezone = timezone
        self.tz = pytz.timezone(self.timezone)
        thetime = datetime.now(self.tz)
        self.time = thetime.strftime('%I:%M %p')
        self.get_greeting() #initialize self.greeting
    
    #getters
    def get_timezone(self):
        return self.timezone
    def get_time(self):
        thetime = datetime.now(self.tz)
        return thetime.strftime('%I:%M %p')
    def get_greeting(self):
        local_time = datetime.now(self.tz)
        hour = local_time.hour
        if hour in range(4,12):
            self.greeting = "Good morning"
        elif hour in range(12,17):
            self.greeting = "Good afternoon"
        else:
            self.greeting = "Good evening"
        return self.greeting
    
    #setter(s)
    def set_timezone(self,val):
        self.timezone = val