import media
class Series(media.Media):
    def __init__(self,n,dir,im,score,url,duration,casts,prise,part,tv_time):
        super().__init__(n,dir,im,score,url,duration,casts,prise)
        self.part=part
        self.tv_time=tv_time
    def add(self,):
        new=self.name +","+self.director+","+self.IMDB+","+self.score+","+self.url+","+self.duration+","+self.casts+","+self.prise+","+self.part+","+self.tv_time+ "\n"
        list1=open("date_base","a")
        list1.write(new)
        list1.close
        return list1
    def edit(self):
        self.subtract(self.name)
        self.add()
