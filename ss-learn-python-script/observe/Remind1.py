from observe.Remind import remind;
import datetime;

class remind1(remind):

    def do(self,time):
        time_ = time%1534329828000;
        time__ = int(time_%(5*1000));
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'\t',time__);
        if time__==0:
            print('到时间了,该XXOO了')