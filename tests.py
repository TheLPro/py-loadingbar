from loadbar import Bar
from time import sleep
from multiprocessing import Process

def loadthis():
    sleep(2)
    print("Loaded this")
def loadthat():
    sleep(2)
    print("Loaded that")
b = Bar
b.bar("o")
b.fill("-")
b.color("light_magenta")
b.speed(1, 1, 10000000000)

this = Process(target=loadthis)
that = Process(target=loadthat)

this.start()
b.update(0, 50)
that.start()
b.update(50, 100)