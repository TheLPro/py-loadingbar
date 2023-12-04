import loadbar as load
from time import sleep
from multiprocessing import Process

def loadthis():
    sleep(2)
    print("Loaded this")
def loadthat():
    sleep(2)
    print("Loaded that")
b = load.Stage

b.color("light_red")
b.chars(["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"])

this = Process(target=loadthis)
that = Process(target=loadthat)

this.start()
b.update(20)