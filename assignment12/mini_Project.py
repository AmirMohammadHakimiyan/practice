import actor
import series
import film
import documenary
import clip
import pyfiglet
t=pyfiglet.figlet_format("HELLOW",font="slant")
print(t)
fake_objects=series.Series(1,2,3,4,5,6,7,8,4,4)
fake_objectf=film.Film(1,2,3,4,5,6,7,6)
fake_objectc=clip.Clip(1,2,3,4,5,6,7,5)
fake_objectd=documenary.Documentary(1,2,3,4,5,6,7,7,5)

while True:
    choice=input("add:(1) ,subtract:(2) ,qrcode url:(3) ,find:(4) ,show list:5,edit:(6) ,download enter the(7) or for exit enter the 8:")
    if int(choice)==1:
        choice2=input("what is it?series,film,clip or documenary")
        if choice2 == "series":
            print("use (,) between parametr")
            choice3=input("write the ,name,director,IMBD,score,url,duration,prise,part,TV_time:")
            kc=input("enter casts, use(|)")
            q=choice3.split(",")
            casts=actor.Actors(kc,None)
            new_series=series.Series(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],casts.names,q[8])
            new_series.add()
        elif choice2=="film":
            kc=input("enter casts, use(|)")
            casts=actor.Actors(kc,None)
            print("use (,) between parametr")
            choice3=input("write the name,director,IMBD,score,url,duration,prise:")
            q=choice3.split(",")
            new_film=film.Film(q[0],q[1],q[2],q[3],q[4],q[5],casts.names,q[6])
            new_film.add()
        elif choice2=="clip":
            kc=input("enter casts, use(|)")
            casts=actor.Actors(kc,None)
            print("use (,) between parametr")
            choice3=input("write the name,director,IMBD,score,url,duration,casts,prise:")
            q=choice3.split(",")
            new_clip=clip.Clip(q[0],q[1],q[2],q[3],q[4],q[5],casts.names,q[6])
            new_clip.add()
        elif choice2 =="documenary":
            kc=input("enter casts, use(|)")
            casts=actor.Actors(kc,None)
            print("use (,) between parametr")
            choice3=input("write the plase,name,director,IMBD,score,url,duration,prise,place:")
            q=choice3.split(",")
            new_documenary=documenary.Documentary(q[0],q[1],q[2],q[3],q[4],q[5],q[6],casts.names,q[7])
            new_documenary.add()
    elif int(choice) == 2:
        choice2=input("what is it?series,film,clip or documenary:")
        if choice2 == "series":
            choice3=input("name")
            fake_objects.subtract(choice3)
        if choice2=="film":
            choice3=input("name")
            fake_objectf.subtract(choice3)
        elif choice2=="clip":
            choice3=input("name")
            fake_objectc.subtract(choice3)
        elif choice2 =="documenary":
            choice3=input("name")
            fake_objectd.subtract(choice3)
    elif int(choice)==3:
        choice2=input("what is it?series,film,clip or documenary:")
        if choice2 == "series":
            choice3=input("name")
            fake_objects.qrcode_url(choice3)
        elif choice2=="film":
            choice3=input("name")
            fake_objectf.qrcode_url(choice3)
        elif choice2=="clip":
            choice3=input("name")
            fake_objectc.qrcode_url(choice3)
        elif choice2 =="documenary":
            choice3=input("name")
            fake_objectd.qrcode_url(choice3)
    elif int(choice)==4:

        choice2=input("what is it?series,film,clip or documenary")
        moudle=input("how do you want to searching?name or duration")
        karbar=input("what is name or duration please just choice one of them.")
        if choice2 == "series":
            fake_objects.find(moudle,karbar)
        elif choice2=="film":
            fake_objectf.find(moudle,karbar)
        elif choice2=="clip":
            choice3=input("name")
            fake_objectc.find(moudle,karbar)
        elif choice2 =="documenary":
            fake_objectd.find(moudle,karbar)
    elif int(choice)==5:
        fake_objects.show_list()
    elif int(choice)==6:
        choice2=input("what is it?series,film,clip or documenary:")
        if choice2 == "series":
            old=input("enter the name")
            print("use (,) between parametr")
            choice3=input("write the new series ,name,director,IMBD,score,url,duration,casts,prise,part,TV_time:")
            q=choice3.split(",")
            new_series=series.Series(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9])
            fake_objects.subtract(old)
            new_series.add()
        elif choice2=="film":
            old=input("enter the name:")
            print("use (,) between parametr:")
            choice3=input("write the new film name,director,IMBD,score,url,duration,casts,prise:")
            q=choice3.split(",")
            new_film=film.Film(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7])
            new_film.add()
            fake_objects.subtract(old)
        elif choice2=="clip":
            old=input("enter the name:")
            print("use (,) between parametr:")
            choice3=input("write the name,director,IMBD,score,url,duration,casts,prise:")
            q=choice3.split(",")
            new_clip=clip.Clip(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7])
            new_clip.add()
            fake_objects.subtract(old)
        elif choice2 =="documenary":
            old=input("enter the name")
            print("use (,) between parametr")
            choice3=input("write the plase,name,director,IMBD,score,url,duration,casts,prise,place:")
            q=choice3.split(",")
            new_documenary=documenary.Documentary(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8])
            new_documenary.add()
            fake_objects.subtract(old)
    elif int(choice)==7:
        name=input("write the name.")
        fake_objects.subtract(name)
    elif int(choice)==8:
        exit(0)