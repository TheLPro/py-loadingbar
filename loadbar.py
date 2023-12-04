from time import sleep
import os
import random
from multiprocessing import Process

try:
    from termcolor import colored
except ImportError:
    print("Installing termcolor...")
    os.system("pip install termcolor --quiet")
    from termcolor import colored
    print(colored("Termcolor installed, please rerun the script", "white", attrs=["bold"]))
    exit()
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
class Bar:
        
    b = "█"
    d = "•"
    c = "light_green"
    tc = "white"
    s = random.randint(1, 5) / 100
    pf = "Loading"
    sf = "%"
    current = 0

    def bar(char):
        Bar.b = char
    def fill(char):
        Bar.d = char
    def color(color):
        Bar.c = color
    def textcolor(color):
        Bar.tc = color
    def speed(min, max, divider):
        Bar.speed = random.randint(min, max) / divider
    def prefix(prefix):
        Bar.pf = prefix
    def suffix(suffix):
        Bar.sf = suffix

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
            print(colored(f"{Bar.pf} {current + 1}{Bar.sf} {Bar.b*boxes}{Bar.d*dots}", Bar.c))
            sleep(Bar.s)
            current += 1
            if current == 100:
                return True
class Stage:

    # ← ↖ ↑ ↗ → ↘ ↓ ↙
    
    stages = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
    c = "light_green"
    tc = "white"
    s = 0.1
    pf = "Loading"
    current = 0
    max = len(stages)

    def color(color):
        Stage.c = color
    def textcolor(color):
        Stage.tc = color
    def speed(speed):
        Stage.s = speed
    def prefix(prefix):
        Stage.pf = prefix
    def chars(chars):
        Stage.stages = chars
        Stage.max = len(chars)
        
    def update(percent):
        current = Stage.current
        wm = Stage.max - 1
        for i in range(percent - current):
            for i in range(percent - current):
                cls()
                print(colored(f"{Stage.pf} {Stage.stages[current]}", Stage.c))
                sleep(Stage.s)
                current += 1
                if current == wm:
                    current = 0
        Stage.current = current
        return True
    
class Count:
        c = "light_green"
        tc = "white"
        s = random.randint(1, 5) / 200
        pf = "Loading"
        sf = ""
        
        current = 0
        max = 100
        
        def color(color):
            Count.c = color
        def textcolor(color):
            Count.tc = color
        def speed(min, max, divider):
            Count.s = random.randint(min, max) / divider
        def prefix(prefix):
            Count.pf = prefix
        def suffix(suffix):
            Count.sf = suffix
            
        def update(percent):
            current = Count.current
            for i in range(percent - current):
                cls()
                print(colored(f"{Count.pf} {current + 1}{Count.sf}", Count.c))
                sleep(Count.s)
                current += 1
                if current == Count.max:
                    return True
            Count.current = current
            return True