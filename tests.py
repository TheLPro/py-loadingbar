import loadbar as load
from time import sleep
from multiprocessing import Process

def loadthis():
    sleep(2)
    print("Loaded this")
def loadthat():
    sleep(2)
    print("Loaded that")
b = load.Bar

b.color("red")
b.bar("▲")
b.fill("▼")
b.prefix("UWU")
b.suffix("OwO")
b.speed(3, 8, 100)

this = Process(target=loadthis)
that = Process(target=loadthat)
bar = Process(target=b.update, args=(100,))

bar.start()
this.start()