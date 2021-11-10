class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_time_valid(self):
        self.hour, self.minute, self.second = map(int,time_string.split(':'))
        return self.hour <= 24 and self.minute <= 59 and self.second <= 60
 
    def from_string(self):
        return self.hour, self.minute, self.second


time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')