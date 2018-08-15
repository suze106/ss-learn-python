
from observe.Person import person;
from observe.Remind1 import remind1;
import time;
from time import sleep

def main():
    remindTo = person();
    remindTo.addObserver(remind1());
    try:
        while True:
            remindTo.setCurrentTime(int(time.time())*1000);
            sleep(1);
    except KeyboardInterrupt as kbi:
        print("程序中断，强制退出");
        return;

if __name__ == '__main__':
    main();