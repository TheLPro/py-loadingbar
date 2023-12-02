from loadbar import Arrow
from time import sleep
from multiprocessing import Process

def loadthis():
    sleep(2)
    print("Loaded this")
def loadthat():
    sleep(2)
    print("Loaded that")
b = Arrow
b.color("light_magenta")
b.speed(.1)

this = Process(target=loadthis)
that = Process(target=loadthat)

b.start()
b.stop()