class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return str(minutes) + ":" + str(seconds)

    def convert_to_hours(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        return str(hours) + ":" + str(minutes) + ":" + str(seconds)
s = int(input("Enter time in seconds: "))
t = Time(s)
print("Minutes and Seconds:", t.convert_to_minutes())
print("Hours, Minutes and Seconds:", t.convert_to_hours())
