import qrcode
from pytube import YouTube
class Media():
    def __init__(self,n,dir,im,score,url,duration,casts,prise):
        self.name=n
        self.director=dir
        self.IMDB=im
        self.score=score
        self.url=url
        self.duration=duration
        self.casts=casts
        self.prise=prise
    # def read_datebase(self):
    #     date_ba=open("date_base","r")
    #     file=[]
    #     for i in date_ba:
    #         v=i.split(",")
    #         r=[{"name":v[0],"director":v[1],"IMDB":v[2],"score":v[3],"url":v[4],"duration":v[5],"casts":v[6],"prise":v[7]}]
    #         file.append(r)
        # date_ba.close()
        # filereturn 
    def subtract(self,name):
        self.list1=open("date_base","r")
        for i in self.list1.readlines():
            n=i.split(",")
            if n[0]==name:
                self.h=i
                print(i)
            
        self.list1.close()
        self.list2=open("date_base","r")
        self.new=self.list2.read()
        self.new_list=self.new.replace(self.h,"         !!delete!!")
        self.list2.close()
        self.list3=open("date_base","w")
        self.list3.write(self.new_list)
        # self.list3=self.list1.read()
        # self.list2.write(new)
        self.list3.close()
    def qrcode_url(self,name):
        m=0
        self.list1=open("date_base","r")
        for i in self.list1.readlines():
            self.b=i.split(",")
            if self.b[0]==name:
                n=qrcode.make(self.b[4])
                n.save("qrcode_url.png")
                m=1
        if m==0:
            print("i can't find it")
    def find(self,moudle,karbar):
        num=0
        self.list1=open("date_base","r")
        if moudle=="name":
            for i in self.list1.readlines():
                self.b=i.split(",")
                if self.b[0] == karbar:
                    print(i)
                    num=1
        if moudle=="duration":
            for i in self.list1.raedlines():
                self.b=i.split(",")
                if self.b[5] == karbar:
                    print(i)
                    num=1
        self.list1.close()
        if num==0:
            print("i can't find it")
    def show_list(self):
        self.list1=open("date_base","r")
        for i in self.list1.readlines():
            print(i)
        self.list1.close()
    def download(self,name):
        self.list1=open("read_datebase()","r")
        for i in self.list1.readlines():
            self.b=i.split(",")
            if self.b[0]==name:
                yt=YouTube(self.b[4])
                yt.streams.filter(adaptive=True)
                yt.streams.first().download()


