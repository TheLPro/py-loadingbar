from termcolor import colored
from time import sleep
import os
import random
from multiprocessing import Process

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
class Bar:
        
    b = "█"
    d = "•"
    c = "light_green"
    s = random.randint(1, 5) / 100
    prefix = "Loading"
    suffix = "%"
    current = 0

    def bar(char):
        Bar.b = char
    def fill(char):
        Bar.d = char
    def color(color):
        Bar.c = color
    def speed(min, max, divider):
        Bar.speed = random.randint(min, max) / divider
    def prefix(prefix):
        Bar.prefix = prefix
    def suffix(suffix):
        Bar.suffix = suffix

    def update(percent):
        current = Bar.current
        for i in range(percent - current):
            if current == 0 or current == 1:
                boxes = 0
                dots = 50
            else:
                boxes = round(current / 2)
                dots = round((100 - current) / 2)
            cls()
            print(colored(f"{Bar.prefix} {current + 1}{Bar.suffix} {Bar.b*boxes}{Bar.d*dots}", Bar.c))
            sleep(Bar.s)
            current += 1
            if current == 100:
                return True
class Arrow:

    # ← ↖ ↑ ↗ → ↘ ↓ ↙
    
    stages = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
    c = "white"
    s = 0.1
    p = "Loading"
    current = 0
    max = len(stages)

    def color(color):
        Arrow.c = color
    def speed(speed):
        Arrow.s = speed
    def prefix(prefix):
        Arrow.p = prefix
    def chars(chars):
        Arrow.stages = chars
        Arrow.max = len(chars)
        
    def update(percent):
        current = Arrow.current
        wm = Arrow.max - 1
        for i in range(percent - current):
            for i in range(percent - current):
                cls()
                print(colored(f"{Arrow.p} {Arrow.stages[current]}", Arrow.c))
                sleep(Arrow.s)
                current += 1
                if current == wm:
                    current = 0
        Arrow.current = current
        return True