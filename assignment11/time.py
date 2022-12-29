class Time:
    def __init__(self,hour,min,sec):
        super
        self.hour=hour
        self.min=min
        self.sec=sec
    # method
    def fix(self):
        if self.sec>60:
            self.sec-=60
            self.min+=1
        elif self.sec<0:
            self.min-=1
            self.sec+=60
        elif self.min>60:
            self.min-=60
            self.hour+=1
        elif self.min<0:
            self.hour-=1
            self.min+=60
        
    def show(self):
        self.fix()
        print(self.hour,":",self.min,":",self.sec)
    def add(self,time2):
        hour1=self.hour+time2.hour
        min1=self.min+time2.min
        sec1=self.sec+time2.sec
        return Time(hour1,min1,sec1)
    def subtract(self,time2):
        hour1=self.hour-time2.hour
        min1=self.min-time2.min
        sec1=self.sec-time2.sec
        return Time(hour1,min1,sec1)
    
    def time_to_second(self):
        second1=self.hour*3600+self.min*60+self.sec
        return second1
    @staticmethod
    def second_to_time(times):
        time1=times//3600
        time2=(times-(time1*3600))//60
        time=times-((time1*3600)+(time2*60))
        return Time(time1,time2,time)
    def gmt_to_mashhad(self):
        hour=self.hour+4
        return Time(hour,self.min,self.sec)
    def country_to_gmt(self,time_difference):
        hour1=self.hour+time_difference.hour
        min1=self.min+time_difference.min
        sec1=self.sec+time_difference.sec
        return Time(hour1,min1,sec1)



# object
t1=Time(1,30,0)
t1.show()
t2=Time(2,50,10)
t3=t1.add(t2)
t3.show()
t4=t3.subtract(t2)
t4.show()
print(t4.time_to_second())
t5=Time.second_to_time(5400)
t5.show()
t6=t5.gmt_to_mashhad()
t6.show()
t7=t6.country_to_gmt(Time(2,30,50))
t7.show()