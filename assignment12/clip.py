import media
class Clip(media.Media):
    def __init__(self,n,dir,im,score,url,duration,casts,prise):
        super().__init__(n,dir,im,score,url,duration,casts,prise)
    def add(self,):
        new=self.name +","+self.director+","+self.IMDB+","+self.score+","+self.url+","+self.duration+","+self.casts+","+self.prise+"\n"
        list1=open("date_base","a")
        list1.write(new)
        list1.close
        return list1
    def edit(self):
        self.subtract(self.name)
        self.add()
