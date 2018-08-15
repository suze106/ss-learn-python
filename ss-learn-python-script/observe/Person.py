
from observe.Remind import remind;

class person:

    def __init__(self):
        self.__observers = [];


    def addObserver(self,observer):
        if isinstance(observer,remind):
            self.__observers.append(observer);
        else:
            raise TypeError('observer must instance Remind');


    def setCurrentTime(self,time):
        self.time = time;
        self.notifies();



    def notifies(self):
        for item in self.__observers:
            item.do(self.time);