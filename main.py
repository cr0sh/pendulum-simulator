import math

global gravity, length
gravity = 9.80665
length = 0.6

class pendulum:
    def __init__(self, radian):
        self.radian = radian
        self.x = length * math.sin(radian)
        self.vx = 0
        self.mass = 0.15
        self.resist = 0.5

    def velocity(self, time):
        linear = gravity * math.sin(self.radian) * time # 선속도
        resist = linear * self.resist * time / self.mass
        self.vx -= math.fabs(self.radian * (linear - resist) * math.cos(self.radian)) / self.radian # Vector-x

    def apply_radians(self):
        self.radian = math.asin(self.x / length)

    def move(self, time):
        self.x += self.vx * time
        self.apply_radians()

config = (140000, 0.1, 20) # 계산 시간, 측정 간격, 초기 설정 각도
secs = total = cnt = 0
last = None
p = pendulum(math.radians(config[2]))

while secs < config[0]:
    toright = bool(p.vx > 0)
    p.velocity(config[1])
    p.move(config[1])
    #print(p.x, p.y)
    if toright == bool(p.vx < 0) and p.vx > 0:
        #print("[!] Turn", secs, p.x)
        if last == None:
            print('setting')
            last = secs
        else:
            total += (secs - last)
            last = secs
            cnt += 1

    secs += config[1]

avr = total/cnt
est = 2*math.pi*math.sqrt(length/gravity)

print('Average period: %s, Estimated: %s, miss: %s' %(avr, est, avr - est))
