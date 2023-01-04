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
    def read_datebase(self):
        date_base=open("date_base","r")
        file=[]
        for i in date_base:
            v=i.split(",")
            r={"name":v[0],"director":v[1],"IMDB":v[2],"score":v[3],"url":v[4],"duration":v[5],"casts":v[6],"prise":v[7]}
            file.append(r)
        date_base.close()
        return file
    def subtract(self,name):
        list1=self.read_datebase()
        for i in list1:
            if i["name"]==name:
                list1.pop(i)
    def qrcode_url(self,name):
        m=0
        list1=self.read_datebase()
        for i in list1:
            if i["name"]==name:
                n=qrcode.make(i["url"])
                n.save("qrcode_url.png")
                m=1
        if m==0:
            print("i can't find it")
    def find(self,moudle,karbar):
        num=0
        list1=self.read_datebase()
        if moudle=="name":
            for i in list1:
                if i["name"] == karbar:
                    print(i)
                    num=1
        if moudle=="duration":
            for i in list1:
                if i["duration"] == karbar:
                    print(i)
                    num=1
        if num==0:
            print("i can't find it")
    def show_list(self):
        list1=self.read_datebase()
        for i in list1:
            print(i)
    def download(self,name):
        list1=self.read_datebase()
        for i in list1:
            if i["name"]==name:
                yt=YouTube(i["url"])
                yt.streams.filter(adaptive=True)
                yt.streams.first().download()


