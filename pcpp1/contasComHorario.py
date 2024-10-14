
class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.tempo = self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __mul__(self, other):
        self.hours *= other.hours
        self.minutes *= other.minutes
        self.seconds *= other.seconds
        self.tempo=self.hours * 3600 + self.minutes * 60 + self.seconds
        return self.tempo
    
    def __add__(self, other):
        self.tempo += other
        return self.tempo
    
    def __sub__(self, other):
        self.tempo-=other
        return self.tempo
    
    def __str__(self):
        self.days=0
        self.days, self.hours = divmod(self.tempo, 86400) #divmod retorna o quociente e o resto da divisão, respectivamente
        self.hours, self.minutes = divmod(self.tempo, 3600) 
        self.minutes, self.seconds = divmod(self.minutes, 60)
        return f'{self.days} dias {self.hours}h:{self.minutes}m:{self.seconds}s'
    
try:
    hours=int(input('Enter hours: '))
    minutes=int(input('Enter minutes: '))
    seconds=int(input('Enter seconds: '))
    t1 = TimeInterval(hours, minutes, seconds)
except Exception as e:
    print(e)
else:
    t2=t1*t1
    print(t1)
    t2=t1-800
    print(t1)
    t2=t1+800
    print(t1)
    
